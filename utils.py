import requests

def get_book_description(isbn):
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
    response = requests.get(url)
    
    if response:
        data = response.json()
        if 'items' in data:
            return data['items'][0]['volumeInfo'].get('description', 'No description available.')
    return 'No description available.'


def get_recommendations(cursor, book):
    cursor.execute(
        """
        SELECT isbn, book_title, book_author, Image_URL_L, price,
            CASE
                WHEN book_author LIKE %s THEN 1
                WHEN publisher = %s THEN 2
                WHEN year_of_publication = %s THEN 3
                ELSE 4
            END AS priority
        FROM books_data
        WHERE book_author LIKE %s
        OR publisher = %s
        OR year_of_publication = %s
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
