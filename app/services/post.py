from ..dependencies import SessionDep
from fastapi import status, HTTPException
from ..core import Post
from ..repositories import CrudGen
from ..schemas import PostCreate


class PostService:
    def __init__(self, session: SessionDep) -> None:
        self._repository = CrudGen(Post, session)

    async def create_post(self, data: PostCreate) -> Post:
        try:
            new_data = Post(**data.model_dump())
            return self._repository.add(new_data)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    async def list_posts_by_recruiter(self, id: int) -> list[Post]:
        return list(self._repository.get_by_field("recruiter_id", id))

    async def close_post(self, recruiter_id: int, id: int):
        try:
            updated_data = Post(recruiter_id=recruiter_id, is_open=False)
            return self._repository.update(id, updated_data)
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

    async def list_posts(self) -> list[Post]:
        return list(self._repository.find_all())
