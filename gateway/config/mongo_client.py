from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["api_gateway"]

def get_user_config(api_key):
    return db.users.find_one({"api_key": api_key})

def get_user_config_by_id(user_id):
    return db.users.find_one({"user_id": user_id})

def get_global_limiter_config():
    return db.global_config.find_one({"name": "default"})
