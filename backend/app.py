from flask import Flask, request, jsonify
from flask_cors import CORS
from scraper.scraper import scrape
from scraper.database import save_to_db, get_from_db, check_in_db
from scraper.config import SCRAPE_URLS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["https://net-component-scraper.vercel.app", "http://localhost:3000"]}})

""" client = MongoClient('localhost', 27017)

db = client.netComponents_db
netComponents = db.netComponents """

def run_scraper(searchQuery):
    searchQuery = searchQuery.strip()
    isAlreadyInDB = check_in_db(searchQuery)
    if (isAlreadyInDB == True):
        get_from_db(searchQuery)
    else:
        result = scrape(searchQuery)
    return result


@app.route('/api/search', methods=['GET'])
def search():
    searchQuery = request.args.get('q')
    print(f"Received search query: {searchQuery}")
    data = run_scraper(searchQuery)

    results = {
        "searchQuery": searchQuery,
        "data": data
        }
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, port=8000)


