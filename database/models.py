from mongoengine import Document, fields
import sys
sys.path.insert(0,'..')
from settings import *
import beatbox

class Product(Document):
    product_id = fields.StringField(unique=True)

    def __init__(self,id, *args, **kwargs):
        super(Product, self).__init__(*args, **kwargs)
        self._cache = None
        self.svc = beatbox.PythonClient()
        self.svc.login(login, password + token)
        self.product_id=id

    @property
    def name(self):
        if self._cache is None:
            attributes = self.svc.describeSObjects('Contact')[0].fields.keys()
            self._cache={}
            key=attributes[0]
           # print self.svc.query('select {} from Contact where id = {}'.format(key,self.product_id))#self._cache[key]=(self.svc.query("select "+str(key) + " from contact"))

class Client(Document):
    contact_id = fields.StringField(required=True, unique=True)
    has_car = fields.BooleanField(default=False)
    has_child = fields.BooleanField(default=False)
    is_married = fields.BooleanField(default=False)
    is_owner = fields.BooleanField(default=False)

    @property
    def boolean_attributes(self):
        return {"has_car": self.has_car, "has_child": self.has_child, "is_married": self.is_married, "is_owner": self.is_owner}




class Feedback(Document):
    positive = fields.BooleanField(required=True)
    reason = fields.ListField(fields.StringField, default=[])
    client = fields.ReferenceField(Client)

class Reunion(Document):
    date = fields.DateTimeField(required=True)
    client = fields.ReferenceField(Client, required=True)
    feedbacks = fields.ListField(Product)

class Challenge(Document):
    title = fields.StringField()
    contract = fields.ReferenceField(Product)
    current_value = fields.IntField()
    max_value = fields.IntField()
    description = fields.StringField()

if __name__ == '__main__':
    c = Client(contact_id="blabla")
    with open("../contacts.txt",'r') as file:
        p = Product(file.readline())
        p = Client()
        print p.boolean_attributes
  #  p.name()
