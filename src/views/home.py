from flask import render_template
from mongo_utils import get_posts

def home():
	return render_template('home.html', title="Fouad's mini-blog", posts=get_posts())
