from database.models import Client, Product

def get_client_similarities(client):
    a1 = client.boolean_attributes
    for other_client in Client.objects(contact_id__ne=client.contact_id):
        a2 = other_client.boolean_attributes
        yield other_client, map(lambda x: x[0] == x[1], zip(a1, a2)).count(True)

def get_client_estimated_score(client, product):
    sum_ = 0
    client_feedbacks = client.reunions.feedbacks
    for feedback in client_feedbacks:
        if product not in feedback:
            continue
        sum_ += 1 if feedback.positive else -1
    sum_ /= len(client_feedbacks)
    return sum_

def get_suggested_products(client):
    client_similarities = get_client_similarities(client)
    for product in Product.objects:
        client_sum = 0
        for other_client, client_score in client_similarities:
            client_sum += get_client_estimated_score(other_client, product)
        client_sum /= len(client_similarities)
        yield product, client_sum
