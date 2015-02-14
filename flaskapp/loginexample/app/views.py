from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = { 'nickname' : 'Aayush' }
	return render_template('index.html', title = 'Home', user = user)

@app.route('/about/')
def aboutus():
	return render_template('aboutus.html', title='About Us')

@app.route('/login')
def login_view():
        return render_template('login.html')
