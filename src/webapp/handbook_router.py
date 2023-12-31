"""HandBook endpoints"""

import json
from bson import json_util

from fastapi import APIRouter, Request, HTTPException

from settings import LOGER
from src.database.crud import HandBook
from src.database.validator import Validator

app = APIRouter(prefix="/hb", tags=["handbooks"])


@LOGER.catch
@app.post("/")
async def create_template(data: dict) -> dict:
    """Endpoint created new templates"""
    db = HandBook()
    res = await db.insert(data)
    return json.loads(json_util.dumps({
        "msg": "Object has been added",
        "_id": res
    }))


@LOGER.catch
@app.get("/all")
async def get_all_items(page: int = 1, page_size: int = 10) -> dict:
    """Endpoint provides all Templates from DB"""
    db = HandBook()
    res = await db.get_all_templates_with_page(page, page_size)
    return json.loads(json_util.dumps(res))


@LOGER.catch()
@app.post("/get_form")
async def get_form(req: Request) -> str | dict:
    """Endpoint provides the closest template, if available"""
    collection = HandBook()
    try:
        req_query = await Validator.parce(req.url.query)
        LOGER.info(f"request_query {req_query}")
    except IndexError:
        raise HTTPException(
            status_code=400,
            detail="Bad Request"
        )
    for key, value in req_query.items():
        req_query[key] = await Validator(value).validate()
    data_db = await collection.get_template(req_query)
    if data_db:
        return data_db
    await collection.insert(req_query)
    req_query.pop("_id")
    req_query.pop("template_name")
    return json.loads(json_util.dumps(req_query))
