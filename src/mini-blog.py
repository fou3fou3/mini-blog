from flask import Flask, redirect, url_for, render_template
from views import home, article, post

miniblog = Flask(__name__)


miniblog.add_url_rule('/', view_func=home.home)
miniblog.add_url_rule('/post', view_func=post.post, methods=['GET', 'POST']) # type: ignore
miniblog.add_url_rule('/article/<string:u_id>', view_func=article.article)


# Redirect users from /home, /main to / .
@miniblog.route('/home')
@miniblog.route('/main')
def redirect_to_root():
    return redirect(url_for('home'))

@miniblog.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == "__main__":
    miniblog.run(host='0.0.0.0', port=80)