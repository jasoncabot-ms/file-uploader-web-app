from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired, Email, Length

class UploadForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', [
        Email(message=('Not a valid email address.')),
        DataRequired()])
    body = TextAreaField('Message', [
        DataRequired(),
        Length(min=4, message=('Your message is too short.'))])
    upload = FileField('Data file', validators=[
        FileRequired(),
        FileAllowed(['csv'], 'CSV Files Only')
    ])    
    submit = SubmitField('Submit')
