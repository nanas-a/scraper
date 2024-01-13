from config.mongo import connect as mongo_connect


def validate_title(title: str):
    client, collection = mongo_connect()
    with client:
        return collection.find_one({'title': title}) is None
