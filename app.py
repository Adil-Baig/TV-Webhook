# import logbot
import json, config , os
from flask import Flask, request
# from orderapi import order

app = Flask(__name__)
app.config["DEBUG"] = True
@app.route("/")
def hello_trader():
    return "<p>Hello young trader!</p>"

@app.route("/tradingview-to-webhook-order", methods=['POST'])
def tradingview_webhook():
    data = json.loads(request.data)

    webhook_passphrase = os.environ.get('WEBHOOK_PASSPHRASE', config.WEBHOOK_PASSPHRASE)
    if 'passphrase' not in data.keys():
        return {
            "success": False,
            "message": "no passphrase entered"
        }

    if data['passphrase'] != webhook_passphrase:
        return {
            "success": False,
            "message": "invalid passphrase"
        }
    
    price = data['strategy']['price']+10
    message = data['strategy']['message']
    passphrase = data['strategy']['passphrase']
    return {
        'price' : price,
        'message' : message,
        'passphrase': passphrase,
        'code': 'success',
        'passphrase': webhook_passphrase
    }