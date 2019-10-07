import json


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def toJSON(self):
        return json.dumps(self.__dict__.update({'__class__': self.__class__}))

    @classmethod
    def my_class_method(cls):
        pass


class PersonEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Person):
            return o.toJSON()
        return super().default(o)


class PersonDecoder(json.JSONDecoder):

    pass
