Bookstore Project
Overview
This is a simple Bookstore Web Application built using Django (Python framework). It allows users to search, view, and manage books, including details like title, author, and genre. The project includes features for user authentication (sign up, log in, password reset) and book search functionality based on author_name, genre, and title.

Features
User Authentication: Users can create accounts, log in, and reset passwords.

Search Functionality: Users can search for books by author, genre, or title.

Book Management: Admin users can manage (add, edit, delete) books.

Responsive Design: The application is responsive and works well on desktop and mobile devices.

Technologies Used
Backend: Django (Python Web Framework)

Frontend: HTML, CSS (with Bootstrap for responsive design)

Database: SQLite (Default in Django, can be switched to PostgreSQL, MySQL, etc.)

Email: For password reset functionality (configured via SMTP)

Version Control: Git (for source code management)

Requirements
Python 3.x

Django 3.x or higher

SQLite (or any other database you configure)

Installation
1. Clone the repository
bash
Copy
git clone https://github.com/yourusername/bookstore-project.git
cd bookstore-project
2. Set up a virtual environment (optional but recommended)
bash
Copy
python3 -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
3. Install the required packages
bash
Copy
pip install -r requirements.txt
4. Set up the database
bash
Copy
python manage.py migrate
5. Create a superuser to access the Django admin
bash
Copy
python manage.py createsuperuser
6. Run the development server
bash
Copy
python manage.py runserver
Now, you can access the application in your browser at http://127.0.0.1:8000/.

Usage
Homepage: Displays a list of available books.

Search Bar: On the homepage or in the search page, you can search for books by author_name, genre, or title.

User Authentication: Users can sign up, log in, and reset passwords (through email verification).

Admin Dashboard: The admin can log in to add, update, or delete books through the Django admin panel at http://127.0.0.1:8000/admin/.
