from pydantic import BaseModel, Field


class PostBase(BaseModel):
   title: str
   body: str
   user_id: int = Field(..., alias="userId")


class PostCreate(PostBase):
    """New post creation schema"""


class PostRead(PostBase):
    id: int
