from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

custom = FastAPI()
my_posts = [{"title": "test", "content": "test content", "is_public": True}]


class Post(BaseModel):
    title: str = Field()
    content: str
    is_public: bool
    rating: Optional[int] = None

    # @model_validator(mode="after")
    # def test(self) -> "Post":
    #     if not self.title.strip():
    #         raise ValueError("this string should be field with white spaces")
    #     return self


@custom.get("/post")
def post():
    return "name"


@custom.post("/posts")
def get_post(post: Post):
    return {"message": f"{post}"}


@custom.patch(f"/posts/{id}")
def change_post_metadata():
    pass
