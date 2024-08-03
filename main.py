from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_mysqldb import MySQL
from functools import wraps
import MySQLdb.cursors
import re
from utils import (
    get_book_description,
    get_recommendations,
    get_books_query,
    isInWishlist,
)

app = Flask(__name__)

app.secret_key = "your secret key"

# Enter your database connection details below
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "MySQLServer8.0.29"
app.config["MYSQL_DB"] = "bookstore"

# Intialize MySQL
mysql = MySQL(app)


# Home page
@app.route("/")
def home():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(
        "SELECT isbn, book_title, book_author, Image_URL_L, price FROM books_data order by Year_of_Publication desc limit 8"
    )
    new = cursor.fetchall()

    cursor.execute(
        "SELECT isbn, book_title, book_author, Image_URL_L, price FROM books_data order by ratings desc, Year_of_Publication desc limit 8"
    )
    featured = cursor.fetchall()

    cursor.execute(
        "SELECT isbn, book_title, book_author, Image_URL_L, price FROM books_data order by Year_of_Publication limit 8"
    )
    classic = cursor.fetchall()

    if "loggedin" in session:
        new = isInWishlist(cursor, session["id"], new)
        featured = isInWishlist(cursor, session["id"], featured)
        classic = isInWishlist(cursor, session["id"], classic)

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
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
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
            cursor.execute(
                "INSERT INTO users VALUES (NULL, %s, %s, %s, %s)",
                (fname, lname, email, password),
            )
            mysql.connection.commit()

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

    elif request.method == "POST":
        # Form is empty... (no POST data)
        msg = "Please fill all the fields"

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
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM users WHERE user_email = %s", [email])
        # Fetch one record and return result
        account = cursor.fetchone()

        # If account exists in users table in out database
        if account:
            if account["user_password"] == password:
                # Create session data, we can access this data in other routes
                session["loggedin"] = True
                session["id"] = account["user_id"]
                session["email"] = account["user_email"]

                flash("Logged in.", "success")

                # Redirect to home page
                return redirect(url_for("home"))

            else:
                msg = "Incorrect password"
                return render_template("login.html", msg=msg)

        else:
            # Account doesnt exist email is incorrect
            msg = "Cannot find the account. Incorrect email"

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

    flash("Logged out.", "success")

    # Redirect to login page
    return redirect(url_for("home"))


# profile page
@app.route("/profile")
@is_logged_in
def profile():
    user_id = session["id"]
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM users WHERE user_id = %s", [user_id])
    user = cursor.fetchone()

    cursor.execute("SELECT * FROM orders WHERE user_id = %s", [user_id])
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

    cursor.execute("SELECT * FROM Addresses WHERE user_id = %s", [user_id])
    addresses = cursor.fetchall()

    return render_template(
        "profile.html", user=user, orders=orders, wishlist=wishlist, addresses=addresses
    )


@app.route("/edit_profile", methods=["POST"])
@is_logged_in
def edit_profile():
    user_id = session["id"]
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    fname = request.form.get("fname")
    lname = request.form.get("lname")
    email = request.form.get("email")
    phone = request.form.get("phone")

    cursor.execute(
        "UPDATE users SET first_name = %s, last_name = %s, user_email = %s, phone = %s WHERE user_id = %s",
        (fname, lname, email, phone, user_id),
    )
    mysql.connection.commit()
    cursor.close()

    return redirect(url_for("profile", tab='profile-info'))


# change password
@app.route("/change_password", methods=["POST"])
def change_password():
    current_password = request.form["current_password"]
    new_password = request.form["new_password"]
    confirm = request.form["confirm"]
    user_id = session["id"]

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT user_password FROM users WHERE user_id = %s", [user_id])
    user = cursor.fetchone()

    if user["user_password"] == current_password:
        if new_password == confirm:
            # Update password
            cursor.execute(
                "UPDATE users SET user_password=%s WHERE user_id = %s",
                (new_password, user_id),
            )
            mysql.connection.commit()
            flash("Password changed successfully", "success")
        else:
            flash("Passwords do not match", "danger")
    else:
        flash("Incorrect current password", "danger")

    cursor.close()
    return redirect(url_for("profile", tab='change-password'))



# Shop page
@app.route("/shop")
def shop():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

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


# Product page
@app.route("/shop/<isbn>")
def productpage(isbn):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(
        "SELECT isbn, book_title, book_author, ratings, num_ratings, price, Image_URL_L, year_of_publication, publisher FROM books_data WHERE isbn = %s",
        [isbn],
    )
    book = cursor.fetchone()

    description = get_book_description(isbn)

    wishlist = {}
    if "loggedin" in session:
        cursor.execute(
            "SELECT isbn FROM wishlist where isbn=%s and user_id=%s",
            (isbn, session["id"]),
        )
        # Fetch one record and return result
        wishlist = cursor.fetchone()

    more = get_recommendations(cursor, book)

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
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(
        "select * from wishlist natural left outer join books_data where user_id=%s",
        [session["id"]],
    )
    wishlist_books = cursor.fetchall()

    return render_template("wishlist.html", wishlist_books=wishlist_books)


# Add book to the wishlist
@app.route("/addtowishlist", methods=["POST"])
@is_logged_in
def addtowishlist():
    isbn = request.form["isbn"]
    if isbn and request.method == "POST":
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
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
            mysql.connection.commit()
    return redirect(url_for("shop"))


# Delete book from the wishlist
@app.route("/deletefromwishlist", methods=["POST"])
def deletefromwishlist():
    isbn = request.form["isbn"]
    if isbn and request.method == "POST":
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            "delete from wishlist where isbn=%s and user_id=%s", (isbn, session["id"])
        )
        mysql.connection.commit()
        return redirect(url_for("wishlist"))


@app.route("/addtocart", methods=["POST"])
@is_logged_in
def addtocart():
    quantity = int(request.form["quantity"])
    isbn = request.form["isbn"]

    if quantity and isbn and request.method == "POST":
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            "SELECT isbn, book_title, book_author, Image_URL_L, price FROM books_data where isbn=%s",
            [isbn],
        )
        # Fetch one record and return result
        book = cursor.fetchone()
        cursor.execute(
            "SELECT isbn FROM cart where isbn=%s and user_id=%s",
            (isbn, session["id"]),
        )
        # Fetch one record and return result
        cart_book = cursor.fetchone()
        if cart_book:
            cursor.execute(
                "UPDATE cart set book_count=book_count+%s where isbn=%s and user_id=%s",
                (quantity, isbn, session["id"]),
            )
            mysql.connection.commit()
        else:
            cursor.execute(
                "INSERT INTO cart VALUES (%s, %s, %s, %s)",
                (session["id"], isbn, quantity, book["price"]),
            )
            mysql.connection.commit()
    return redirect(url_for("shop"))


@app.route("/cart")
@is_logged_in
def cart():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(
        "select * from cart natural left outer join books_data where user_id=%s",
        [session["id"]],
    )
    cart_books = cursor.fetchall()

    cart_total = sum(item["price"] * item["book_count"] for item in cart_books)

    return render_template("cart.html", cart_books=cart_books, cart_total=cart_total)


@app.route("/inc_quantity", methods=["POST"])
def inc_quantity():
    isbn = request.form["isbn"]

    if isbn and request.method == "POST":
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            "SELECT book_count FROM cart where isbn=%s and user_id=%s",
            (isbn, session["id"]),
        )
        # Fetch one record and return result
        cart_book = cursor.fetchone()

        cursor.execute(
            "UPDATE cart set book_count=book_count+1 where isbn=%s and user_id=%s",
            (isbn, session["id"]),
        )
        mysql.connection.commit()

    return redirect(url_for("cart"))


@app.route("/dec_quantity", methods=["POST"])
def dec_quantity():
    isbn = request.form["isbn"]

    if isbn and request.method == "POST":

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            "SELECT book_count FROM cart where isbn=%s and user_id=%s",
            (isbn, session["id"]),
        )
        # Fetch one record and return result
        cart_book = cursor.fetchone()

        if cart_book["book_count"] == 1:
            cursor.execute(
                "delete from cart where isbn=%s and user_id=%s", (isbn, session["id"])
            )
            mysql.connection.commit()

        else:
            cursor.execute(
                "UPDATE cart set book_count=book_count-1 where isbn=%s and user_id=%s",
                (isbn, session["id"]),
            )
            mysql.connection.commit()

    return redirect(url_for("cart"))


@app.route("/set_quantity", methods=["POST"])
def set_quantity():
    quantity = request.form["quantity"]
    isbn = request.form["isbn"]

    if isbn and request.method == "POST":
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            "SELECT book_count FROM cart where isbn=%s and user_id=%s",
            (isbn, session["id"]),
        )
        # Fetch one record and return result
        cart_book = cursor.fetchone()

        cursor.execute(
            "UPDATE cart set book_count=%s where isbn=%s and user_id=%s",
            (quantity, isbn, session["id"]),
        )
        mysql.connection.commit()

    return redirect(url_for("cart"))


@app.route("/deletefromcart", methods=["POST"])
def deletefromcart():
    isbn = request.form["isbn"]
    if isbn and request.method == "POST":
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            "delete from cart where isbn=%s and user_id=%s", (isbn, session["id"])
        )
        mysql.connection.commit()
        return redirect(url_for("cart"))


# checkout page
@app.route("/checkout", methods=["GET", "POST"])
@is_logged_in
def checkout():
    user_id = session["id"]

    # Fetch existing addresses
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM Addresses WHERE user_id = %s", [user_id])
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

        # Insert into Orders table
        cursor.execute(
            """
            INSERT INTO Orders (user_id, name, phone, address_id, total_amount, order_date)
            VALUES (%s, %s, %s, %s, %s, NOW())
            """,
            [user_id, name, phone, address_id, total_price],
        )
        order_id = cursor.lastrowid

        # Insert order items
        for item in cart_items:
            cursor.execute(
                """
                INSERT INTO Order_Items (order_id, isbn, quantity, price)
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

        mysql.connection.commit()
        cursor.close()
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
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM Orders WHERE order_id = %s", [order_id])
    order = cursor.fetchone()
    
    cursor.execute(
        "select * from Order_Items natural left outer join books_data where order_id=%s",
        [order_id],
    )
    order_items = cursor.fetchall()
    
    cursor.execute("SELECT * FROM Payments WHERE order_id = %s", [order_id])
    payment = cursor.fetchone()
    
    cursor.execute("SELECT * FROM Addresses WHERE address_id = %s", [order['address_id']])
    address = cursor.fetchone()
    
    cursor.close()

    return render_template(
        "order_confirmation.html", order=order, order_items=order_items, payment=payment, address=address
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

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    if is_default:
        cursor.execute(
            "UPDATE addresses SET is_primary = 0 WHERE user_id = %s", [user_id]
        )

    if address_id:  # Update existing address
        cursor.execute(
            """
            UPDATE Addresses
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

    mysql.connection.commit()
    cursor.close()

    return redirect(url_for("profile", tab='saved-addresses'))


@app.route("/delete_address", methods=["POST"])
@is_logged_in
def delete_address():
    user_id = session["id"]
    address_id = request.form.get("address_id")

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    if address_id:
        cursor.execute(
            "UPDATE Addresses SET is_deleted=TRUE WHERE address_id=%s AND user_id=%s",
            (address_id, user_id),
        )

    mysql.connection.commit()
    cursor.close()

    return redirect(url_for("profile", tab='saved-addresses'))


if __name__ == "__main__":
    app.run(debug=True)
