from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from bookreview.models import User
from flask_login import login_user, current_user

# Form to add review
class ListForm(FlaskForm):
    bookname = StringField('Book Name', validators=[DataRequired()])
    review = StringField('Review', validators=[DataRequired()])
    isbn = StringField('ISBN', validators=[DataRequired()])
    libraryid = StringField('Library Id', validators=[DataRequired()])
    submit = SubmitField('Add Review')
    search = SubmitField('Search Book')

# Form to add a new book review after searching from external API
class SearchnaddForm(FlaskForm):
    bookname = StringField('Book Name', validators=[DataRequired()])
    review = StringField('Review', validators=[DataRequired()])
    isbn = StringField('ISBN', validators=[DataRequired()])
    libraryid = StringField('Library Id', validators=[DataRequired()])
    submit = SubmitField('Add Review')

# Form to search a book from external API
class SearchForm(FlaskForm):
    bookname = StringField('Book Name', validators=[DataRequired()])
    submit = SubmitField('Search Book')