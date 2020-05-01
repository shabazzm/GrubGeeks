#Database Table Models
from myproject import login_manager, db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
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
    password = db.Column('password',
               db.String(200),
               nullable=False)
    password_salt = db.Column('password_salt',
                    db.String(50),
                    nullable=True)
    password_hash_algorithm = db.Column('password_hash_algorithm',
                              db.String(50),
                              nullable=False)
    user_posts = db.relationship('User_Posts', backref='user_accounts', lazy='dynamic')
    post_replies = db.relationship('Post_Replies', backref='user_accounts', lazy='dynamic')

    def __init__(self, user_name, email_address, password, password_salt, password_hash_algorithm):
        self.user_name = user_name
        self.email_address = email_address
        self.password = password
        self.password_salt = password_salt
        self.password_hash_algorithm = password_hash_algorithm

#User Posts Model
class User_Posts(db.Model):
    __tablename__ = 'user_posts'
    __table_args__ = {'sqlite_autoincrement': True}
    post_id = db.Column('post_id',
              db.Integer,
              primary_key=True,
              nullable=False)
    user_id = db.Column(db.Integer,
              db.ForeignKey('user_accounts.user_id'),

              nullable=False)
    subject = db.Column('subject',
              db.String(100),
              nullable=False)
    main_post_content = db.Column('main_post_content',
                        db.String(254),
                        nullable=False)
    date_created = db.Column('date_created',
                   db.DateTime,
                   nullable=False)
    post_replies = db.relationship('Post_Replies', backref='user_posts',lazy='dynamic')

    def __init__(self, user_id, subject, main_post_content, date_created):
        self.user_id = user_id
        self.subject = subject
        self.main_post_content = main_post_content
        self.date_created = date_created

#Post Replies Model
class Post_Replies(db.Model):
    __tablename__ = 'post_replies'
    __table_args__ = {'sqlite_autoincrement': True}
    reply_id = db.Column('reply_id',
               db.Integer,
               primary_key=True)
    post_id = db.Column(db.Integer,
              db.ForeignKey('user_posts.post_id'),
              nullable=False)
    user_id = db.Column(db.Integer,
              db.ForeignKey('user_accounts.user_id'),
              nullable=False)
    reply_content = db.Column('subject',
                    db.String(254),
                    nullable=False)
    date_created = db.Column('date_created',
                   db.DateTime,
                   nullable=False)

    def __init__(self, post_id, user_id, reply_content, date_created):
        self.post_id = post_id
        self.user_id = user_id
        self.reply_content = reply_content
        self.date_created = date_created
