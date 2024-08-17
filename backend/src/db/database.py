from pymongo import MongoClient

class MongoFactory:
    def __init__(self, collection) -> None:
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['rootsearch_db']
        self.collection = self.db[collection]
