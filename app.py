# Importing flask module in the project is mandatory.
from flask import Flask ,render_template,request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import csv
app = Flask(__name__)#web application framework
#
#

# Flask is a web application framework written in Python. It is developed by Armin Ronacher, who leads an international
# group of Python enthusiasts named Pocco. Flask is based on the Werkzeug WSGI toolkit and Jinja2 template engine.
# Both are Pocco projects.

# WSGI
# Web Server Gateway Interface (WSGI) has been adopted as a standard for Python web application development. WSGI is a
# specification for a universal interface between the web server and the web applications.

# Werkzeug
# It is a WSGI toolkit, which implements requests, response objects, and other utility functions. This enables building
# a web framework on top of it. The Flask framework uses Werkzeug as one of its bases.

# Jinja2
# Jinja2 is a popular templating engine for Python. A web templating system combines a template with a certain data
# source to render dynamic web pages.

# Web Application Framework or simply Web Framework represents a collection of libraries and modules that enables
# a web application developer to write applications without having to bother about low-level details such as
# protocols, thread management etc.

# Flask is often referred to as a micro framework. It aims to keep the core of an application simple yet extensible.
# Flask does not have built-in abstraction layer for database handling, nor does it have form a validation support.
# Instead, Flask supports the extensions to add such functionality to the application.

@app.route('/')#route() function of the Flask class is a decorator, which tells the application which URL should call
               # the associated function. -->app.route(rule, options)
def homepage():
    return "<h1>Home Page</h1>"


# It is possible to build a URL dynamically, by adding variable parts to the rule parameter. This variable part is
# marked as <variable-name>. It is passed as a keyword argument to the function with which the rule is associated.
@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

@app.route('/testing')
def testing():
    return '''<!doctype html>
    <html>
    <head>
    <meta charset="UTF-8">
    <title>Testing</title>
    </head>
    <body>
    <h1>Testing</h1>
    </body>
    </html>
    '''
#
# However, generating HTML content from Python code is cumbersome, especially when variable data and Python language
# elements like conditionals or loops need to be put. This would require frequent escaping from HTML.

@app.route('/review')
def review():
    form = ReviewForm()
    data=[]
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        line_count = 0
        for row in csv_reader:
            data.append(row[2])
    return render_template('Review.html',title = 'Main', form =form, reviewForm = 'Review Form', data = data)
# This is where one can take advantage of Jinja2 template engine, on which Flask is based. Instead of returning
# hardcode HTML from the function, a HTML file can be rendered by the render_template() function.

@app.route('/layout')
def layout():
    return render_template('layout.html',title='Main Layout')


# The add_url_rule() function of an application object is also available to bind a URL with a function as in the
# above example, route() is used.

# Example
# def hello_world():
#    return ‘hello world’
# app.add_url_rule(‘/’, ‘hello’, hello_world)

@app.route('/submit',methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        result = request.form
        with open('data.csv', mode='a') as data_file:
            data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            data_writer.writerow([request.form.get("fname"), request.form.get("product"), request.form.get("review")])
    return "<h1>Submit!!!</h1>"
# def hello_world():
#     return 'Hello World!'
#
#
if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug=True)

# Debug mode
# A Flask application is started by calling the run() method. However, while the application is under development, it
# should be restarted manually for each change in the code. To avoid this inconvenience, enable debug support. The
# server will then reload itself if the code changes. It will also provide a useful debugger to track the errors if
# any, in the application.
#
# The Debug mode is enabled by setting the debug property of the application object to True before running or passing
# the debug parameter to the run() method.
#
# app.debug = True
# app.run()
# app.run(debug = True)
# fname = TextField('First Name  *',validators=[validators.DataRequired()])



class ReviewForm(Form):
    fname = TextField('First Name  *', validators=[validators.DataRequired()])
    product = TextField('Product Name  *', validators=[validators.DataRequired()])
    review = TextField('Review  *', validators=[validators.DataRequired()])
    submit = SubmitField('Submit Your Review')