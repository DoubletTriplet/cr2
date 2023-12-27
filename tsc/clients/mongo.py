from typing import List
from pymongo import MongoClient
from pymongo.results import InsertOneResult
from tsc.models import Word
from tsc.utils.config import SETTINGS
import logging

CLIENT = MongoClient(
    f"mongodb://{SETTINGS.MONGODB_USER}:{SETTINGS.MONGODB_PASSWORD}@{SETTINGS.MONGODB_HOST}:{SETTINGS.MONGODB_PORT}"
)


async def get_word(word: str):
    """Query DB for a word document"""
    assert word
    assert len(word.split(" ")) == 1

    result: List | None = (
        CLIENT.get_database(SETTINGS.MONGODB_DATABASE)
        .get_collection(name=SETTINGS.MONGODB_COLLECTION)
        .find_one({"word": word})
    )
    logging.info('result fetched')

    return result


async def insert_word(word: Word):
    """Creates new word document in DB"""
    assert word

    result: InsertOneResult = (
        CLIENT.get_database(SETTINGS.MONGODB_DATABASE)
        .get_collection(SETTINGS.MONGODB_COLLECTION)
        .insert_one(word.model_dump())
    )
    assert result.inserted_id
    logging.info('new word persisted')


async def get_words(query: dict, skip: int, limit: int) -> List[dict]:
    """Paginated query for word collection"""
    assert query

    result = (
        CLIENT.get_database(SETTINGS.MONGODB_DATABASE)
        .get_collection(SETTINGS.MONGODB_COLLECTION)
        .find(query)
        .skip(skip)
        .limit(limit)
        .sort("word")
    )
    logging.info('result list fetched')
    return list(result)


async def delete_word(word: str) -> bool:
    """Deletes word document from DB"""
    assert word
    assert len(word.split(" ")) == 1

    result = (
        CLIENT.get_database(SETTINGS.MONGODB_DATABASE)
        .get_collection(SETTINGS.MONGODB_COLLECTION)
        .delete_one({"word": word})
    )
    logging.info('result deleted')

    return result.deleted_count > 0
