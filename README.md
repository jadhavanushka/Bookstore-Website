# Bookstore Website - Book Haven

This full-featured online bookstore website is built using Flask, MySQL, and Bootstrap. It allows users to browse books, add them to their wishlist or cart, and make purchases. The project is deployed on AlwaysData. You can check it out [here](https://bookhaven.alwaysdata.net/)

## Features

- **Browse Books**: Browse through a large collection of books.
- **Search**: Search for books by title or author.
- **Book Details**: See detailed information about a book, including price, author, and ratings.
- **Add to Cart/Wishlist**: Users can add books to their cart or wishlist.
- **Authentication**: User login, registration, and session management.
- **Orders**: Checkout books & place orders.
- **Responsive Design**: Built with Bootstrap to be fully responsive.
- **Error Handling**: Custom error pages for 404, 500, and no internet scenarios.

## Tech Stack

- **Backend**: Flask, MySQL
- **Frontend**: Jinja2 templating, Bootstrap
- **Database & Deployment**: AlwaysData
- **APIs Used**: Google Books API for fetching book descriptions.

## Getting Started

### Prerequisites

- Python 3.8+
- MySQL
- MySQL Workbench or any MySQL client (for local development)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/jadhavanushka/bookstore-website.git
   cd bookstore-website
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your `.env` file with the following variables:
   ```bash
   DB_HOST=your_db_host
   DB_USER=your_db_user
   DB_PASS=your_db_password
   DB_NAME=your_db_name
   SECRET_KEY=your_secret_key
   ```

5. Set up the database:

   Create the database:
      ```bash
      mysql -u your_db_user -p -e "CREATE DATABASE your_db_name;"
      ```

   Import the schema:
      ```bash
      mysql -u your_db_user -p your_db_name < database/schema.sql
      ```

   Import books data:
      ```bash
      mysql -u your_db_user -p your_db_name < database/books_data.sql
      ```

6. Run the development server:
   ```bash
   flask run
   ```