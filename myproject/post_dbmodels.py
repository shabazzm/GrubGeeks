#Database Table Models
from myproject import login_manager, db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin


# Base Post
class Post(db.Model):
	
	def __init__(self, user_id, post_id, date_created):
	    self.user_id = user_id
	    self.post_id = post_id
	    self.date_created = date_created

    post_id = db.Column('post_id', db.Integer, primary_key=True, nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user_accounts.user_id'), nullable=False)

    date_created = db.Column('date_created', db.DateTime, nullable=False)


#User Posts
class Topic(Post):

    def __init__(self, user_id, post_id, subject, main_post_content, date_created):
    	super().__init__(user_id=user_id, post_id=post_id, date_created=date_created)
        self.subject = subject
        self.main_post_content = main_post_content

    __tablename__ = 'user_posts'
    __table_args__ = {'sqlite_autoincrement': True}
    
    subject = db.Column('subject', db.String(100), nullable=False)

    main_post_content = db.Column('main_post_content', db.String(254), nullable=False)
    
    post_replies = db.relationship('Post_Replies', backref='user_posts',lazy='dynamic')


#User Replies
class Reply(Post):

	def __init__(self, user_id, post_id, subject, main_post_content, date_created):
	    	super().__init__(user_id=user_id, post_id=post_id, date_created=date_created)
	        self.reply_content = reply_content

    __tablename__ = 'post_replies'
    __table_args__ = {'sqlite_autoincrement': True}
    
    reply_id = db.Column('reply_id', db.Integer, primary_key=True)

    reply_content = db.Column('subject', db.String(254), nullable=False)