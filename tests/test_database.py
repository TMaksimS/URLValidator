from src.database.crud import HandBook
from src.database import handbook_collection

collection = HandBook()
base_data = {
    "lead_email": "email",
    "mobile": "phone",
    "birthday": "date",
    "description": "text"
}


class TestHandBook:
    async def test_insert(self):
        assert await collection.insert(data=base_data) == handbook_collection.find_one(base_data).get(
            "_id")

    async def test_get_template_by_id(self):
        obj = handbook_collection.find_one(base_data)
        obj_id = obj.get("_id")
        obj.pop("_id")
        obj.pop("template_name")
        assert await collection.get_template_by_id(obj_id) == obj
