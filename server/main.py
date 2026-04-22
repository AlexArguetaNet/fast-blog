from fastapi import FastAPI, HTTPException

app = FastAPI()

posts: list[dict] = [
    {
        "id": 1,
        "author": "Corey Schafer",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even better.",
        "date_posted": "April 21, 2025",
    },
]

@app.get("/")
def home():
    return {"msg": "Hello, world!"}

# Can stack decorators to provide multiple API routes
# fot the same function
@app.get("/api/posts")
@app.get("/posts", include_in_schema=False) # include_in_schema=False excludes the route from the docs
def get_posts():
    return posts

@app.get("/api/posts/{post_id}")
def get_post(post_id: int):
    if post_id > len(posts) - 1 or post_id < 0:
        raise HTTPException(status_code=404, detail="Post not found")
    else:
        return posts[post_id]
