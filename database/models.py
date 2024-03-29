from mongoengine import Document, fields

class Product(Document):
    product_id = fields.StringField(unique=True)
    name = fields.StringField()
    code = fields.StringField()
    description = fields.StringField()
    family = fields.StringField()

    @property
    def challenges(self):
        return Challenge.objects(contract=self)

    @property
    def discounts(self):
        return Discount.objects(products__contains=self)

    @property
    def nb_discounts(self):
        return Discount.objects(products__contains=self).count()

class Client(Document):
    contact_id = fields.StringField(required=True, unique=True)
    has_car = fields.BooleanField(default=False)
    has_child = fields.BooleanField(default=False)
    is_married = fields.BooleanField(default=False)
    is_owner = fields.BooleanField(default=False)
    first_name = fields.StringField()
    last_name = fields.StringField()
    email = fields.StringField()
    phone = fields.StringField()
    description = fields.StringField()
    mailing_street = fields.StringField()
    mailing_city = fields.StringField()

    @property
    def reunions(self):
        return Reunion.objects(client=self)

    @property
    def feedbacks(self):
        return Feedback.objects(client=self)

    @property
    def name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @property
    def boolean_attributes(self):
        data = { 'has_car': self.has_car, 'has_child': self.has_child,
                'is_married': self.is_married, 'is_owner': self.is_owner }
        return data

class Feedback(Document):
    positive = fields.BooleanField(required=True)
    reason = fields.StringField()
    product = fields.ReferenceField(Product)
    client = fields.ReferenceField(Client)

class Reunion(Document):
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
        return 100*float(self.current_value)/float(self.max_value)

class Discount(Document):
    products = fields.ListField(fields.ReferenceField(Product))
    description = fields.StringField(required=True)


if __name__ == '__main__':
    print Client.objects()
    client = Client("003b000000KqjPVAAZ")
    print client.Name
   # Product.object.get()
    # with open("../contacts.txt",'r') as file:
    #     p = Product(file.readline().strip('\r\n'))
