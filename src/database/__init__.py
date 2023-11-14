"""Connect to MongoDB"""

import pymongo

from settings import MONGO_USER, MONGO_PASS, MONGO_URL

client = pymongo.MongoClient(
    host=f"{MONGO_URL}",
    username=MONGO_USER,
    password=MONGO_PASS
)

mydb: pymongo.mongo_client.database.Database = client.leadhit
handbook_collection: pymongo.collection.Collection = mydb.handbook
