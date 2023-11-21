from flask import Flask, request, render_template, redirect, session, jsonify, flash
from flask_debugtoolbar import DebugToolbarExtension
import urllib.request
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

debug = DebugToolbarExtension(app)

API_ACCESS_KEY = 'c52fe9fb2cf7ab057cff11a586b02291'

def api_json(request_url):
    response = urllib.request.urlopen(f'{request_url}')
    res_body = response.read()
    return json.loads(res_body.decode("utf-8"))

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/convert', methods=['POST'])
def currency_converter():
    from_currency = request.form['from-currency']
    to_currency = request.form['to-currency']
    amount = request.form['amount']

    if not is_valid_currency(from_currency):
        flash(f'{ from_currency } is not a valid currency code.')
        return render_template('form.html', from_currency=from_currency, to_currency=to_currency, amount=amount)

    if not is_valid_currency(to_currency):
        flash(f'{ to_currency } is not a valid currency code.')
        return render_template('form.html', from_currency=from_currency, to_currency=to_currency, amount=amount)

    if not is_valid_amount(amount):
        flash(f'{ amount } is not a valid amount.')
        return render_template('form.html', from_currency=from_currency, to_currency=to_currency, amount=amount)
    
    # Construct the API endpoint URL with the access key and query parameters
    data = api_json(f'http://api.exchangerate.host/convert?access_key={API_ACCESS_KEY}&format=1&from={from_currency}&to={to_currency}&amount={amount}')

    converted_amount = round(data['result'], 2)

    return render_template('form.html', from_currency=from_currency, to_currency=to_currency, amount=amount, converted_amount=converted_amount)

def is_valid_currency(currency):
    data = api_json(f'http://api.exchangerate.host/list?access_key={API_ACCESS_KEY}')
    if currency in data['currencies']:
        return True
    else:
        return False

def is_valid_amount(num):
    if int(num) <= 0:
        return False
    else:
        return True