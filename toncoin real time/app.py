from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Faqat 4 ta valyuta
CURRENCIES = ["TONUSDT", "BTCUSDT", "ETHUSDT", "BNBUSDT"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/prices')
def prices():
    data_all = {}
    for symbol in CURRENCIES:
        try:
            url = f'https://api.binance.com/api/v3/ticker/24hr?symbol={symbol}'
            data = requests.get(url, timeout=1).json()
            data_all[symbol] = {
                "price": round(float(data["lastPrice"]), 1),
                "change": round(float(data["priceChangePercent"]), 2)
            }
        except:
            data_all[symbol] = {"price": 0, "change": 0}
    return jsonify(data_all)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
