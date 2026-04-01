import json  # noqa: F401
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from pymongo import MongoClient
from bson import ObjectId  # noqa: F401

DATA_DIR = Path(__file__).parent / "data"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env.secret", extra="ignore")

    user: str = Field(..., alias="MONGO_USER")
    password: str = Field(..., alias="MONGO_PASSWORD")
    host_port: int = Field(..., alias="MONGO_HOST_PORT")
    db: str = Field(..., alias="MONGO_DB")


settings = Settings()  # type: ignore[reportCallIssue]


def get_db():
    client = MongoClient(
        f"mongodb://localhost:{settings.host_port}/",
        username=settings.user,
        password=settings.password,
    )
    return client[settings.db]


# Exercise 1: Insert the single object and multiple objects using one function.
# Data: data/ex1/data-single-object.json, data/ex1/data-multiple-objects.json
def insert_operation(db):
    raise NotImplementedError


# Exercise 2: Implement three queries:
# - Find all sales where the sale date is in 2024.
# - Find all sales where the customer satisfaction rating >= 3.
# - Find all sales where the customer satisfaction rating was 5 and a coupon was used.
def find_operation(db):
    raise NotImplementedError


# Exercise 3: Implement two deletions:
# - Delete the object with id = "5bd761dcae323e45a93ccff4".
# - Delete all documents where the store location is "Seattle" and coupon is "not used".
def delete_operation(db):
    raise NotImplementedError


# Exercise 4:
# - Update the customer satisfaction to 4 and couponUsed to true,
#   where the id equals "5bd761dcae323e45a93ccff3".
def update_operation(db):
    raise NotImplementedError


if __name__ == "__main__":
    db = get_db()
    insert_operation(db)
    find_operation(db)
    delete_operation(db)
    update_operation(db)
