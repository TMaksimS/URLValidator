"""CRUD operations to MongoDB"""

from bson import ObjectId

from src.database import handbook_collection as hb


class HandBook:
    """CRUD operations for HandBook repository"""
    def __init__(self):
        self.collection = hb

    async def insert(self, data) -> ObjectId:
        """Insert data to HandBook collection"""
        post_id = self.collection.insert_one(data).inserted_id
        return post_id

    async def get(self, data: dict) -> dict:
        """Get documents"""
        post_id = self.collection.find_one(data)
        return post_id
