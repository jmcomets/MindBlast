from mongoengine import Document, fields
import sys
sys.path.insert(0,'..')
from settings import *
import beatbox

svc = beatbox.PythonClient()
svc.login(login, password + token)

class LazySforceDocument(object):
    sforce_klass = None
    sforce_id_attr = None
    attributes = []

    def __getattribute__(self, attr):
        try:
            return super(LazySforceDocument, self).__getattribute__(attr)
        except AttributeError:
            if attr not in self.attributes:
                raise AttributeError
            if not hasattr(self, '_cached_time') or not self._cached_time:
                query = "select %s from %s where Id='%s'" \
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

    def __init__(self,id, *args, **kwargs):
        super(Product, self).__init__(*args, **kwargs)
        self._cache = None
        self.product_id=id


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

class discount(Document):
    products = fields.ListField(fields.ReferenceField(Product))
    description = fields.StringField(required=True)

if __name__ == '__main__':
    client = Client("003b000000KqjPVAAZ")
    print client.Name
   # Product.object.get()
    # with open("../contacts.txt",'r') as file:
    #     p = Product(file.readline().strip('\r\n'))
