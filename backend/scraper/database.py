from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client['componentsDB']
collection = db['components_data']

#maybe create hash key when saving to db combining name with date scraped
#so that if already current data > scraped date by 10 days, then scrape is ran again, otherwise return with what is already saved to db


def get_from_db(data):
    records = list(collection.find({}, {"_id": 1, "url": 1, "titles": 1, "timestamp": 1}))
    return [
        {"id": str(record["_id"]), "url": record["url"], "titles": record["titles"], "timestamp": record["timestamp"]}
        for record in records
    ]


def save_to_db(data):
    if "error" in data:
        print(f"Error saving data for {data.get('url')}: {data['error']}")
        return

    data['timestamp'] = datetime.now()
    collection.insert_one(data)
    print(f"Data saved for {data['url']}")