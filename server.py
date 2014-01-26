import sys
from flask import Flask, render_template
from suggestions import get_suggested_products
from database import connect as connect_to_database
from database.models import Client

app = Flask(__name__)

# connect to mongodb
connect_to_database()

@app.route('/')
def index():
    clients = Client.objects()[:10]
    return render_template('index.html', clients=clients)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/meeting')
def meeting():
    return render_template('meeting.html')

@app.route('/api/suggestions/<contact_id>/products')
def suggested_products(contact_id):
    client = Client.objects(contact_id=contact_id)
    # TODO handle errors
    suggestions = get_suggested_products(client)
    return '<br>'.join(map(lambda x: x[0] + ':' + x[1], suggestions))

if __name__ == '__main__':
    app.run('0.0.0.0', port=8888,
            debug=True or '--debug' in sys.argv)
