import requests

def get_book_description(isbn):
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data['items'][0]['volumeInfo'].get('description', 'No description available')


def get_recommendations(cursor, book):
    cursor.execute(
        """
        SELECT isbn, book_title, book_author, Image_URL_L, price,
            CASE
                WHEN book_author LIKE %s THEN 1
                WHEN publisher = %s THEN 2
                WHEN year_of_publication >= %s THEN 3
                ELSE 4
            END AS priority
        FROM books_data
        WHERE book_author LIKE %s
        OR publisher = %s
        OR year_of_publication >= %s
        ORDER BY priority
        LIMIT 8
        """,
        (
            "%" + book["book_author"] + "%",
            book["publisher"],
            book["year_of_publication"],
            "%" + book["book_author"] + "%",
            book["publisher"],
            book["year_of_publication"],
        )
    )
    recommendations = cursor.fetchall()
    return recommendations


def get_books_query(base_query, params, sort, per_page, offset):
    query = (
        "SELECT isbn, book_title, book_author, Image_URL_L, price, ratings, num_ratings "
        + base_query
    )
    if sort == "latest":
        query += " ORDER BY Year_of_Publication DESC"
    elif sort == "oldest":
        query += " ORDER BY Year_of_Publication ASC"
    elif sort == "price_asc":
        query += " ORDER BY price ASC"
    elif sort == "price_desc":
        query += " ORDER BY price DESC"
    elif sort == "popular":
        query += " ORDER BY (ratings / num_ratings) DESC"
    query += " LIMIT %s OFFSET %s"
    params.extend([per_page, offset])
    return query, params


def isInWishlist(cursor, user_id, books):
    cursor.execute(
            "SELECT isbn FROM wishlist WHERE user_id=%s",
            [user_id],
        )
    wishlist = cursor.fetchall()
    wishlist_isbns = {item["isbn"] for item in wishlist}    
    
    for book in books:
        book["wish"] = book["isbn"] in wishlist_isbns
    
    return books