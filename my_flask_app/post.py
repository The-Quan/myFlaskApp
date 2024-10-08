import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore

# Load environment variables
load_dotenv()

# Initialize Firebase Admin SDK with environment variables
cred = credentials.Certificate({
    "type": "service_account",
    "project_id": os.getenv("FIREBASE_PROJECT_ID"),
    "private_key": os.getenv("FIREBASE_PRIVATE_KEY").replace("\\n", "\n"),
    "client_email": os.getenv("FIREBASE_CLIENT_EMAIL"),
    "token_uri": "https://oauth2.googleapis.com/token"
})

firebase_admin.initialize_app(cred)
db = firestore.client()

# Functions
posts = []

def get_posts():
    posts_ref = db.collection("posts").stream()
    posts.clear()
    for post in posts_ref:
        posts.append(post.to_dict())
    return posts

def add_posts(title, content):
    post = {'title': title, 'content': content}
    db.collection("posts").add(post)
    posts.append(post)
