from flask import Flask, render_template,session,redirect,url_for,request


app =Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/entrees_gallery')
def entrees_gallery():
    return render_template('entrees_gallery.html')

@app.route('/roasted_bsprouts')
def roasted_bsprouts():
    return render_template('roasted_bsprouts.html')

@app.route('/chicken_quesadila')
def chicken_quesadila():
    return render_template('chicken_quesadila.html')



if __name__ == '__main__':
    app.run(debug=True)
