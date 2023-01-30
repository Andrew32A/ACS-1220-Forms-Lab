from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.validators import DataRequired, Length, ValidationError
from books_app.models import Audience, Book, Author, Genre

class BookForm(FlaskForm):
    """Form to create a book."""
    title = StringField('Book Title', 
        validators=[
            DataRequired(), 
            Length(min=3, max=80, message="Your message needs to be betweeen 3 and 80 chars")
        ])
    publish_date = DateField('Date Published', validators=[DataRequired()])
    author = QuerySelectField('Author', query_factory=lambda: Author.query, allow_blank=False)
    audience = SelectField('Audience', choices=Audience.choices())
    genres = QuerySelectMultipleField('Genres', query_factory=lambda: Genre.query)
    submit = SubmitField('Submit')

    def validate_title(form, field):
        if 'banana' in field.data:
            raise ValidationError('Title cannot contain the word banana')


class AuthorForm(FlaskForm):
    """Form to create an author."""

    # TODO: Fill out the fields in this class for:
    # - the author's name
    # - the author's biography (hint: use a TextAreaField)
    # - a submit button

    # name = StringField("Author's name",
    #     validators = [
    #         DataRequired()
    #         Length(min=1, max=80, message="Your name needs to be between 1 and 80 characters")
    #     ])
    # biography = 

    """Form to create a book."""
    author_name = StringField("Author's name", 
        validators=[
            DataRequired(), 
            Length(min=1, max=80, message="Your message needs to be betweeen 1 and 80 characters")
        ])
    author_biography = StringField("Author's Biography", 
        validators=[
            DataRequired(), 
            Length(min=1, max=200, message="Your message needs to be betweeen 1 and 200 characters")
        ])
    submit = SubmitField('Submit')

    def validate_title(form, field):
        if 'banana' in field.data:
            raise ValidationError('Title cannot contain the word banana')

    # STRETCH CHALLENGE: Add more fields here as well as in `models.py` to
    # collect more information about the author, such as their birth date,
    # country, etc.

class GenreForm(FlaskForm):
    """Form to create a genre."""
    # TODO: Fill out the fields in this class for:
    # - the genre's name (e.g. fiction, non-fiction, etc)
    # - a submit button

    genre_name = SelectField('Genre', choices=Genre.name.choices()) # maybe get rid of .name
    submit = SubmitField('Submit')