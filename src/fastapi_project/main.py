from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/about")
def about():
    return {"message": "About page"}


@app.get("/users")
def users():
    return {"message": "Users list"}


@app.post("/users")
def create_users():
    return {"message": "User created"}
