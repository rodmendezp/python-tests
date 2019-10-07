import unittest
from serializer import custom_serializer


class SerializerTest(unittest.TestCase):
    def test_custom_serializer(self):
        person = custom_serializer.Person('Rodrigo', 28)
        person_encoder = custom_serializer.PersonEncoder()
        person_json = person_encoder.encode(person)
        print(person_json)
        print('Finished Test')
