from flask import Flask, render_template, redirect, flash, request
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyCodes

import requests

app = Flask(__name__)

# Configure Flask Debug Toolbar
app.config['SECRET_KEY'] = 'my_secret_key'

app.config['DEBUG'] = True
app.config['DEBUG_TB_ENABLED'] = True

# Create an instance of the DebugToolbarExtension
toolbar = DebugToolbarExtension(app)

@app.route('/home')
def intro_page():
    return render_template('base.html') 

@app.route('/home', methods=['POST'])
def convert():
    fromcurr = request.form['fromcurr']
    tocurr = request.form['tocurr']
    convert = f"{fromcurr}{tocurr}"
    response = requests.get('http://api.exchangerate.host/live?access_key=7f7872a5d79ca6a2cdf707cd2a33bdf6')
    response2 = requests.get('https://api.exchangerate.host/list?access_key=7f7872a5d79ca6a2cdf707cd2a33bdf6')
    data = response.json()
    data2 = response2.json()
    if not fromcurr in data2['currencies'].keys():
        return render_template('base.html', message = f'From currency is not a valid currency ==>{fromcurr}') 
    if not tocurr in data2['currencies'].keys():
        return render_template('base.html', message = f'To currency is not a valid currency ==>{tocurr}') 
    try:
        fromamt = float(request.form['fromamt'])
    except ValueError:
        return render_template('base.html', message = f'Amount is not a valid number')
    if not convert in data['quotes'].keys():
        return render_template('base.html', message = f'No exchange rate from {fromcurr} to {tocurr}')
    toamount = fromamt * data['quotes'][convert]
    c = CurrencyCodes()
    symbol = c.get_symbol(tocurr)
    return render_template('base.html', symbol = symbol, toamount = round(toamount,2)) 
