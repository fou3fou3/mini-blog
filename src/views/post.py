from flask import render_template, request, redirect
from mongo_utils import MongoDB, authenticate_jwt

def post():
	if request.method == 'GET':
		return render_template('post.html', title='post', method='GET')

	elif request.method == 'POST':
		if 'authenticated' == authenticate_jwt(request.form.get('jwt')):
			title = request.form.get('title')
			article = request.form.get('article')
			u_id = MongoDB.add_post(title, article)
			return redirect(f'/article/{u_id}')
		else:	return render_template('post.html', title='post', method='POST')