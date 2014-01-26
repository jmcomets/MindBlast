from database.models import Client, Product, Feedback
from collections import Counter

def get_suggested_products(client):
    scores = Counter()
    clients = Client.objects(contact_id__ne=client.contact_id)
    for c in clients:
        sim = len([att for att, val in c.boolean_attributes.items() \
                if client.boolean_attributes[att] == val])
        for f in Feedback.objects(client=c):
            scores[f.product.product_id] += sim if f.positive else -sim

    return sorted(scores.items(), key = lambda e : e[1], reverse=True)


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
