import dotenv
import os
import uuid
import arrow
import jwt
from pymongo import MongoClient

dotenv.load_dotenv()
connection_string = str(os.environ['MONGO-URI'])
client = MongoClient(connection_string)

class MongoDB:
	mini_blog = client.get_database("mini-blog")
	posts = mini_blog.get_collection("posts")

	@staticmethod
	def add_post(title, article):
		u_id = str(uuid.uuid4()).replace("-", "")
		post = {"title": title, "date": arrow.now().format('DD/MM/YYYY'), "article": article, "u_id": u_id}
		result = MongoDB.posts.insert_one(post)
		print(f"Inserted post with ID: {result.inserted_id}")
		return u_id

	@staticmethod
	def get_posts():
		all_posts = list(MongoDB.posts.find())
		all_posts = all_posts[::-1]
		return all_posts

	@staticmethod
	def get_post(u_id):
		uid_query = {"u_id": u_id}
		post = MongoDB.posts.find_one(uid_query)
		return post

def authenticate_jwt(jwt_encoded):
	try:
		jwt_decoded = jwt.decode(jwt_encoded, os.environ['JWT'], algorithms=['HS256'])
		if 'permission' in jwt_decoded and jwt_decoded['permission'] == 'permitted':
			return 'authenticated'
		else:
			return 'unauthenticated'
	except jwt.exceptions.DecodeError:
		return 'unauthenticated'
