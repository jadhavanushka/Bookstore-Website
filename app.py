from flask import Flask, flash, redirect, render_template, request, session, url_for
from functools import wraps
import pymysql
import pymysql.cursors
import os
from dotenv import load_dotenv
import re
from requests.exceptions import ConnectionError
from utils import (
    get_book_description,
    get_recommendations,
    get_books_query,
    isInWishlist,
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")

load_dotenv()  # Load from .env


def get_db_connection():
    return pymysql.connect(
        host = os.getenv("DB_HOST"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASS"),
        database = os.getenv("DB_NAME"),
        cursorclass = pymysql.cursors.DictCursor,
    )


# Home page
@app.route("/")
def home():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT isbn, book_title, book_author, Image_URL_L, price FROM books_data ORDER BY Year_of_Publication DESC LIMIT 8"
    )
    new = cursor.fetchall()

    cursor.execute(
        "SELECT isbn, book_title, book_author, Image_URL_L, price FROM books_data ORDER BY ratings DESC, Year_of_Publication DESC LIMIT 8"
    )
    featured = cursor.fetchall()

    cursor.execute(
        "SELECT isbn, book_title, book_author, Image_URL_L, price FROM books_data ORDER BY Year_of_Publication LIMIT 8"
    )
    classic = cursor.fetchall()

    if "loggedin" in session:
        new = isInWishlist(cursor, session["id"], new)
        featured = isInWishlist(cursor, session["id"], featured)
        classic = isInWishlist(cursor, session["id"], classic)
        
    cursor.close()
    conn.close()
    
    return render_template("home.html", new=new, classic=classic, featured=featured)


# Sign up page
@app.route("/signup", methods=["GET", "POST"])
def signup():
    # Output message if something goes wrong...
    msg = ""
    # Check if all " POST requests exist (user submitted form)
    if (
        request.method == "POST"
        and "fname" in request.form
        and "lname" in request.form
        and "email" in request.form
        and "password" in request.form
        and "confirm" in request.form
    ):
        fname = request.form["fname"]
        lname = request.form["lname"]
        email = request.form["email"]
        password = request.form["password"]
        confirm = request.form["confirm"]

        # Check if account exists
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE user_email = %s", [email])
        account = cursor.fetchone()

        # If account exists show error
        if account:
            msg = "Account already exists"
        # validation checks
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            msg = "Invalid email address"
        elif not password == confirm:
            msg = "Passwords do not match"
        # Account doesnt exists and the form data is valid, insert new account into users table
        else:
            hashed_password = generate_password_hash(password)
            cursor.execute(
                "INSERT INTO users VALUES (NULL, %s, %s, %s, %s, NULL)",
                (fname, lname, email, hashed_password),
            )
            conn.commit()

            # Log in to the account
            cursor.execute("SELECT user_id FROM users WHERE user_email = %s", [email])
            # Fetch one record and return result
            account = cursor.fetchone()

            # If account exists in accounts table in out database
            if account:
                # Create session data, we can access this data in other routes
                session["loggedin"] = True
                session["id"] = account["user_id"]
                session["email"] = email

                flash("New account created!", "success")

                # Redirect to home page
                return redirect(url_for("home"))

        cursor.close()
        conn.close()

    # Show registration form with message (if any)
    return render_template("signup.html", msg=msg)


# Login page
@app.route("/login", methods=["GET", "POST"])
def login():
    # Output message if something goes wrong...
    msg = ""
    # Check if "email" and "password" POST requests exist (user submitted form)
    if (
        request.method == "POST"
        and "email" in request.form
        and "password" in request.form
    ):
        # Create variables for easy access
        email = request.form["email"]
        password = request.form["password"]

        # Check if account exists using MySQL
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE user_email = %s", [email])
        # Fetch one record and return result
        account = cursor.fetchone()

        # If account exists in users table in out database
        if account:
            if check_password_hash(account["user_password"], password):
                # Create session data, we can access this data in other routes
                session["loggedin"] = True
                session["id"] = account["user_id"]
                session["email"] = account["user_email"]

                flash("Logged in!", "success")

                # Redirect to home page
                return redirect(url_for("home"))

            else:
                msg = "Incorrect password"
                return render_template("login.html", msg=msg)

        else:
            # Account doesnt exist email is incorrect
            msg = "Cannot find the account. Incorrect email"

        cursor.close()
        conn.close()
        
    return render_template("login.html", msg=msg)


# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "loggedin" in session:
            return f(*args, **kwargs)
        else:
            flash("Please login to continue", "danger")
            return redirect(url_for("login"))

    return wrap


# Log out
@app.route("/logout")
@is_logged_in
def logout():
    # Remove session data, this will log the user out
    session.pop("loggedin", None)
    session.pop("id", None)
    session.pop("email", None)

    flash("Logged out", "success")

    # Redirect to login page
    return redirect(url_for("home"))


# profile page
@app.route("/profile")
@is_logged_in
def profile():
    user_id = session["id"]
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id = %s", [user_id])
    user = cursor.fetchone()

    cursor.execute("SELECT * FROM orders WHERE user_id = %s ORDER BY order_date DESC", [user_id])
    orders = cursor.fetchall()

    for order in orders:
        cursor.execute(
            """SELECT Book_Title, Image_URL_L, price, quantity FROM orders NATURAL LEFT JOIN 
            order_items NATURAL LEFT JOIN books_data WHERE user_id = %s and order_id=%s""",
            (user_id, order["order_id"]),
        )
        order_items = cursor.fetchall()
        order["order_items"] = order_items

    cursor.execute(
        "select * from wishlist natural left outer join books_data where user_id=%s",
        [user_id],
    )
    wishlist = cursor.fetchall()

    cursor.execute("SELECT * FROM addresses WHERE user_id = %s", [user_id])
    addresses = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template(
        "profile.html", user=user, orders=orders, wishlist=wishlist, addresses=addresses
    )


@app.route("/edit_profile", methods=["POST"])
@is_logged_in
def edit_profile():
    user_id = session["id"]
    conn = get_db_connection()
    cursor = conn.cursor()

    fname = request.form.get("fname")
    lname = request.form.get("lname")
    email = request.form.get("email")
    phone = request.form.get("phone")

    cursor.execute(
        "UPDATE users SET first_name = %s, last_name = %s, user_email = %s, phone = %s WHERE user_id = %s",
        (fname, lname, email, phone, user_id),
    )
    
    conn.commit()
    cursor.close()
    conn.close()
    
    return redirect(url_for("profile", tab="profile-info"))


# change password
@app.route("/change_password", methods=["POST"])
def change_password():
    current_password = request.form["current_password"]
    new_password = request.form["new_password"]
    confirm = request.form["confirm"]
    user_id = session["id"]

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT user_password FROM users WHERE user_id = %s", [user_id])
    user = cursor.fetchone()

    if check_password_hash(user["user_password"], current_password):
        if new_password == confirm:
            hashed_new_password = generate_password_hash(new_password)
            # Update password
            cursor.execute(
                "UPDATE users SET user_password=%s WHERE user_id = %s",
                (hashed_new_password, user_id),
            )
            conn.commit()
            flash("Password changed successfully", "success")
        else:
            flash("Passwords do not match", "danger")
    else:
        flash("Incorrect current password", "danger")

    cursor.close()
    conn.close()
    
    return redirect(url_for("profile", tab="change-password"))


# Shop page
@app.route("/shop")
def shop():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Get filter and sort parameters
    min_price = request.args.get("min_price", 0, type=int)
    max_price = request.args.get("max_price", 1000, type=int)
    rating = request.args.get("rating", 0, type=int)
    sort = request.args.get("sort", "latest")
    query = request.args.get("q", "", type=str)

    # Base query for filtering
    if query:
        base_query = """
            FROM books_data
            WHERE (book_title LIKE %s OR book_author LIKE %s)
            AND price BETWEEN %s AND %s AND ratings >= %s
        """
        search_term = f"%{query}%"
        params = [search_term, search_term, min_price, max_price, rating]
    else:
        base_query = """
            FROM books_data
            WHERE price BETWEEN %s AND %s AND ratings >= %s
        """
        params = [min_price, max_price, rating]

    # Count total books for pagination
    count_query = "SELECT COUNT(*) " + base_query
    cursor.execute(count_query, params)
    total_books = cursor.fetchone()["COUNT(*)"]

    # Calculate total pages
    per_page = 30
    total_pages = (total_books + per_page - 1) // per_page

    # Limit and offset for pagination
    page = request.args.get("page", 1, type=int)
    offset = (page - 1) * per_page

    # Get books
    query_string, params = get_books_query(base_query, params, sort, per_page, offset)
    cursor.execute(query_string, params)
    books = cursor.fetchall()

    if "loggedin" in session:
        books = isInWishlist(cursor, session["id"], books)

    cursor.close()
    conn.close()
    
    return render_template(
        "shop.html",
        books=books,
        total_pages=total_pages,
        page=page,
        min_price=min_price,
        max_price=max_price,
        rating=rating,
        sort=sort,
        search_query=query,
    )


@app.route("/shop/category/<category>")
def shop_category(category):
    conn = get_db_connection()
    cursor = conn.cursor()

    if category == "new":
        cursor.execute(
            "SELECT isbn, book_title, book_author, Image_URL_L, price FROM books_data ORDER BY Year_of_Publication DESC LIMIT 30"
        )
    elif category == "featured":
        cursor.execute(
            "SELECT isbn, book_title, book_author, Image_URL_L, price FROM books_data ORDER BY ratings DESC, Year_of_Publication DESC LIMIT 30"
        )
    elif category == "classic":
        cursor.execute(
            "SELECT isbn, book_title, book_author, Image_URL_L, price FROM books_data ORDER BY Year_of_Publication LIMIT 30"
        )
    else:
        return redirect(url_for("shop"))

    books = cursor.fetchall()

    if "loggedin" in session:
        books = isInWishlist(cursor, session["id"], books)

    cursor.close()
    conn.close()
    
    return render_template(
        "shop.html", books=books, category=category, total_pages=1, page=1
    )


# Product page
@app.route("/shop/<isbn>")
def productpage(isbn):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT isbn, book_title, book_author, ratings, num_ratings, price, Image_URL_L, year_of_publication, publisher FROM books_data WHERE isbn = %s",
        [isbn],
    )
    book = cursor.fetchone()

    try:
        description = get_book_description(isbn)
    except ConnectionError:
        app.logger.error("Failed to connect to Google API.")
        return render_template("500.html"), 500

    wishlist = {}
    if "loggedin" in session:
        cursor.execute(
            "SELECT isbn FROM wishlist where isbn=%s and user_id=%s",
            (isbn, session["id"]),
        )
        # Fetch one record and return result
        wishlist = cursor.fetchone()

    more = get_recommendations(cursor, book)

    cursor.close()
    conn.close()
    
    return render_template(
        "productpage.html",
        book=book,
        wishlist=wishlist,
        more=more,
        description=description,
    )


# Wishlist page
@app.route("/wishlist")
@is_logged_in
def wishlist():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "select * from wishlist natural left outer join books_data where user_id=%s",
        [session["id"]],
    )
    wishlist_books = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template("wishlist.html", wishlist_books=wishlist_books)


# Add book to the wishlist
@app.route("/addtowishlist", methods=["POST"])
@is_logged_in
def addtowishlist():
    isbn = request.form["isbn"]
    if isbn and request.method == "POST":
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT isbn FROM books_data where isbn=%s", [isbn])
        # Fetch one record and return result
        book = cursor.fetchone()

        cursor.execute(
            "SELECT isbn FROM wishlist where isbn=%s and user_id=%s",
            (isbn, session["id"]),
        )
        # Fetch one record and return result
        wishlist_book = cursor.fetchone()

        if wishlist_book:
            pass
        else:
            cursor.execute(
                "INSERT INTO wishlist VALUES (%s, %s)", ((session["id"]), isbn)
            )
            conn.commit()
            flash("Added to wishlist", "success")

    cursor.close()
    conn.close()
    
    return redirect(request.referrer or url_for("wishlist"))


# Delete book from the wishlist
@app.route("/deletefromwishlist", methods=["POST"])
def deletefromwishlist():
    isbn = request.form["isbn"]
    if isbn and request.method == "POST":
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "delete from wishlist where isbn=%s and user_id=%s", (isbn, session["id"])
        )
        conn.commit()
        cursor.close()
        conn.close()

        flash("Removed from wishlist", "success")
        return redirect(request.referrer or url_for("wishlist"))


@app.route("/cart")
@is_logged_in
def cart():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "select * from cart natural left outer join books_data where user_id=%s",
        [session["id"]],
    )
    cart_books = cursor.fetchall()
    cursor.close()
    conn.close()
    
    cart_total = sum(item["price"] * item["book_count"] for item in cart_books)

    return render_template("cart.html", cart_books=cart_books, cart_total=cart_total)


@app.route("/cart/update", methods=["POST"])
@is_logged_in
def update_cart():
    action = request.form.get("action")
    isbn = request.form.get("isbn")
    quantity = int(request.form.get("quantity", 1))
    user_id = session["id"]

    conn = get_db_connection()
    cursor = conn.cursor()

    if action == "add":
        cursor.execute(
            "SELECT isbn FROM cart WHERE isbn = %s AND user_id = %s", (isbn, user_id)
        )
        cart_book = cursor.fetchone()
        if cart_book:
            cursor.execute(
                "UPDATE cart SET book_count = book_count + %s WHERE isbn = %s AND user_id = %s",
                (quantity, isbn, user_id),
            )
        else:
            cursor.execute("SELECT price FROM books_data WHERE isbn = %s", (isbn,))
            book = cursor.fetchone()
            cursor.execute(
                "INSERT INTO cart (user_id, isbn, book_count, price) VALUES (%s, %s, %s, %s)",
                (user_id, isbn, quantity, book["price"]),
            )
        flash("Added to cart", "success")

    elif action == "increment":
        cursor.execute(
            "UPDATE cart SET book_count = book_count + 1 WHERE isbn = %s AND user_id = %s",
            (isbn, user_id),
        )

    elif action == "decrement":
        cursor.execute(
            "SELECT book_count FROM cart WHERE isbn = %s AND user_id = %s",
            (isbn, user_id),
        )
        cart_book = cursor.fetchone()
        if cart_book and cart_book["book_count"] > 1:
            cursor.execute(
                "UPDATE cart SET book_count = book_count - 1 WHERE isbn = %s AND user_id = %s",
                (isbn, user_id),
            )
        else:
            cursor.execute(
                "DELETE FROM cart WHERE isbn = %s AND user_id = %s", (isbn, user_id)
            )

    elif action == "set":
        cursor.execute(
            "UPDATE cart SET book_count = %s WHERE isbn = %s AND user_id = %s",
            (quantity, isbn, user_id),
        )

    elif action == "delete":
        cursor.execute(
            "DELETE FROM cart WHERE isbn = %s AND user_id = %s", (isbn, user_id)
        )
        flash("Removed from cart", "success")

    conn.commit()
    cursor.close()
    conn.close()
    
    return redirect(request.referrer or url_for('cart'))


# checkout page
@app.route("/checkout", methods=["GET", "POST"])
@is_logged_in
def checkout():
    user_id = session["id"]

    # Fetch existing addresses
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM addresses WHERE user_id = %s", [user_id])
    addresses = cursor.fetchall()

    # Fetch cart items
    cursor.execute(
        "select isbn, Book_Title, price, book_count from cart natural left outer join books_data where user_id=%s",
        [session["id"]],
    )
    cart_items = cursor.fetchall()

    # Calculate total price
    total_price = sum(item["price"] * item["book_count"] for item in cart_items)

    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        address_id = request.form.get("address_id")
        payment_method = request.form.get("payment_method")

        # Insert into orders table
        cursor.execute(
            """
            INSERT INTO orders (user_id, name, phone, address_id, total_amount, order_date)
            VALUES (%s, %s, %s, %s, %s, NOW())
            """,
            [user_id, name, phone, address_id, total_price],
        )
        order_id = cursor.lastrowid

        # Insert order items
        for item in cart_items:
            cursor.execute(
                """
                INSERT INTO order_items (order_id, isbn, quantity, price)
                VALUES (%s, %s, %s, %s)
                """,
                [order_id, item["isbn"], item["book_count"], item["price"]],
            )

        # Insert into payments table
        cursor.execute(
            """
            INSERT INTO payments (order_id, payment_date, amount, payment_method, status)
            VALUES (%s, NOW(), %s, %s, %s)
            """,
            [order_id, total_price, payment_method, "completed"],
        )

        # Clear the cart
        cursor.execute("DELETE FROM Cart WHERE user_id = %s", [user_id])

        conn.commit()
        cursor.close()
        conn.close()
        
        return redirect(url_for("order_confirmation", order_id=order_id))

    return render_template(
        "checkout.html",
        addresses=addresses,
        cart_items=cart_items,
        total_price=total_price,
    )


@app.route("/order_confirmation/<int:order_id>")
@is_logged_in
def order_confirmation(order_id):
    # Fetch order details for confirmation page
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders WHERE order_id = %s", [order_id])
    order = cursor.fetchone()

    cursor.execute(
        "select * from order_items natural left outer join books_data where order_id=%s",
        [order_id],
    )
    order_items = cursor.fetchall()

    cursor.execute("SELECT * FROM payments WHERE order_id = %s", [order_id])
    payment = cursor.fetchone()

    cursor.execute(
        "SELECT * FROM addresses WHERE address_id = %s", [order["address_id"]]
    )
    address = cursor.fetchone()

    cursor.close()
    conn.close()
    
    return render_template(
        "order_confirmation.html",
        order=order,
        order_items=order_items,
        payment=payment,
        address=address,
    )


@app.route("/save_address", methods=["POST"])
@is_logged_in
def save_address():
    user_id = session["id"]
    address_id = request.form.get("address_id")
    street = request.form.get("street")
    city = request.form.get("city")
    state = request.form.get("state")
    country = request.form.get("country")
    pincode = request.form.get("pincode")
    is_default = request.form.get("is_default") == "on"

    conn = get_db_connection()
    cursor = conn.cursor()

    if is_default:
        cursor.execute(
            "UPDATE addresses SET is_primary = 0 WHERE user_id = %s", [user_id]
        )

    if address_id:  # Update existing address
        cursor.execute(
            """
            UPDATE addresses
            SET street=%s, city=%s, state=%s, country=%s, pincode=%s, is_primary=%s
            WHERE address_id=%s AND user_id=%s
            """,
            (street, city, state, country, pincode, is_default, address_id, user_id),
        )
    else:
        cursor.execute(
            """
            INSERT INTO addresses (user_id, street, city, state, country, pincode, is_primary)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (user_id, street, city, state, country, pincode, is_default),
        )

    conn.commit()
    cursor.close()
    conn.close()

    return redirect(request.referrer or url_for("profile", tab="saved-addresses"))


@app.route("/delete_address", methods=["POST"])
@is_logged_in
def delete_address():
    user_id = session["id"]
    address_id = request.form.get("address_id")

    conn = get_db_connection()
    cursor = conn.cursor()

    if address_id:
        cursor.execute(
            "UPDATE addresses SET is_deleted=TRUE WHERE address_id=%s AND user_id=%s",
            (address_id, user_id),
        )

    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for("profile", tab="saved-addresses"))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500


@app.route("/no_internet")
def no_internet():
    return render_template("no_internet.html")

