from scripts.config import MongoDB
from pymongo import MongoClient

mongo_client = MongoClient(MongoDB.uri)