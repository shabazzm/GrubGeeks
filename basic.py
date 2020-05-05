from myproject import app,db
from flask import Flask, render_template,session,redirect,url_for,request, flash, abort
from flask_login import login_user,login_required,logout_user
from myproject.dbModels import User_Accounts, Recipe_Calories, User_Posts, Post_Replies
from myproject.forms import LoginForm,RegistrationForm, AddPostForm
from datetime import datetime
from sqlalchemy.sql import select
from sqlalchemy import create_engine

#App Routes
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You logged out!")
    return redirect(url_for('home'))

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User_Accounts.query.filter_by(email_address=form.email_address.data).first()
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Logged in Successfully')
            next = request.args.get('next')

            if next == None or not next[0]=='/':
                next = url_for('home')

            return redirect(next)
    return render_template('login.html',form=form)

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User_Accounts(email_address=form.email_address.data,
                            user_name=form.user_name.data,
                            password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("You have successfully registered an account!")
        return redirect(url_for('login'))

    return render_template('register.html',form=form)


# main forum page
@app.route('/forum')
def forum():
    # query="SELECT * FROM User_Posts ORDER BY date_created DESC"
    # posts = db.session.execute(query)
    # db.session.commit()
    posts = User_Posts.query.order_by(User_Posts.date.desc())
    return render_template('forum.html', posts=posts)
    #posts = User_Posts.query.filter_by(*).order_by()

# add post to forum
@app.route('/add_post', methods=['GET', 'POST'])
def add_post():
    form = AddPostForm()
    if form.validate_on_submit():
        engine = create_engine('sqlite:///myproject\\grubgeeks.db')
        res = select([User_Posts])
        # select = "SELECT MAX(User_Posts.post_id) FROM User_Posts"
        result = engine.execute(res)
        max_id=0
        for row in result:
            if row.post_id > max_id:
                max_id = row.post_id
        post_id = max_id + 1
        user_id = current_user.user_id
        date_created = datetime.now()
        subject = form.subject.data
        main_post_content = form.main_post_content.data
        post = User_Posts(user_id, subject, main_post_content, date_created)
        db.session.add(post)
        db.session.commit()
        url = ("/post/" + str(post_id) + "/add_success/")
        return redirect(url)
    else:
        return render_template('add_post.html', form=form)

@app.route('/post/<string:post_id>/add_success/')
def successful_add_post(post_id):
    id = int(post_id)
    select = "SELECT post_id, user_id, subject, post_content, date_created from User_Posts WHERE post_id = " + id
    result = db.session.execute(select)
    auth_query = "SELECT user_name FROM User_Accounts WHERE user_id = " + result.user_id
    auth = db.session.execute(auth_query)
    return render_template('post.html', post=result, author=auth)

# view a specific post's thread / post reply
@app.route('/post/<string:post_id>', methods=['GET', 'POST'])
def post(post_id):
    return render_template('index.html')

#routes to food gallery
@app.route('/entrees_gallery')
def entrees_gallery():
    return render_template('entrees_gallery.html')

#route to calorie calculator
@app.route('/calorie_calc')
def calorie_calc():
    #Recipes = Recipe_Calories.query.all()
    return render_template('calorie_calc.html')

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
