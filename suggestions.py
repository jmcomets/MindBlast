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

def get_suggested_products_jm(client):
    client_similarities = list(get_client_similarities(client))
    for product in Product.objects:
        client_sum = 0
        for other_client, client_score in client_similarities:
            client_sum += client_score*get_client_estimated_score(other_client, product)
        client_sum /= len(client_similarities)
        yield product, client_sum

def get_suggested_products_ahmed(client):
    scores = Counter()
    clients = Client.objects(contact_id__ne=client.contact_id)
    for c in clients:
        sim = len([att for att, val in c.boolean_attributes.items() \
                if client.boolean_attributes[att] == val])
        for f in Feedback.objects(positive=True, client=c):
            scores[f.product.product_id] += sim
    return scores

if __name__ == '__main__':
    import database
    database.connect()

    client = Client.objects().first()

    scores = get_suggested_products_ahmed(client)
    products = sorted((score, Product.objects(product_id=p_id).first()) for p_id, score in scores.iteritems())

    for score, p in products:
        print p.name
