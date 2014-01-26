from mongoengine import Document, fields
import sys
sys.path.insert(0,'..')
from settings import *
import beatbox

import database
database.connect()

svc = beatbox.PythonClient()
svc.login(login, password + token)

class LazySforceDocument(object):
    sforce_klass = None
    sforce_id_attr = None
    attributes = []
    _cache = {}

    def __getattribute__(self, attr):
        try:
            return super(LazySforceDocument, self).__getattribute__(attr)
        except AttributeError as e:
            if attr not in self.attributes:
                raise e

        if self._cache:
            return self._cache[attr]

        query = "SELECT %s FROM %s WHERE Id='%s'" \
            % (', '.join(self.attributes),
                self.sforce_klass,
                getattr(self, self.sforce_id_attr))

        res = svc.query(query)
        if not res:
            raise ValueError("No entries for given ID")

        self._cache = res[0]
        return self._cache[attr]

class Product(Document, LazySforceDocument):
    product_id = fields.StringField(unique=True)
    sforce_klass = 'Product2'
    sforce_id_attr = 'product_id'
<<<<<<< HEAD
=======

    def __init__(self,id, *args, **kwargs):
        super(Product, self).__init__(*args, **kwargs)
        self._cache = None
        self.product_id=id


>>>>>>> df1a637b89454693fa9f66f85255313f1f4aee07
    attributes = svc.describeSObjects(sforce_klass)[0].fields.keys()



class Client(Document, LazySforceDocument):
    sforce_klass = 'Contact'
    sforce_id_attr = 'contact_id'


    contact_id = fields.StringField(required=True, unique=True)
    has_car = fields.BooleanField(default=False)
    has_child = fields.BooleanField(default=False)
    is_married = fields.BooleanField(default=False)
    is_owner = fields.BooleanField(default=False)

    attributes = svc.describeSObjects(sforce_klass)[0].fields.keys()
    # ['OtherStreet',
    #  'MailingPostalCode',
    #  'ReportsToId',
    #  'MasterRecordId',
    #  'FirstName',
    #  'Title',
    #  'mindblast__Level__c',
    #  'LastName',
    #  'LastModifiedById',
    #  'EmailBouncedReason',
    #  'Department',
    #  'OwnerId',
    #  'MailingState',
    #  'AssistantPhone',
    #  'Fax',
    #  'Description',
    #  'LastModifiedDate',
    #  'AssistantName',
    #  'Email',
    #  'Phone',
    #  'CreatedById',
    #  'MailingCity',
    #  'LastCURequestDate',
    #  'IsDeleted',
    #  'OtherPostalCode',
    #  'MailingStreet',
    #  'OtherCountry',
    #  'Name',
    #  'EmailBouncedDate',
    #  'MailingCountry',
    #  'Birthdate',
    #  'LeadSource',
    #  'OtherState',
    #  'MobilePhone',
    #  'LastActivityDate',
    #  'OtherCity',
    #  'LastCUUpdateDate',
    #  'SystemModstamp',
    #  'mindblast__Languages__c',
    #  'CreatedDate',
    #  'Salutation',
    #  'AccountId',
    #  'OtherPhone',
    #  'Id',
    #  'HomePhone']


    @property
    def boolean_attributes(self):
        return {"has_car": self.has_car, "has_child": self.has_child, "is_married": self.is_married, "is_owner": self.is_owner}

class Feedback(Document):
    positive = fields.BooleanField(required=True)
    reason = fields.StringField()
    client = fields.ReferenceField(Client)

class Meetings(Document):
    date = fields.DateTimeField(required=True)
    client = fields.ReferenceField(Client, required=True)
    feedbacks = fields.ListField(fields.ReferenceField(Feedback))

class Challenge(Document):
    title = fields.StringField()
    contract = fields.ReferenceField(Product)
    current_value = fields.IntField()
    max_value = fields.IntField()
    description = fields.StringField()

    @property
    def progress(self):
        return float(self.current_value) / float(self.max_value)

class Discount(Document):
    products = fields.ListField(fields.ReferenceField(Product))
    description = fields.StringField(required=True)

class OffreCommerciale(Document):
    products = fields.ListField(fields.ReferenceField(Product), required=True)
    description = fields.StringField(required=True)


if __name__ == '__main__':
    print Client.objects()
    client = Client("003b000000KqjPVAAZ")
    print client.Name
    # with open("../contacts.txt",'r') as file:
    #     p = Product(file.readline().strip('\r\n'))
