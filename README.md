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

application features

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

Flask, DB, Cloud

External tools required for the setup:
* flask
* flask-restful
* flask-bcrypt
* flask-wtf
* flask-login
* flask-SQLAlchemy
* email-validator
* AWS
* MySQL


# HTTP REST API

| Endpoint               | Methods   | Action                   | Use                      |
| -------------------    |:---------:|:------------------------:| ------------------------:|
| /                      | GET, POST | home()                   |                          |
| /register              | GET, POST | register()               |                          |
| /login                 | GET, POST | login()                  |                          |
| /logout                |           | logout()                 |                          |
| /account               | GET, POST | account()                |                          |
| /list                  | GET, POST | home()                   |                          |
| /list/new              | GET, POST | new_list()               |                          |
| /book/bookid           | GET, POST | alist()                  |                          |
| /book/bookid/update    | GET, POST | update_list(list id)     |                          |
| /book/bookid/delete    | POST      | delete_list(list id)     |                          |
| /book/bookid/add       | GET, POST | addbook(list id)         |                          |
| /book/bookname/search  | GET, POST | booknamesearch(bookname) |                          |
| /book/list/search      | GET, POST | searchbook()             |                          |


# Contributors
The application was jointly developed by below team members.
* Abhinav Gyani
* Mekie Sied Alabo
* Ropan Bhattacharya
* Simon Michael Hart
* Vineet Ranjan
