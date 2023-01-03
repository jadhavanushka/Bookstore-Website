from flask import Flask
from flask import render_template
from flask import request, Flask, redirect, url_for, request, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

app.secret_key = 'your secret key'

# Enter your database connection details below
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'MySQLServer8.0.29'
app.config['MYSQL_DB'] = 'bookstore'

# Intialize MySQL
mysql = MySQL(app)


@app.route('/shop')
def shop():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(
        'SELECT isbn, book_title, book_author, Image_URL_L, price FROM books_data order by Year_of_Publication desc limit 20 ')
    # Fetch one record and return result
    books = cursor.fetchall()

    return render_template('shop.html', books=books)


@app.route('/shop/<isbn>')
def productpage(isbn):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT isbn, book_title, book_author, price, Image_URL_L, year_of_publication FROM books_data WHERE isbn = %s',[isbn])
    book = cursor.fetchone()

    wishlist_btn='Add to wishlist'
    if 'loggedin' in session:
        cursor.execute('SELECT isbn FROM wishlist where isbn=%s and user_id=%s', (isbn,session['id']))
                # Fetch one record and return result
        wishlist_book = cursor.fetchone()
        if wishlist_book:
            wishlist_btn='Remove from wishlist'
        else:
            wishlist_btn='Add to wishlist'
            

    cursor.execute(
    'SELECT book_title, book_author, Image_URL_L, price FROM books_data where Year_of_Publication=%s limit 8 ',[book['year_of_publication']])
        # Fetch one record and return result
    more = cursor.fetchall()

    if book:
        if 'loggedin' in session:
            return render_template('productpage1.html', book=book, wishlist_btn=wishlist_btn, more=more)
        else:
            return render_template('productpage.html', book=book, wishlist_btn=wishlist_btn, more=more)


@app.route('/addtocart', methods=['POST'])
def addtocart():
    quantity = int(request.form['quantity'])
    isbn = request.form['isbn']
    if 'loggedin' in session:
    
        if quantity and isbn and request.method == 'POST':
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute(
                'SELECT isbn, book_title, book_author, Image_URL_L, price FROM books_data where isbn=%s', [isbn])
            # Fetch one record and return result
            book = cursor.fetchone()

            cursor.execute('SELECT isbn FROM cart where isbn=%s and user_id=%s', (isbn,session['id']))
            # Fetch one record and return result
            cart_book = cursor.fetchone()
            if cart_book:
                cursor.execute('UPDATE cart set book_count=book_count+%s where isbn=%s and user_id=%s',
                            (quantity,session['id'], isbn))
                mysql.connection.commit()
            else:
                cursor.execute('INSERT INTO cart VALUES (%s, %s, %s)',
                                (session['id'], isbn,  quantity))
                mysql.connection.commit()

        return redirect(url_for('home'))
        # User is not loggedin redirect to login page
    else:
        return redirect(url_for('login'))


@app.route('/addtowishlist', methods=['POST'])
def addtowishlist():
    isbn = request.form['isbn']
    if 'loggedin' in session:
    
        if isbn and request.method == 'POST':
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute(
                'SELECT isbn FROM books_data where isbn=%s', [isbn])
            # Fetch one record and return result
            book = cursor.fetchone()

            cursor.execute('SELECT isbn FROM wishlist where isbn=%s and user_id=%s', (isbn,session['id']))
            # Fetch one record and return result
            cart_book = cursor.fetchone()
            # delete from wishlist if it's already there
            if cart_book:
                cursor.execute('delete from wishlist where isbn=%s and user_id=%s',
                            (session['id'], isbn))
                mysql.connection.commit()
            else:
                cursor.execute('INSERT INTO wishlist VALUES (%s, %s)',
                                (session['id'], isbn))
                mysql.connection.commit()

        return redirect(url_for('home'))
        # User is not loggedin redirect to login page
    else:
        return redirect(url_for('login'))


@app.route('/home')
def home():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(
        'SELECT book_title, book_author, Image_URL_L, price FROM books_data order by Year_of_Publication desc limit 8')
    # Fetch one record and return result
    new = cursor.fetchall()

    cursor.execute(
        'SELECT book_title, book_author, Image_URL_L, price FROM books_data order by ratings desc limit 8')
    # Fetch one record and return result
    featured = cursor.fetchall()

    cursor.execute(
        'SELECT book_title, book_author, Image_URL_L, price FROM books_data order by Year_of_Publication limit 8')
    # Fetch one record and return result
    classic = cursor.fetchall()

    # Check if user is loggedin

    if 'loggedin' in session:
        return render_template('home1.html', new=new, classic=classic, featured=featured)
    else:
        return render_template('home.html', new=new, classic=classic, featured=featured)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        # Create variables for easy access
        email = request.form['email']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT * FROM users WHERE user_email = %s AND user_password = %s', (email, password))
        # Fetch one record and return result
        account = cursor.fetchone()
        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['user_id']
            session['email'] = account['user_email']
            # Redirect to home page
            # return 'Logged in successfully!'
            return redirect(url_for('home'))

        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect email/password. Try again.'

    return render_template('login.html', msg=msg)


@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('email', None)
    # Redirect to login page
    return redirect(url_for('home'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'fname' in request.form and 'lname' in request.form and 'email' in request.form and 'password' in request.form and 'password2' in request.form:
        # Create variables for easy access
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        password = request.form['password']
        password2 = request.form['password2']

        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE user_email = %s', [email])
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not password == password2:
            msg = 'Passwords do not match!'
        elif not email or not password or not password2:
            msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO users VALUES (NULL, %s, %s, %s, %s)',
                           (fname, lname,  email, password))
            mysql.connection.commit()

            # Log in to the account
            cursor.execute(
                'SELECT user_id FROM users WHERE user_email = %s', [email])
            # Fetch one record and return result
            account = cursor.fetchone()
            # If account exists in accounts table in out database
            if account:
                # Create session data, we can access this data in other routes
                session['loggedin'] = True
                session['id'] = account['user_id']
                session['email'] = email
                # Redirect to home page
                return redirect(url_for('home'))

    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('signup.html', msg=msg)


@app.route('/profile')
def profile():
    # Check if user is loggedin
    if 'loggedin' in session:
        # We need all the account info for the user so we can display it on the profile page
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE user_id = %s',
                       (session['id'],))
        account = cursor.fetchone()
        # Show the profile page with account info
        return render_template('profile.html', account=account)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
