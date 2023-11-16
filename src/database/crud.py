"""CRUD operations to MongoDB"""

import bson

from bson import ObjectId

from src.database import handbook_collection as hb
from settings import LOGER


class HandBook:
    """CRUD operations for HandBook repository"""
    def __init__(self):
        self.collection = hb

    @LOGER.catch
    async def insert(self, data: dict) -> ObjectId:
        """Insert data to HandBook collection"""
        count = self.collection.count_documents({})
        data["template_name"] = f"Template №{count}"
        post_id = self.collection.insert_one(data).inserted_id
        return post_id

    @LOGER.catch
    async def get_template_by_id(self, obj_id: bson.ObjectId) -> dict:
        """Returning template name by _id"""
        res = self.collection.find_one(
            {"_id": obj_id},
            {"_id": 0, "template_name": 1}
        )
        return res

    @LOGER.catch
    async def get_template(self, data: dict) -> str | None:
        """Returning the closest matching document and added new document"""
        existing_values = []
        final_query = {}
        for key, value in data.items():
            if self.collection.find_one({key: value}):
                existing_values.append({key: value})
            LOGER.info(f"Ищем ключ и значение в бд {key}, {value}")
        LOGER.info(f"Искомые поля: {existing_values}")
        for i in range(len(existing_values)):
            if i == len(existing_values) - 1:
                break
            query = existing_values[i]
            for k in range(len(existing_values[i:])):
                if self.collection.find_one({**query, **existing_values[k]}):
                    query = {**query, **existing_values[k]}
                else:
                    continue
            if len(final_query) < len(query):
                final_query = query
            LOGER.info(f"Финальный запрос каждой интерации {query}")
        res = self.collection.find_one(
            final_query,
            {"_id": 0, "template_name": 1}
        )
        if len(data) > len(existing_values):
            await self.insert(data)
            return res
        return res

    @LOGER.catch
    async def get_all_templates(self) -> dict:
        """Returning all documents from collection"""
        res = {"templates": []}
        a = self.collection.find()
        for item in a:
            res["templates"].append(item)
        return res
