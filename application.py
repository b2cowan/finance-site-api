from flask import Flask
from flask_cors import CORS
from tickers import test_response

application = Flask(__name__)
cors = CORS(application, origins='*')

@application.route("/api/stocks/<ticker>", methods=['GET'])
def stocks(ticker):
    stock_list = test_response(ticker) 
    return stock_list

if __name__ == "__main__":
    application.run(debug=True, port=8080)