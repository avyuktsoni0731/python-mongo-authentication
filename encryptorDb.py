import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
mongodb_uri = os.getenv('MONGODB_URI')

client = MongoClient(mongodb_uri)

db = client['encryptionDb']
collection = db['encryptionData']
