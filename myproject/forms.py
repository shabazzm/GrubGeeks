from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
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

    def check_email(self,field):
        if User_Accounts.query.filter_by(email_address=field.data).first():
            raise ValidationError('Your email address has already been registered!')

    def check_username(self,field):
        if User_Accounts.query.filter_by(user_name).first():
            raise ValidationError('Username is already taken!')
