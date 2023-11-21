from flask import Flask, request, render_template, redirect, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
import urllib.request
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

debug = DebugToolbarExtension(app)

API_ACCESS_KEY = 'c52fe9fb2cf7ab057cff11a586b02291'

def api_json(request_url):
    reesponse = urllib.request.urlopen(f'{request_url}')
    res_body = reesponse.read()
    return json.loads(res_body.decode("utf-8"))

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/convert', methods=['POST'])
def currency_converter():
    from_currency = request.form['from-currency']
    to_currency = request.form['to-currency']
    amount = request.form['amount']
    # TODO: check if currencies and amount are valid, if not flash message?

    # Construct the API endpoint URL with the access key and query parameters
    data = api_json(f'http://api.exchangerate.host/convert?access_key={API_ACCESS_KEY}&format=1&from={from_currency}&to={to_currency}&amount={amount}')

    
    converted_amount = data['result']

    return render_template('form.html', from_currency=from_currency, to_currency=to_currency, amount=amount, converted_amount=converted_amount)


