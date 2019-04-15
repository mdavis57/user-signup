from flask import Flask, request, redirect
import os
import jinja2
import cgi

template_dir = os.path.join(os.path.dirname(__file__),
    'templates')
jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(template_dir), autoescape=True)


app = Flask(__name__)
app.config['DEBUG']= True

@app.route('/')
def index():
    template = jinja_env.get_template('homepage.html')
    return template.render()

@app.route('/welcome',methods=['POST'])
def welcome():
    username = request.form['username']
    template = jinja_env.get_template('welcome.html')
    return template.render(username = username)
    

'''def is_null(field):
    if field == NULL:
        return True
    else:
        return False'''

''' @app.route('/', methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    user_error = ''
    pass_error = '' 
    pass2_error = ''
    email_error = ''

    if is_null(username):
        user_error = 'Cannot leave field blank'
        username = ''
    else: 
        username = username
        if len(username) <3 or len(username) >20:
            user_error = "Character count must be in range 3-20"
            username = ''
    if not user_error:
        return redirect('/welcome')
    else:
        template = jinja_env.get_template('homepage.html')
        return template.render(user_error=user_error)'''




app.run()