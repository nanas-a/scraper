from pymongo import MongoClient


def connect():
    client = MongoClient('mongodb://nasri:UtyCantik12@103.187.146.135:27017/')
    db = client['Stockers']
    collection = db['Media']
    return client, collection
