# Bookstore Website - Book Haven

This full-featured online bookstore website is built using Flask, MySQL, and Bootstrap. It allows users to browse books, add them to their wishlist or cart, and make purchases.
The project is deployed on Google Cloud. You can check it out [here](https://abiding-splicer-433313-j2.el.r.appspot.com)

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
- **Database**: Google Cloud SQL (MySQL)
- **Deployment**: Google Cloud App Engine
- **APIs Used**: Google Books API for fetching book descriptions.

## Getting Started

### Prerequisites

- Python 3.8+
- MySQL
- Google Cloud SDK (for deployment)
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
   DB_USER=your_db_user
   DB_PASS=your_db_password
   DB_NAME=your_db_name
   DB_PORT=3306
   INSTANCE_CONNECTION_NAME=your_instance_connection_name
   ```

5. Run the development server:
   ```bash
   flask run
   ```

### Deployment

1. Ensure you have the Google Cloud SDK installed and authenticated.
2. Deploy the app using App Engine:
   ```bash
   gcloud app deploy
   ```
