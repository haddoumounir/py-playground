from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/names/{names}")
def sayMyName(names):
    return "hello " + names


@app.post("/createPosts")
def create_posts(playLoad: dict = Body()):
    # ! use single quote to access part pf dict
    return {"message": f"succuss register post with name: {playLoad['title']}"}


# title
# content

a = "aaaaa"

a