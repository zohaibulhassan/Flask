from flask import Flask,render_template
from data import Articles
app = Flask(__name__)

@app.route('/')

@app.route('/home')
def index():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/articles')
def article():
    return render_template('articles.html',articles = Articles)



if __name__ == '__main__':
    app.run(debug=True)
