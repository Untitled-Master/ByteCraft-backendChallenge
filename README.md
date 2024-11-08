# ByteCraft-backendChallenge


# Flask API with Firebase Realtime Database

This Flask API is connected to a Firebase Realtime Database and allows creating, reading, updating, deleting, liking, and commenting on posts.

## Requirements

- Python 3.x
- Firebase Admin SDK JSON credentials file (`sdk.json`)
- Flask (`pip install flask`)
- Firebase Admin SDK (`pip install firebase-admin`)

## Setup

1. Place your Firebase Admin SDK JSON credentials file in the project directory as `sdk.json`.
2. Replace `databaseURL` in the code with your Firebase Realtime Database URL.
3. Install the required libraries:
   ```bash
   pip install flask firebase-admin

## Running the Server

Start the Flask server with:
```bash
python app.py
```

The server will run on `http://127.0.0.1:5000`.

## API Endpoints

### 1. Create a Post

- **Endpoint**: `/api/posts`
- **Method**: POST
- **Description**: Creates a new post.
- **Request Body**:
  ```json
  {
    "title": "Post Title",
    "content": "Post content",
    "author": "Author Name",
    "category": "Post Category",
    "likes": 0,
    "createdAt": "2024-11-08",
    "comments": [
      {
        "author": "Commenter Name",
        "text": "Comment text"
      }
    ]
  }
  ```

### 2. Get All Posts

- **Endpoint**: `/api/posts`
- **Method**: GET
- **Description**: Fetches all posts.

### 3. Get a Single Post

- **Endpoint**: `/api/posts/<post_id>`
- **Method**: GET
- **Description**: Fetches a single post by its ID.
- **Example**:
  ```python
  import requests
  response = requests.get("http://127.0.0.1:5000/api/posts/<post_id>")
  print(response.json())
  ```

### 4. Update a Post

- **Endpoint**: `/api/posts/<post_id>`
- **Method**: PUT
- **Description**: Updates a post by its ID.
- **Request Body**:
  ```json
  {
    "title": "Updated Title",
    "content": "Updated content"
  }
  ```

### 5. Delete a Post

- **Endpoint**: `/api/posts/<post_id>`
- **Method**: DELETE
- **Description**: Deletes a post by its ID.

### 6. Like a Post

- **Endpoint**: `/like/<post_id>`
- **Method**: POST
- **Description**: Increments the "likes" count of the post by 1.
- **Example**:
  ```python
  import requests
  response = requests.post("http://127.0.0.1:5000/like/<post_id>")
  print(response.json())
  ```

### 7. Add a Comment to a Post

- **Endpoint**: `/comment/<post_id>`
- **Method**: POST
- **Description**: Adds a comment to a post.
- **Request Body**:
  ```json
  {
    "author": "Commenter Name",
    "text": "Comment text"
  }
  ```

## Example Python Code to Request Each Route

### 1. Create a Post
```python
import requests

url = "http://127.0.0.1:5000/api/posts"
data = {
    "title": "New Post",
    "content": "This is the content of the post",
    "author": "Ahmed",
    "category": "Technology",
    "likes": 0,
    "createdAt": "2024-11-08",
    "comments": []
}

response = requests.post(url, json=data)
print(response.json())
```

### 2. Get All Posts
```python
import requests

response = requests.get("http://127.0.0.1:5000/api/posts")
print(response.json())
```

### 3. Get a Single Post
```python
import requests

post_id = "<post_id>"
response = requests.get(f"http://127.0.0.1:5000/api/posts/{post_id}")
print(response.json())
```

### 4. Update a Post
```python
import requests

post_id = "<post_id>"
data = {
    "title": "Updated Post Title",
    "content": "Updated content for the post"
}

response = requests.put(f"http://127.0.0.1:5000/api/posts/{post_id}", json=data)
print(response.json())
```

### 5. Delete a Post
```python
import requests

post_id = "<post_id>"
response = requests.delete(f"http://127.0.0.1:5000/api/posts/{post_id}")
print(response.json())
```

### 6. Like a Post
```python
import requests

post_id = "<post_id>"
response = requests.post(f"http://127.0.0.1:5000/like/{post_id}")
print(response.json())
```

### 7. Add a Comment to a Post
```python
import requests

post_id = "<post_id>"
data = {
    "author": "User",
    "text": "This is a comment."
}

response = requests.post(f"http://127.0.0.1:5000/comment/{post_id}", json=data)
print(response.json())
```

## Notes

- Replace `<post_id>` in the URLs with the actual ID of a post.
- Ensure your Firebase Realtime Database is properly configured and accessible.
- The server runs on `http://127.0.0.1:5000` by default.

```
