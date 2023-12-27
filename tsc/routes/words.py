from fastapi import APIRouter, HTTPException, status
from typing import Optional
from tsc.clients import mongo, google_translation
from tsc.models import Word
import logging

router = APIRouter(prefix="/word", tags=["Translation"])


@router.get("", status_code=status.HTTP_200_OK)
async def list_words(
    filter_word: str,
    skip: int = 0,
    limit: int = 10,
):
    query = {}
    if not filter_word:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Filter word required")
    query["word"] = {"$regex": filter_word, "$options": "i"}

    result = await mongo.get_words(query, skip, limit)

    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    logging.info('[GET] - /word - result returned')
    return [Word(**word) for word in result]


@router.get("/{word}", status_code=status.HTTP_200_OK)
async def get_word(
    word: str,
):
    stored_word = await mongo.get_word(word=word)

    if stored_word:
        logging.info(f'[GET] - /word/{word} - result already exists')
        result = stored_word
        return Word(**result)
    
    result = await google_translation.translate_word(word)
    logging.info(f"{word} word translated")

    result = Word(
        word=word,
        definitions=result.extra_data['definitions'],
        synonyms=result.extra_data['synonyms'],
        examples=result.extra_data['examples'],
        translations=result.extra_data['translation']
    )
    await mongo.insert_word(result)
    return result.model_dump_json()


@router.delete("/{word}", status_code=status.HTTP_202_ACCEPTED)
async def delete_word(word: str):
    result = await mongo.delete_word(word)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Word not found"
        )
    return {"status": "Word deleted"}
