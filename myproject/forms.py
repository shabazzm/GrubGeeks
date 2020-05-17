from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, TextAreaField, IntegerField
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
    main_post_content = StringField('Post Content', validators=[DataRequired()])
    submit = SubmitField('Add Post')

class AddReplyForm(FlaskForm):
    reply_content = TextAreaField('Reply Content', validators=[DataRequired()])
    submit = SubmitField('Post Reply')

class CalorieCalcForm(FlaskForm):
    daily_calories = IntegerField('Calories Consumed Today', validators=[DataRequired()])
    calorie_goal = IntegerField('Daily Caloric Goal', validators=[DataRequired()])
    submit = SubmitField('Get Recipe')

class AddRecipeForm(FlaskForm):
    recipe_name = StringField('Recipe Name', validators=[DataRequired()])
    calories = IntegerField('Number of Calories', validators=[DataRequired()])
    submit = SubmitField('Add Recipe')
