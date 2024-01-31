from flask import render_template
from mongo_utils import MongoDB

def home():
	return render_template('home.html', title="Fouad's mini-blog", posts=MongoDB.get_posts())
