import time

from bson import ObjectId
from mongoengine import Document, StringField, IntField, EmailField, BooleanField, ListField


class Users(Document):
    id = ObjectId()
    name = StringField(required=True)
    email = EmailField(sparse=True, unique=True, required=True)
    passwords = StringField(required=True)
    hash_passwords = StringField(required=True)
    createdAt = IntField(default=time.time())

    def to_json(self):
        return {
            "id": str(self.pk),
            "name": self.name,
            "email": self.email,
            "hash_passwords": self.hash_passwords,
            "createdAt": self.createdAt
        }

    def to_info(self):
        return {
            "id": str(self.pk),
            "name": self.name,
            "email": self.email
        }
