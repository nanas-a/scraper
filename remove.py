from config.mongo import connect as mongo_connect

client, collection = mongo_connect()
with client:
    collection.delete_many({})
