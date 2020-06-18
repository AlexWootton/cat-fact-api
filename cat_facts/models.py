from peewee import *


DATABASE = SqliteDatabase('catfacts.sqlite')


class Fact(Model):
    """Contains the ids and body text of all accepted facts"""
    _id = CharField(unique=True)
    text = TextField()

    class Meta:
        database = DATABASE


class Blacklist(Model):
    """Contains the ids of all blacklisted facts"""
    _id = CharField(unique=True)

    class Meta:
        database = DATABASE


def initialise():
    DATABASE.connect()
    DATABASE.create_tables([Fact, Blacklist], safe=True)
    DATABASE.close()
