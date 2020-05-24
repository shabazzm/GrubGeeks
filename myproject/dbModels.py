#Database Table Models
from myproject import login_manager, db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User_Accounts.query.get(user_id)

#Recipe Calories Model
class Recipe_Calories(db.Model):
    __tablename__ = 'recipe_calories'
    recipe_id = db.Column('recipe_id',
                db.Integer,
                primary_key=True,
                nullable=False)
    recipe_name = db.Column('recipe_name',
                  db.String(100),
                  nullable=False)
    calories = db.Column('calories',
               db.Integer,
               nullable=False)

#User Accounts Model
class User_Accounts(db.Model, UserMixin):
    __tablename__ = 'user_accounts'
    __table_args__ = {'sqlite_autoincrement': True}
    user_id = db.Column('user_id',
              db.Integer,
              primary_key=True,
              nullable=False)
    user_name = db.Column('user_name',
                db.String(100),
                nullable=False,
                unique=True)
    email_address = db.Column('email_address',
                    db.String(254),
                    nullable=False,
                    unique=True)
    password_hash = db.Column('password_hash',
               db.String(200),
               nullable=False)
    user_posts = db.relationship('User_Posts', backref='user_accounts', lazy='dynamic')
    post_replies = db.relationship('Post_Replies', backref='user_accounts', lazy='dynamic')

    def __init__(self, email_address, user_name, password):
        self.user_name = user_name
        self.email_address = email_address
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def get_id(self):
        return (self.user_id)
        