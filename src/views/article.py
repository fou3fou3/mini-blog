from flask import render_template
from mongo_utils import get_post

def article(u_id:str):
	post = get_post(u_id)
	if post:
		return render_template('article.html', post=post)
	else:
		return render_template('404.html'), 404