import os
from flask import Flask, render_template,session,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app =Flask(__name__, template_folder='templates')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'grubgeeks.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##################################################################################
#Database Table Models
class Recipe_Calories(db.Model):
    __tablename__ = 'Recipe_Calories'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.Text)
    calories = db.Column('calories', db.Integer)
##################################################################################

@app.route('/')
def index():
    return render_template('index.html')

#routes to food gallery
@app.route('/entrees_gallery')
def entrees_gallery():
    return render_template('entrees_gallery.html')

#route to calorie calculator
@app.route('/calorie_calc')
def calorie_calc():
    Recipes = Recipe_Calories.query.all()
    return render_template('calorie_calc.html', Recipes = Recipes)

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


if __name__ == '__main__':
    app.run(debug=True)
