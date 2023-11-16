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
            {"_id": 0, "template_name": 0}
        )
        return res

    @LOGER.catch
    async def get_template(self, data: dict) -> str | None:
        """Returning the closest matching document and added new document"""
        existing_values = []
        for key, value in data.items():
            if self.collection.find_one({key: value}):
                existing_values.append({"$and": [{key: value}]})
        if len(existing_values) > 0:
            query = {"$or": existing_values}
            LOGER.info(f"query = {query}")
            rows = self.collection.find(query, {"_id": 0})
            res = {}
            for row in rows:
                row_name = row.get("template_name")
                row.pop("template_name")
                flag = True
                if len({**row, **data}) == len(data):
                    for key in row.keys():
                        if row.get(key) != data.get(key):
                            flag = False
                    row["template_name"] = row_name
                    if flag is True and len(res) < len(row):
                        res = row
            if len(res):
                return res.get("template_name")
        return None

    @LOGER.catch
    async def get_all_templates_with_page(
            self,
            page_number: int,
            page_size: int
    ) -> dict:
        """Returning all documents from collection"""
        res = {"templates": []}
        a = self.collection.find().skip((page_number - 1) * page_size).limit(page_size)
        for item in a:
            res["templates"].append(item)
        return res
