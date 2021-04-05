# Book Review App

BookReviewApp is a small prototype cloud application developed to apply and extend the techniques and technologies learned as part of ECS781P-Cloud Computing at Queen Mary Univsersity of London.

BookReviewApp is a Flask application hosted on Amazon Web Services. The user can register with the application to maintain a list of book reviews. The application used Open Library's REST API to fetch book details. As per the guidelines, we have focussed on below areas in the development phase.

* REST based service interface for CRUD operations.
* Interaction with external REST services.
* Using an external cloud database.
* Serving the application over https.
* Implementing hash-based authentication.
* Implementing user accounts and access management.


# Features

* User can login or sign up if new user.
* View all the book reviews when logged in.
* Add more book reviews to your account.
* Search OpenLibrary's books database to add book and it's review.
* Update existing book reviews in your account.
* Delete existing book reviews in your account.
* Change account details.

# Directory structure

The project directory structure is as shown below.

```text
BookReviewApp/
├── run.py
├── README.md
├── bookreview
|   ├── __init__.py
|   ├── config.py
|   ├── models.py
|   ├── errors/
│   |    ├── __init__.py
│   |    └── handlers.py
|   ├── main/
│   |   ├── __init__.py
|   |   └── routes.py
|   ├── readinglist/
|   |   ├── __init__.py
|   |   └── routes.py
|   ├── static/
|   |   └── main.css
|   ├── templates/
|   |   ├── account.html
|   |   ├── addbook.html
|   |   ├── alist.html
|   |   ├── booklist.html
|   |   ├── create_list.html
|   |   ├── layout.html
|   |   ├── login.html
|   |   ├── register.html
|   |   └── searchbook.html
└── └── users/
    |   ├── __init__.py
    |   ├── forms.py
    └── └── routes.py
```


# Design

## Application
The application is developed using Flask web framework and other flask extensions as listed under External tools section.
- Flask-RESTful is an extension for Flask that adds support for quickly building REST APIs. It is a lightweight abstraction that works with major existing ORM/libraries. Flask-RESTful encourages best practices with minimal setup.
- Flask-Bcrypt is a Flask extension that provides bcrypt hashing utilities for applications.
- Flask-WTF is a simple integration of Flask and WTForms.
- Flask-Login provides user session management for Flask. It handles the common tasks of logging in, logging out, and remembering users’ sessions over extended periods of time.
- Flask-SQLAlchemy is an extension for Flask that adds support for SQLAlchemy to the application. It aims to simplify using SQLAlchemy with Flask by providing useful defaults and extra helpers that make it easier to accomplish common tasks. SQLAlchemy is an open-source SQL toolkit and object-relational mapper for Python.

## Database
The application connects to AWS RDS instance which hosts MySQL database. The instance details are covered in the explaination video.

## Platform
The application is deployed on AWS EC2 instance which hosts Ubuntu Server 18.04 (Bionic) with Public IPv4 54.205.252.26.
The application runs on port 5000.

## External tools
* flask
* flask-restful
* flask-bcrypt
* flask-wtf
* flask-login
* flask-SQLAlchemy
* email-validator
* AWS
* MySQL


## HTTP REST API

| Endpoint               | Methods   | Action                   | Use                                 |
| -------------------    |:---------:|:------------------------:| -----------------------------------:|
| /                      | GET, POST | home()                   | Home page of the application.       |
| /register              | GET, POST | register()               | New user signs up.                  |
| /login                 | GET, POST | login()                  | Existing user logs in.              |
| /logout                |           | logout()                 | Current user logs out.              |
| /account               | GET, POST | account()                | View user account details.          |
| /list                  | GET, POST | home()                   | View existing list of book reviews. |
| /list/new              | GET, POST | new_list()               | Create new book review.             |
| /book/bookid           | GET, POST | alist()                  |                                     |
| /book/bookid/update    | GET, POST | update_list(list id)     | Update book review by book id.      |
| /book/bookid/delete    | POST      | delete_list(list id)     | Delete book review by book id.      |
| /book/bookid/add       | GET, POST | addbook(list id)         | Add book review by book id.         |
| /book/bookname/search  | GET, POST | booknamesearch(bookname) | Search book by book name.           |
| /book/list/search      | GET, POST | searchbook()             |                                     |


# Contributors
The application was jointly developed by below team members.
* Abhinav Gyani
* Mekie Sied Alabo
* Ropan Bhattacharya
* Simon Michael Hart
* Vineet Ranjan
