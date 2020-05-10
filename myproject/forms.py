from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, TextAreaField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError

class LoginForm(FlaskForm):
    email_address = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password')
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    email_address = StringField('Email',validators=[DataRequired(),Email()])
    user_name = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('pass_confirm',message='Passwords do not match. Please re-enter.')])
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register!')

    def check_email(self,field):
        if User_Accounts.query.filter_by(email_address=field.data).first():
            raise ValidationError('Your email address has already been registered!')

    def check_username(self,field):
        if User_Accounts.query.filter_by(user_name).first():
            raise ValidationError('Username is already taken!')

class AddPostForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired()])
    main_post_content = TextAreaField('Post Content', validators=[DataRequired()])
    submit = SubmitField('Add Post')

class AddReplyForm(FlaskForm):
    reply_content = TextAreaField('Reply Content', validators=[DataRequired()])
    submit = SubmitField('Post Reply')
