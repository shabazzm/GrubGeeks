from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, TextAreaField
from wtforms.validators import DataRequired,Email,EqualTo,Length
from wtforms import ValidationError

class LoginForm(FlaskForm):
    email_address = StringField('Email',validators=[Email(message='Enter a valid email.'),DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    email_address = StringField('Email',validators=[DataRequired(),Email(message='Enter a valid email')])
    user_name = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),
                            EqualTo('pass_confirm',message='Passwords do not match. Please re-enter.'),
                            Length(min=6, max=25, message='Password must be at  6-25 characters')])
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    
    submit = SubmitField('Register!')

class AddPostForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired()])
    main_post_content = TextAreaField('Post Content', validators=[DataRequired()])
    submit = SubmitField('Add Post')

class AddReplyForm(FlaskForm):
    reply_content = TextAreaField('Reply Content', validators=[DataRequired()])
    submit = SubmitField('Post Reply')
