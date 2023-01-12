from datetime import datetime

from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import BooleanField, DateTimeField, EmbeddedDocumentField, ListField, StringField


class Email(EmbeddedDocument):
    name = StringField()

class Adress(EmbeddedDocument):
    name = StringField()

class Phone(EmbeddedDocument):
    name = StringField()



class Record(Document):
    name = StringField()
    created = DateTimeField(default=datetime.now())
    emails = ListField(EmbeddedDocumentField(Email))
    adresses = ListField(EmbeddedDocumentField(Adress))
    phones = ListField(EmbeddedDocumentField(Phone))
    meta = {'allow_inheritance': True}