from flask import *
import json
import requests
from web3 import Web3, HTTPProvider

with open('contract/abi.json') as f:
    abi = json.load(f)
with open('contract/address.txt') as f:
    address = f.read()

url= 'https://sandbox.truffleteams.com/8f7572d1-e253-420a-93bc-2ed8a6f051e6'
w3 = Web3(HTTPProvider(url))
w3.eth.default_account = w3.eth.accounts[0]
c = w3.eth.contract(abi=abi, address=address)

app = Flask(__name__)

@app.route('/<parent>', methods=['POST', 'GET'])
def index(parent):
    if request.method == 'POST':
        data = request.form
        c.functions.store(
            data['message'], 
            parent
        ).transact()

    else:
        pass

    event_filter = c.events.post.createFilter(
        fromBlock=0, 
        argument_filters=dict(
            parent=parent
        )
    )
    entries = event_filter.get_all_entries()

    return render_template(
        'index.html',
        entries=entries
    )

app.run(port=8080, debug=True)