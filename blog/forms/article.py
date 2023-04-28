from wtforms import StringField, validators, SubmitField, TextAreaField
from flask_wtf import FlaskForm

class CreateArticleForm(FlaskForm):
    title=StringField('Title', [validators.DataRequired()])
    text=TextAreaField('Text', [validators.DataRequired()])
    submit = SubmitField('Create')
    
