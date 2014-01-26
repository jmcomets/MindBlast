#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from flask import Flask, render_template, request
from suggestions import get_suggested_products
from database import connect as connect_to_database
from database.models import Client, Product, Feedback

app = Flask(__name__)

# connect to mongodb
connect_to_database()

@app.route('/')
def list_clients():
    c_id = request.args.get('id')
    return client_detail(c_id)

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

@app.route('/clients/reunion/finish')
def finish_reunion():
    client_id, feedbacks = request.json['client_id'], request.json['feedbacks']
    client = Client.objects(contact_id=client_id).first()
    for p_id, f in feedbacks.iteritems():
        product = Product.objects(product_id=p_id)
        if f['positive']:
            feedback = Feedback(client=client, product=product, positive=True)
        else:
            feedback = Feedback(client=client, product=product, positive=False, reason=f['reason'])

        print feedback
        # feedback.save()
        return 'ok'

#@app.route('/api/icon/<family_name>')
#def family_icon(family_name):

if __name__ == '__main__':
    app.run('0.0.0.0', port=8888,
            debug=True or '--debug' in sys.argv)
