import os
import json
from database.models import Client, Product, Feedback
from collections import Counter

def get_client_similarities(client):
    a1 = client.boolean_attributes.itervalues()
    for other_client in Client.objects(contact_id__ne=client.contact_id):
        a2 = other_client.boolean_attributes.itervalues()
        yield other_client, map(lambda x: x[0] == x[1], zip(a1, a2)).count(True)

def get_client_estimated_score(client, product):
    sum_ = 0
    client_feedbacks = client.feedbacks
    for feedback in client_feedbacks:
        if feedback.product != product:
            continue
        sum_ += 1 if feedback.positive else -1
    if client_feedbacks:
        sum_ /= len(client_feedbacks)
    return sum_

def get_suggested_products(client, force_db_load=False):
    if not force_db_load:
        cached = _get_cached_suggested_products(client)
        if cached:
            return cached
    scores = Counter()
    clients = Client.objects(contact_id__ne=client.contact_id)
    for c in clients:
        sim = len([att for att, val in c.boolean_attributes.items() \
                if client.boolean_attributes[att] == val])
        for f in Feedback.objects(positive=True, client=c):
            scores[f.product.product_id] += sim
    _cache_suggested_products(client, scores)
    return sorted(scores.items(), key = lambda e : e[1], reverse=True)

_cache_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'cache.json')
def _get_cached_suggested_products(client):
    if os.path.exists(_cache_filename):
        with open(_cache_filename, 'r') as fp:
            cache = json.load(fp)
            return cache.get(client.id)

def _cache_suggested_products(client, suggests):
    cache = {}
    if os.path.exists(_cache_filename):
        with open(_cache_filename, 'r') as fp:
            cache = json.load(fp)
    with open(_cache_filename, 'w') as fp:
        cache[str(client.id)] = suggests
        json.dump(cache, fp)

if __name__ == '__main__':
    import database
    database.connect()

    client = Client.objects().first()
    print client.boolean_attributes

    products = get_suggested_products(client)
    print products
    for p_id, score in products:
        p = Product.objects(product_id=p_id).first()
        print p.name.encode('utf-8'), score
