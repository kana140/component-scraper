from flask import Flask, request, jsonify
import requests, bs4
import lxml #faster parser than lxml

app = Flask(__name__)

@app.route('/api/search')
def home():
    data = request.get_json()  # Parse JSON from the frontend
    print(f"Received data: {data}")
    return jsonify({'message': 'Data received', 'received_data': data})
if __name__ == '__main__':
    app.run(debug=True, port=5000)


""" @app.route('/search')
def search(searchTerm):
    res = requests.get('https://www.netcomponents.com/demo/result?pn1=' + searchTerm)
    try:
        res.raise_for_status()
    except Exception as exc:
        print('There was a problem: $s' % (exc))
    yummySoup = bs4.BeautifulSoup(res.text, 'lxml')
    rowElems = yummySoup.select('tr')
    jsonResult = 'blah'
    return jsonResult """
