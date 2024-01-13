# import json
# import pandas as pd
# from pymongo import MongoClient
# from bson import ObjectId

# uri = "mongodb://nasri:UtyCantik12@103.187.146.135:27017/"

# client = MongoClient(uri)
# db = client['Stockers']
# collection = db['ListStock']

# # Load Excel file into DataFrame
# df = pd.read_excel('Daftar Saham 20240111.xlsx')

# # Convert DataFrame to JSON
# json_data = df.to_dict(orient='records')

# result = [{**data, **{'_id': str(ObjectId())}} for data in json_data]

# collection.insert_many(result)
