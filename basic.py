from myproject import app,db
from flask import Flask, render_template,session,redirect,url_for,request, flash, abort
from flask_login import login_user,login_required,logout_user, current_user
from myproject.dbModels import User_Accounts, Recipe_Calories
from myproject.post_dbmodels import Topic, Reply
from myproject.forms import LoginForm,RegistrationForm, AddPostForm, AddReplyForm, CalorieCalcForm
from datetime import datetime
from sqlalchemy.sql import select
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc

#App Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User_Accounts.query.filter_by(email_address=form.email_address.data).first()
        if user is None:
            flash('This user does not exist in our system. Please try again.')

        elif user.check_password(form.password.data) and user is not None:
            login_user(user)
            next = request.args.get('next')

            if next == None or not next[0]=='/':
                next = url_for('home')

            return redirect(next)
        else:
            flash('Invalid username/password combination')
    return render_template('login.html',form=form)

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        existing_user_email = User_Accounts.query.filter_by(email_address=form.email_address.data).first()
        existing_user_name = User_Accounts.query.filter_by(user_name=form.user_name.data).first()
        if existing_user_email is None and existing_user_name is None:
            user = User_Accounts(email_address=form.email_address.data,
                                user_name=form.user_name.data,
                                password=form.password.data)
            db.session.add(user)
            db.session.commit()
            flash("You have successfully registered an account!")
            return redirect(url_for('login'))

        else:
            flash('A user already exists with that email address or username.')
    return render_template('register.html',form=form)


# main forum page
@app.route('/forum')
def forum():
    posts = Topic.query.order_by(desc(Topic.date_created))
    post_count = Topic.query.count()
    print(Topic.query.count())
    return render_template('forum.html', posts=posts, post_count=post_count)

# add post to forum
@app.route('/add_post', methods=['GET', 'POST'])
def add_post():
    form = AddPostForm()
    if request.method == 'POST':
        user_id = current_user.user_id
        date_created = datetime.now()
        subject = form.subject.data
        main_post_content = form.main_post_content.data
        post = Topic(user_id=user_id, subject=subject, main_post_content=main_post_content, date_created=date_created)
        db.session.add(post)
        db.session.commit()
        flash("Post Created")
        return redirect(url_for('forum'))
    else:
        return render_template('add_post.html', form=form)

@app.route('/post/<string:post_id>/add_success/')
def successful_add_post(post_id):
    id = int(post_id)
    select = "SELECT post_id, user_id, subject, post_content, date_created from Topic WHERE post_id = " + id
    result = db.session.execute(select)
    auth_query = "SELECT user_name FROM User_Accounts WHERE user_id = " + result.user_id
    auth = db.session.execute(auth_query)
    return render_template('post.html', post=result, author=auth)

# view a specific post's thread (get) / post reply (post)
@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post(post_id):
    post = Topic.query.filter_by(post_id=post_id).first()
    form = AddReplyForm()
    author = User_Accounts.query.filter_by(user_id=post.user_id).first()
    if form.validate_on_submit():
        reply_content = form.reply_content.data
        user_id=current_user.user_id
        date_created=datetime.now()
        db.session.execute("INSERT INTO Reply (post_id, user_id, reply_content, date_created) VALUES (" + str(post_id) + ", " + str(user_id) + ", '" + reply_content + "', '" +  str(date_created) + "')")
        db.session.commit()
        flash("Reply Posted")
        return redirect('/post/' + str(post_id))
    else:
        replies = db.session.execute("SELECT reply_id, user_id, reply_content, date_created FROM Reply WHERE post_id = " + str(post_id))
        return render_template('post.html', post=post, replies=replies, form=form, author=author)

#routes to food gallery
@app.route('/entrees_gallery')
def entrees_gallery():
    return render_template('entrees_gallery.html')

#route to calorie calculator
@app.route('/calorie_calc', methods=['GET', 'POST'])
def calorie_calc():
    form = CalorieCalcForm()
    error=None
    if form.validate_on_submit():
        # do all the stuff
        calories_in = int(form.daily_calories.data)
        calorie_goal = int(form.calorie_goal.data)
        if calories_in >= calorie_goal:
            error="Calorie goal must be greater than calories consumed"
            return render_template('calorie_calc.html', form=form, error=error)
        else:
        	optimal_calories = calorie_goal - calories_in
        	return redirect('/calc_results/' + str(optimal_calories))
    else:
        return render_template('calorie_calc.html', form=form, error=None)

@app.route('/calc_results/<int:optimal_calories>')
def calc_results(optimal_calories):
    query = "SELECT * from Recipe_Calories WHERE calories BETWEEN  0 AND " + str(optimal_calories)
    recipes = db.session.execute(query)
    return render_template('calc_results.html', recipes=recipes)

#routes to 9 recipe pages
@app.route('/roasted_bsprouts')
def roasted_bsprouts():
    return render_template('roasted_bsprouts.html')

@app.route('/chicken_quesadila')
def chicken_quesadila():
    return render_template('chicken_quesadila.html')

@app.route('/thai_basil_chicken')
def thai_basil_chicken():
    return render_template('thai_basil_chicken.html')

@app.route('/white_bean_soup')
def white_bean_soup():
    return render_template('white_bean_soup.html')

@app.route('/italian_parmesean_chicken')
def italian_parmesean_chicken():
    return render_template('italian_parmesean_chicken.html')

@app.route('/sweet_potato_chips')
def sweet_potato_chips():
    return render_template('sweet_potato_chips.html')

@app.route('/green_beans')
def green_beans():
    return render_template('green_beans.html')

@app.route('/orange_chicken')
def orange_chicken():
    return render_template('orange_chicken.html')

@app.route('/lemon_rosemary_salmon')
def lemon_rosemary_salmon():
    return render_template('/lemon_rosemary_salmon.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.errorhandler(401)
def unauthorized_error(e):
    return render_template('401.html'), 401

@app.errorhandler(400)
def bad_request(e):
    return render_template('400.html'), 400

@app.errorhandler(403)
def forbidden_error(e):
    return render_template('403.html'), 403

@app.errorhandler(503)
def service_unavilble(e):
    return render_template('503.html'), 503

@app.errorhandler(408)
def request_timeout(e):
    return render_template('408.html'), 408

if __name__ == '__main__':
    app.run(debug=True)
