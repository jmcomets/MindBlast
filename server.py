import sys
import beatbox
from flask import Flask, render_template
from suggestions import (get_suggested_products_jm, get_suggested_products_ahmed)
from database import connect as connect_to_database
from database.models import Client

app = Flask(__name__)

# connect to mongodb
connect_to_database()

@app.route('/')
def list_clients():
    return render_template('list_clients.html', clients=Client.objects)

@app.route('/<client_id>')
def client_detail(client_id):
    client = Client.objects.get(id=client_id)
    suggestions = sorted(get_suggested_products_jm(client), key=lambda x: x[1], reverse=True)
    recommendations = filter(lambda x: x[1] > 0.7, suggestions)
    risqued = filter(lambda x: x[1] < 0.3, suggestions)
    return render_template('client_detail.html', **locals())

@app.route('/api/suggestions/<contact_id>/products')
def suggested_products(contact_id):
    client = Client.objects(contact_id=contact_id)
    # TODO handle errors
    suggestions = get_suggested_products(client)
    return '<br>'.join(map(lambda x: x[0] + ':' + x[1], suggestions))

@app.route('/<client_id>/reunion')
def meeting():
    client = Client.objects.get(id=client_id)
    products = [s[0] for s in sorted(get_suggested_products_jm(client), key=lambda x: x[1])]
    return render_template('meeting.html', **locals())

#@app.route('/api/icon/<family_name>')
#def family_icon(family_name):

if __name__ == '__main__':
    app.run('0.0.0.0', port=8888,
            debug=True or '--debug' in sys.argv)
