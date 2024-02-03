from flask import render_template, request, redirect
from mongo_utils import MongoDB
from ipaddress import ip_address

def post():
	if not ip_address(request.remote_addr).is_private: return render_template('404.html')
	if request.method == 'GET':
		return render_template('post.html', title='post', method='GET')

	elif request.method == 'POST':
		title = request.form.get('title')
		article = request.form.get('article')
		u_id = MongoDB.add_post(title, article)
		return redirect(f'/article/{u_id}')
