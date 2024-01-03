from flask import render_template, request
from mongo_utils import add_post, authenticate_jwt

def post():
	if request.method == 'GET':
		return render_template('post.html', title='post', method='GET')

	elif request.method == 'POST':
		print(request.form.get('jwt'))
		if 'authenticated' == authenticate_jwt(request.form.get('jwt')):
			title = request.form.get('title')
			article = request.form.get('article')
			u_id = add_post(title, article)
			return render_template('post.html', title='post', method='POST', success=True, u_id=u_id)
		else:	return render_template('post.html', title='post', method='POST', success=False)
		