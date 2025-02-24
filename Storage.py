from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.chat_db
collection = db.interactions

def store_interaction(user_text, response):
    collection.insert_one({"user_input": user_text, "response": response})
