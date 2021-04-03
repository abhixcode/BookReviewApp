from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from bookreview.models import User
from flask_login import login_user, current_user


class ListForm(FlaskForm):
    bookname = StringField('Book Name', validators=[DataRequired()])
    review = StringField('Review', validators=[DataRequired()])
    isbn = StringField('ISBN', validators=[DataRequired()])
    libraryid = StringField('Library Id', validators=[DataRequired()])
    #author = StringField('Author', validators=[DataRequired()])
    #search = SubmitField('search')
    submit = SubmitField('Add Review')
    search = SubmitField('Search Book')

class SearchnaddForm(FlaskForm):
    bookname = StringField('Book Name', validators=[DataRequired()])
    review = StringField('Review', validators=[DataRequired()])
    isbn = StringField('ISBN', validators=[DataRequired()])
    libraryid = StringField('Library Id', validators=[DataRequired()])
    #author = StringField('Author', validators=[DataRequired()])
    #search = SubmitField('search')
    submit = SubmitField('Add Review')

class SearchForm(FlaskForm):
    bookname = StringField('Book Name', validators=[DataRequired()])
    #author = StringField('Author', validators=[DataRequired()])
    #search = SubmitField('search')
    submit = SubmitField('Search Book')