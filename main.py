from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, db

# Initialize the Firebase app
cred = credentials.Certificate("sdk.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://books-7f64d-default-rtdb.firebaseio.com'  # Replace with your database URL
})

# Get a reference to the database
ref = db.reference("/")

app = Flask(__name__)


@app.route('/api/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    author = data.get('author')
    category = data.get('category')
    likes = data.get('likes')
    createdAt = data.get('createdAt')
    if not title or not content:
        return jsonify({"error": "Please provide title and content"}), 400
    
    post = {   
        "title": title,
        "content": content,
        "author": author,
        "category": category,
        "likes": likes,
        "createdAt": createdAt
    }
    comments = data.get('comments')
    if comments:
        post["comments"] = comments
    ref.child("Posts").push(post)
    return jsonify(data), 201

@app.route('/api/posts', methods=['GET'])
def get_posts():
    posts = ref.child("Posts").get()
    return jsonify(posts), 200

@app.route('/api/posts/<post_id>', methods=['GET'])
def get_post(post_id):
    post = ref.child("Posts").child(post_id).get()
    if post:
        return jsonify(post), 200
    return jsonify({"error": "Post not found"}), 404

@app.route('/api/posts/<post_id>', methods=['PUT'])
def update_post(post_id):
    data = request.get_json()
    post = ref.child("Posts").child(post_id).get()
    if post:
        ref.child("Posts").child(post_id).update(data)
        return jsonify(data), 200
    return jsonify({"error": "Post not found"}), 404

@app.route('/api/posts/<post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = ref.child("Posts").child(post_id).get()
    if post:
        ref.child("Posts").child(post_id).delete()
        return jsonify({"message": "Post deleted successfully"}), 200
    return jsonify({"error": "Post not found"}), 404

@app.route('/like/<post_id>', methods=['POST'])
def like_post(post_id):
    post = ref.child("Posts").child(post_id).get()
    if post:
        likes = post.get("likes", 0)
        ref.child("Posts").child(post_id).update({"likes": likes + 1})
        return jsonify({"message": "Post liked successfully"}), 200
    return jsonify({"error": "Post not found"}), 404

@app.route('/comment/<post_id>', methods=['POST'])
def comment_post(post_id):
    data = request.get_json()
    post = ref.child("Posts").child(post_id).get()
    if post:
        comments = post.get("comments", [])
        comments.append(data)
        ref.child("Posts").child(post_id).update({"comments": comments})
        return jsonify({"message": "Comment added successfully"}), 200
    return jsonify({"error": "Post not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
