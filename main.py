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


def is_null(field):
    if len(field) <=0:
        return True
    else:
        return False

@app.route('/', methods=['POST'])
def validate_fields():
    user = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']
    user_error = ''
    email_error = ''
    password_error = ''
    user_length = len(user)
    pass_length = len(password)
    verify_pass_length = len(password)
    
    at_count = email.count('.')
    dot_count = email.count('@')

    if is_null(user):
        user_error = 'cannot leave field blank'
        
    if " " in user:
        user_error = "cannot contain space"
        user = ''
        password = ''
        verify_password = ''
    if user_length > 20 or user_length <3:
        user_error = " cannot be blank and must be between 3-20 characters"
        user = ''
        password = ''
        verify_password = ''
    
    if password != verify_password:
        password_error = "passwords must match"
        password=''
        verify_password = ''
    if pass_length >20 or pass_length <3:
        password_error = "passwords must not be left blank and be between 3-20 characters"
        password=''
        verify_password = ''
    if verify_pass_length >20 or pass_length <3:
        password_error = "passwords must not be left blank and be between 3-20 charaters"
        password=''
        verify_password = ''
    if " " in password or " " in verify_password:
        password_error = "passwords cannot contain spaces"
        password=''
        verify_password = ''

    if is_null(password) or is_null(verify_password):
        #password_error = 'cannot leave either password field blank'
        password = ''
        verify_password = ''
    
        
    if not is_null(email):
        email_length = len(email)
        if email_length >20 or email_length <3:
            email_error = "must be between 3-20 characters"
            email = ''
            password = ''
            verify_password = ''
        if at_count != 1 or dot_count != 1:
            email_error = 'email must contain exactly 1 @ and .'
            email = ''
            password = ''
            verify_password = ''
        if ' ' in email:
            email_error = 'email cannot contain spaces'
            password = ''
            verify_password = ''

        
    

    
    if not user_error and not password_error and not email_error:
        
        username = request.form['username']
        template = jinja_env.get_template('welcome.html')
        return template.render(username = username)
        
        
    else:
        template = jinja_env.get_template('homepage.html')
        return template.render(user_error=user_error, password_error=password_error, email_error=email_error, password=password, username=user, email=email,verify_password=verify_password)




@app.route('/welcome',methods=['POST'])
def welcome():
    username = request.form['username']
    template = jinja_env.get_template('welcome.html')
    return template.render(username = username)
    








app.run()