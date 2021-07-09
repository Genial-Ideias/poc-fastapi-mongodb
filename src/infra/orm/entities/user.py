from mongoengine.document import Document
from mongoengine.fields import EmailField, StringField

class User(Document):
    name = StringField(max_length=200, requuired=True)
    email = EmailField(required=True)
    password = StringField(max_length=255, required=True)
