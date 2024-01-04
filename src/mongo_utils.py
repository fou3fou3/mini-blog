import dotenv, os, uuid, arrow, jwt
from pymongo import MongoClient

dotenv.load_dotenv()
connection_string = str(os.environ['MONGO-URI'])
client = MongoClient(connection_string)
mini_blog = client.get_database("mini-blog")
posts = mini_blog.get_collection("posts")

def add_post(title, article):
	u_id = str(uuid.uuid4()).replace("-", "")
	post = {"title": title, "date": arrow.now().format('DD/MM/YYYY'), "article": article, "u_id": u_id}
	result = posts.insert_one(post)
	print(f"Inserted post with ID: {result.inserted_id}")
	return u_id

def get_posts():
	all_posts = list(posts.find())
	all_posts = all_posts[::-1]
	return all_posts

def get_post(u_id):
	uid_query = {"u_id": u_id}
	post = posts.find_one(uid_query)
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