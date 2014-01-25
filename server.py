import sys
import beatbox
from flask import Flask
from suggestions import get_suggested_products_jm as get_suggested_products
#from suggestions import get_suggested_products_ahmed as get_suggested_products
from database import connect as connect_to_database
from database.models import Client

app = Flask(__name__)

# connect to mongodb
connect_to_database()

# fix for index page
@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/meeting')
def meeting():
    return app.send_static_file('meeting.html')

@app.route('/api/suggestions/<contact_id>/products')
def suggested_products(contact_id):
    client = Client.objects(contact_id=contact_id)
    # TODO handle errors
    suggestions = get_suggested_products(client)
    return '<br>'.join(map(lambda x: x[0] + ':' + x[1], suggestions))

if __name__ == '__main__':
    app.run('0.0.0.0', port=8888,
            debug=True or '--debug' in sys.argv)
