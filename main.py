from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_mysqldb import MySQL
from functools import wraps
import MySQLdb.cursors
import re
from utils import get_book_description, get_recommendations

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
    # We need all the account info for the user so we can display it on the profile page
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM users WHERE user_id = %s", (session["id"],))
    account = cursor.fetchone()
    # Show the profile page with account info
    return render_template("profile.html", account=account)


# Shop page
@app.route("/shop")
def shop():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(
        "SELECT isbn, book_title, book_author, Image_URL_L, price FROM books_data order by Year_of_Publication desc limit 30"
    )

    books = cursor.fetchall()

    if "loggedin" in session:
        cursor.execute(
            "select isbn from wishlist natural left outer join books_data where user_id=%s",
            [session["id"]],
        )
        wishlist = cursor.fetchall()
        if wishlist:
            for book in books:
                if book["isbn"] in wishlist:
                    book["wish"] = True
                else:
                    book["wish"] = False

    return render_template("shop.html", books=books)


# Filter books by price
@app.route("/shop/filterbyprice", methods=["POST"])
def filterbyprice():
    FilterPrice = int(request.form["FilterPrice"])
    if FilterPrice and request.method == "POST":
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            "SELECT isbn, book_title, book_author, Image_URL_L, price FROM books_data where price<=%s order by Year_of_Publication desc limit 30 ",
            [FilterPrice],
        )
        books = cursor.fetchall()

    return render_template("shop.html", books=books)


# Filter books by rating
@app.route("/shop/filterbyrating", methods=["POST"])
def filterbyrating():
    rating = int(request.form["rating"])
    if rating and request.method == "POST":
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            "SELECT isbn, book_title, book_author, Image_URL_L, price FROM books_data where ratings>=%s order by Year_of_Publication desc limit 30 ",
            [rating],
        )
        books = cursor.fetchall()

    return render_template("shop.html", books=books)


# Search a book
@app.route("/shop/search", methods=["POST"])
def search():
    searchbook = request.form["searchbook"]
    if searchbook and request.method == "POST":
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            "SELECT isbn, book_title, book_author, Image_URL_L, price FROM books_data where Book_Title like %s or Book_Author like %s order by Year_of_Publication desc limit 30 ",
            ("%" + searchbook + "%", "%" + searchbook + "%"),
        )
        books = cursor.fetchall()
        return render_template("shop.html", books=books)


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

    more = get_recommendations(cursor,book)

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
    # Fetch one record and return result
    cart_books = cursor.fetchall()

    cursor.execute(
        "select sum(price*book_count)as cart_total from cart natural left outer join books_data where user_id=%s",
        [session["id"]],
    )
    cart_total = cursor.fetchone()
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
            "select sum(book_count) as stock from stock where isbn=%s", [isbn]
        )
        # Fetch one record and return result
        stock = cursor.fetchone()
        stock = stock["stock"]

        # if stock > cart_book["book_count"] + 1:
        if stock or not stock:
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
            "select sum(book_count) as stock from stock where isbn=%s", [isbn]
        )
        # Fetch one record and return result
        stock = cursor.fetchone()
        stock = stock["stock"]

        if stock > int(quantity):

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


@app.route("/payment", methods=["POST", "GET"])
@is_logged_in
def payment():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(
        "select * from cart natural left outer join books_data where user_id=%s",
        [session["id"]],
    )
    # Fetch one record and return result
    cart_books = cursor.fetchall()
    total_items = len(cart_books)

    cursor.execute(
        "select sum(price*book_count)as cart_total from cart natural left outer join books_data where user_id=%s",
        [session["id"]],
    )
    cart_total = cursor.fetchone()

    cursor.execute(
        "select sum(price*book_count)as cart_total from cart natural left outer join books_data where user_id=%s",
        [session["id"]],
    )
    cart_total = cursor.fetchone()
    cart_total = cart_total["cart_total"]

    if (
        request.method == "POST"
        and "fname" in request.form
        and "lname" in request.form
        and "phone" in request.form
    ):  # and 'address' in request.form and 'city' in request.form and 'zip' in request.form and 'paymentmethod' in request.form:
        # Create variables for easy access
        fname = request.form["fname"]
        lname = request.form["lname"]
        phone = int(request.form["phone"])
        # address = request.form['address']
        # city = request.form['city']
        # zip = int(request.form['zip'])
        # payment_method = request.form['paymentMethod']

        # cursor.execute('INSERT INTO orders VALUES (NULL, %s, %s, %s, %s,%s, %s, %s, %s,%s )',
        #                (session[id], fname, lname, phone, address, city, zip, payment_method, cart_total))
        # mysql.connection.commit()

        cursor.execute("DELETE FROM cart where user_id=%s", [session["id"]])
        mysql.connection.commit()

        return render_template("orderplaced.html")

    return render_template(
        "paymentpage.html",
        total_items=total_items,
        cart_books=cart_books,
        cart_total=cart_total,
    )


if __name__ == "__main__":
    app.run(debug=True)
