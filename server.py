import sys
from flask import Flask, render_template
from suggestions import get_suggested_products
from database import connect as connect_to_database
from database.models import Client, Product

app = Flask(__name__)

# connect to mongodb
connect_to_database()

@app.route('/')
def list_clients():
    return render_template('list_clients.html', clients=Client.objects)

@app.route('/clients/<client_id>')
def client_detail(client_id):
    client = Client.objects.get(id=client_id)
    suggestions = sorted(get_suggested_products(client), key=lambda x: x[1], reverse=True)
    recommendations = filter(lambda x: x[1] > 0.7, suggestions)
    risqued = filter(lambda x: x[1] < 0.3, suggestions)
    return render_template('client_detail.html', **locals())

@app.route('/clients/reunions/<client_id>')
def meeting(client_id):
    client = Client.objects(contact_id=client_id).first()
    # DEBUG ONLY
    products = Product.objects()[:10]
    return render_template('meeting.html', client=client, products=products)


#@app.route('/api/icon/<family_name>')
#def family_icon(family_name):

if __name__ == '__main__':
    app.run('0.0.0.0', port=8888,
            debug=True or '--debug' in sys.argv)
