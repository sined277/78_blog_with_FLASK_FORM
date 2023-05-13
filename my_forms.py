from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField
import random


class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign Me Up!")


class CommentForm(FlaskForm):
    submit = SubmitField("Submit Comment")
    comment_text = CKEditorField("Comment", validators=[DataRequired()])


##WTForm
class CreatePostForm(FlaskForm):
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    title = StringField("Blog Post Title", validators=[DataRequired()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let Me In!")
