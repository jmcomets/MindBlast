from mongoengine import Document, fields

class Contract(Document):
    product_id = fields.StringField(unique=True)

class Client(Document):
    contact_id = fields.StringField(unique=True)
    has_car = fields.BooleanField(default=False)
    has_child = .BooleanField(default=False)
    is_married = fields.BooleanField(default=False)
    is_owner = fields.BooleanField(default=False)
    interests = fields.ListField(Contract)

class Challenge(Document):
    title = fields.StringField()
    contract = fields.ReferenceField(Contract)
    current_value = fields.IntField()
    max_value = fields.IntField()
    description = fields.StringField()
