import random
import pprint
from faker import Factory
import beatbox
from settings import *

pprint.pprint('Logging in to salesforce')
svc = beatbox.PythonClient()
svc.login(login, password + token)

fake = Factory.create()

def random_phone(is_mobile):
    prefix = '+33 %s' % (random.randint(6, 7) if is_mobile else random.randint(1, 5))
    return prefix + ''.join(str(random.choice(range(10))) for _ in xrange(8))

file_ = open('contacts.txt', 'a')

nb_data = 100
for _ in xrange(nb_data):
    contact = {
            'type': 'Contact',
            'Email': fake.email(),
            'FirstName': fake.first_name(),
            'LastName': fake.last_name(),
            'Description': fake.text(),
            'Phone': random_phone(False),
            'MobilePhone': random_phone(True),
            'HomePhone': random_phone(False),
            'MailingCity': fake.city(),
            'MailingCountry': 'France',
            'MailingPostalCode': fake.postcode().split('-')[0],
            'MailingStreet': fake.street_address(),
            }
    pprint.pprint('Creating contact %s' % contact)
    created_contact = svc.create(contact)[0]
    if created_contact['success']:
        pprint.pprint('Created contact %s' % created_contact)
        file_.write('%s\n' % created_contact['id'])
    else:
        pprint.pprint('An error occurred!')
file_.close()
