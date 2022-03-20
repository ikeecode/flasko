from flask import Flask, render_template


# create a Flask instance
app = Flask(__name__)

# create  route decorator
@app.route('/')
# def index():
#     return "<h1> Hello, World ! </h1>"

def index():
    programming = ['python','<em>javascript</em>', 'java', 'php', 'html', 'flask', 'css', 'mysql',]

    return render_template('index.html', maliste = programming)

#
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', username = name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500
