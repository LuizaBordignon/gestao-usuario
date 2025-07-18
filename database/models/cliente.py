from peewee import CharField, Model, DateField, DateTimeField, datetime
from database.database import db

class Cliente(Model):
    nome = CharField()
    email = CharField()
    data_registro = DateTimeField(default=datetime.datetime.now)

    class Meta: 
        database = db