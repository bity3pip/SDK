from typing import Any

from fastapi import FastAPI, HTTPException, status

from app.schemas.post import PostCreate, PostRead
from app.sdk.jsonplaceholder import JSONPlaceholderSDK
from app.service.post_service import PostService
from app.storage.memory_storage import DataStorage

app = FastAPI(title="SDK Challenge API")

sdk = JSONPlaceholderSDK()
storage = DataStorage()
service = PostService(sdk, storage)


@app.get("/fetch/{post_id}")
async def fetch_post(post_id: int) -> dict[str, Any] | PostRead:
    try:
        return service.get_post(post_id)
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(error),
        )


@app.get("/fetch-recent")
async def fetch_recent(limit: int = 5) -> list[PostRead]:
    return service.get_recent_posts(limit)


@app.get("/posts/{post_id}")
async def get_local_post(post_id: int) -> PostRead:
    post = storage.get(post_id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post {post_id} not found in local storage",
        )
    return post


@app.get("/posts")
async def get_saved_postsapp() -> list[PostRead]:
    return service.get_local_posts()


@app.post("/create")
async def create_post(post: PostCreate) -> PostRead:
    return service.create_post(
        post.title,
        post.body,
        post.user_id,
    )
