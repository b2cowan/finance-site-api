import os

from flask import Flask
from flask_cors import CORS
from tickers import test_response

app = Flask(__name__)
cors = CORS(app, origins='*')

@app.route("/api/stocks/<ticker>", methods=['GET'])
def stocks(ticker):
    stock_list = test_response(ticker) 
    return stock_list

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))