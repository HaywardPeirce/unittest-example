import json
from datetime import date

people = []

class humanConstructor():
    def __init__(self, name, age):

            self.name = name
            self.age = age

    def birthYear(self):

        return date.today().year - self.age

def createNewPersonFromJSON(jsonData):
    try:
        parsedData = json.loads(jsonData)
        person = humanConstructor(parsedData["name"], parsedData["age"])

        return person
    except TypeError as te:
        print(te)
        raise TypeError(te)
    except Exception as e:
        raise Exception(e)

def addPersonToPeople(person):
    people.append(person)


person = humanConstructor("John", 18)

attribute = "name"

# print(getattr(person, attribute))

