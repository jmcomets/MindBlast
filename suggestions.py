import itertools as it
from database.models import Client

def get_client_similarities(client):
    a1 = client.boolean_attributes
    for other_client in Client.objects.filter(id__ne=client.id)
        a2 = other_client.boolean_attributes
        score = sum(it.imap(lambda x: float((x[0]+1)*x[0]), it.compress(a1, a2)))
        score /= len(a2)*(len(a2)+1)/2
        yield other_client, score

def get_suggested_products(client):
    client_similarities = get_client_similarities(client)
    pass # TODO
