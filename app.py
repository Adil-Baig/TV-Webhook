# import logbot
import json #, os, config
from flask import Flask, request
# from orderapi import order

app = Flask(__name__)

@app.route("/")
def hello_trader():
    return "<p>Hello young trader!</p>"

@app.route("/tradingview-to-webhook-order", methods=['POST'])
def tradingview_webhook():
    data = json.loads(request.data)
    price = data['strategy']['price']+2
    message = data['strategy']['message']
    passphrase = data['strategy']['passphrase']
    return {
        'price' : price,
        'message' : message,
        'passphrase': passphrase,
        'code': 'success'
    }
# from flask import Flask
# app=Flask(__name__)

# @app.route("/")
# def home():
#     return "Hello, World!"

# @app.route("/webhook")
# def webhook():
#     return "Webhook Route"