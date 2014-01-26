#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import datetime
from flask import Flask, render_template, request
from suggestions import get_suggested_products
from database import connect as connect_to_database
from database.models import Client, Product, Feedback, Reunion

app = Flask(__name__)

# connect to mongodb
connect_to_database()

@app.route('/')
def index():
    return client_detail('003b000000KqjT8AAJ')

@app.route('/list')
def list_clients():
    clients = Client.objects()
    return render_template('list_clients.html', clients=clients)

@app.route('/clients/<client_id>')
def client_detail(client_id):
    client = Client.objects.get(contact_id=client_id)

    # suggestions
    raw_suggestions = get_suggested_products(client)
    suggestions = map(lambda x: (Product.objects.get(product_id=x[0]), x[1]), raw_suggestions)
    magic_number = 4
    recommendations = map(lambda x: x[0], suggestions[magic_number:])
    risqued = []
    sum_ = 0
    for sugg in suggestions[:-magic_number]:
        if sugg[0] in recommendations:
            continue
        risqued.append(sugg)
    max_abs = max(map(lambda x: abs(x[1]), risqued))
    risqued = map(lambda x: (x[0], 0.2 + 0.7*abs(x[1])/float(2*max_abs)), risqued)
    print recommendations
    print risqued

    # meetings
    all_meetings = client.reunions
    scheduled_meetings = [x for x in all_meetings if x.date() > datetime.datetime.now()]
    passed_meetings = [x for x in all_meetings if x not in scheduled_meetings]
    return render_template('client_detail.html', **locals())

@app.route('/clients/reunions/<client_id>')
def meeting(client_id):
    client = Client.objects.get(contact_id=client_id)
    # DEBUG ONLY
    products = Product.objects()[:5]
    return render_template('meeting.html', client=client, products=products)

@app.route('/clients/reunion/finish', methods=['POST'])
def finish_reunion():
    client_id, feedbacks = request.json['client_id'], request.json['feedbacks']
    client = Client.objects.get(contact_id=client_id)
    for p_id, f in feedbacks.iteritems():
        product = Product.objects.get(product_id=p_id)
        if f['positive']:
            feedback = Feedback(client=client, product=product, positive=True)
        else:
            feedback = Feedback(client=client, product=product, positive=False, reason=f['reason'])

        print feedback.positive, feedback.client.name
        # feedback.save()
    return 'ok'

@app.route('/clients/reunion/<reunion_id>')
def reunion_detail(reunion_id):
    return render_template('reunion.html', reunion=Reunion.objects.get(id=reunion_id))

#@app.route('/api/icon/<family_name>')
#def family_icon(family_name):

if __name__ == '__main__':
    app.run('0.0.0.0', port=8888,
            debug=True or '--debug' in sys.argv)
