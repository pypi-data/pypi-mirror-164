from typing import Any, Optional
from uuid import uuid4

from pydantic import UUID4
from pymongo import MongoClient

from authix.core.config import AuthConfig
from authix.data.query_exceptions import QueryResultNotFoundError
from authix.data.query_exceptions import UserAlreadyExistsError
from authix.data.users.model import UserModel
from authix.data.users.queries.interface import UserQueries


class MongoDBUserQueries(UserQueries):
    def __init__(self, config: AuthConfig) -> None:
        self._client = MongoClient(config.settings.mongodb_url)
        self._db = self._client.users
        self._users = self._db.users

    async def get_user_by_email(self, email: str) -> UserModel:
        user = self._users.find_one({"email": email})
        return self._transform_query_result(user)

    async def get_user_by_id(self, user_id: UUID4) -> UserModel:
        user = self._users.find_one({"id": str(user_id)})
        return self._transform_query_result(user)

    def _transform_query_result(self, user: Optional[dict[str, Any]]) -> UserModel:
        if user is None:
            raise QueryResultNotFoundError
        return UserModel(
            email=user["email"],
            id=user["id"],
            password_hash=user["password_hash"],
        )

    async def add_user(self, email: str, password_hash: str) -> UserModel:
        try:
            await self.get_user_by_email(email=email)
        except QueryResultNotFoundError:
            return self._create_user(email=email, password_hash=password_hash)
        raise UserAlreadyExistsError

    def _create_user(self, email: str, password_hash: str) -> UserModel:
        user = UserModel(
            id=uuid4(),
            email=email,
            password_hash=password_hash,
        )
        self._users.insert_one(
            {
                "email": user.email,
                "password_hash": user.password_hash,
                "id": str(user.id),
            }
        )
        return user
