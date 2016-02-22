from flask import Flask, render_template, request, redirect, url_for, abort, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'F34TF$($e34D';
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/development';
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True;

from models import *

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/signup', methods=['POST'])
def signup():
	user = Users(request.form['username'],request.form['firstname'],request.form['lastname'],request.form['email'],request.form['message'])
	db.session.add(user)
	db.session.commit()
	return redirect(url_for('message', username=user.username))

@app.route('/message')
def show_messages():
	users = Users.query.all()
	return render_template('show_all.html', list=users)

@app.route('/message/<username>')
def message(username):
	user = Users.query.filter_by(username=username).first_or_404()
	return render_template('message.html', username=user.username, firstname=user.firstname, lastname=user.lastname, email=user.email, message=user.message)

if __name__ == '__main__':
    app.run()