from db.database import MongoFactory


def insert_data(data, collection) -> bool:
    mongo_instance = MongoFactory(collection=collection)
    result = mongo_instance.collection.insert_one(data.dict())
    return result.acknowledged


def update_data(query, update_values, collection) -> int:
    """sumary_line

    factory = MongoFactory('my_collection')
    update_count = factory.update_document({'name': 'John'}, {'age': 30})
    """
    mongo_instance = MongoFactory(collection=collection)
    result = mongo_instance.collection.update_many(query, {"$set": update_values})
    return result.modified_count


def fetch_data(key: str, collection):
    mongo_instance = MongoFactory(collection=collection)
    data = mongo_instance.collection.find()
    if data:
        return {"key": data["key"], "value": data["value"]}
    return None
