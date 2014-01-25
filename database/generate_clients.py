import sys
import random
sys.path.insert(0,'..')
import mongoengine
from models import Client
from settings import db_name

probas = {
    'has_car': 0.7,
    'has_child': 0.45,
    'is_married': 0.45,
    'is_owner': 0.3,
    }

with open('contacts.txt', 'r') as fp:
    clients = map(lambda l: {
        'has_car': False,
        'has_child': False,
        'is_married': False,
        'is_owner': False,
        'contact_id':l.strip('\r\n')
        }, fp.readlines())

for pk, p in probas.iteritems():
    random.shuffle(clients)
    for i in xrange(0, int(p*len(clients))):
        clients[i][pk] = True
random.shuffle(clients)

mongoengine.connect('mindblast')
for c in clients:
    Client(**c).save()
