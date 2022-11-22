import unittest
from itertools import combinations
from app import *

# TODO: how to automate testing a range of cases around correct data/type, none, bad data, different exceptions without manually writing them out for each funtion

class AssertPeopleEqual:
    def assert_people_equal(self, person1, person2):

        if type(person1) != type(person2):
                raise AssertionError("car1 is of type: ", type(car1), " and car2 is of type: ", type(car2))
        
        for attribute, value in person1.__dict__.items():
            # print(attribute," ", value)
            
            if value != getattr(person2, attribute):
                raise AssertionError( attribute, " of person1: ", person1.getattr(attribute), " and ", attribute, " of person2: ", person1.getattr(attribute))





class TestData(humanConstructor):
    

    basicBadDataItems = [None, True, False, "test", 10]

    goodValues = {"name":"Patrick", "age":21}

    benchmarkPerson = humanConstructor(goodValues["name"],goodValues["age"])

    structuredAgeTestData = [
        {
            "input": benchmarkPerson,
            "comparisonValue": 2003,
            "expectedResult": "fail" # options include pass, fail, 
        },
        {
            "input": benchmarkPerson,
            "comparisonValue": 2001,
            "expectedResult": "pass" # options include pass, fail, 
        }
        
    ]


    # Generate a list of combinations (in the same length as the object holding the good data values) of each of the basic possible input values
    def generatePersonTestDataList(self):
        
        list_combinations = []

        for combo in combinations(self.basicBadDataItems, len(self.goodValues)):

            list_combinations.append(combo)
        
        print(list_combinations)

        return list_combinations


    
        
# The test based on unittest module
# includes `AssertPeopleEqual` class to allow for comparing the equlaity of people objects (which otherwise can't be direclty compared)
class TestHumanBuilder(unittest.TestCase, AssertPeopleEqual, TestData):

    def setUp(self):

        # super().__init__()
        # print(self.personJSONData)
        # self.testJSONData

        self.examplePerson = humanConstructor("James", 19)

        self.testJSONData = '{"name":"Patrick", "age":21}'

    # test creating a person using both good and bad data
    def test_person_create(self):

        self.assert_people_equal(createNewPersonFromJSON(self.testJSONData), self.benchmarkPerson)

        # Loop through each of the generated combinations of bad test data and confirm they each thrown an exception
        for caseData in self.generatePersonTestDataList():
            
            print("printing case: ", caseData)
            
            with self.assertRaises(Exception):

                createNewPersonFromJSON(caseData)

    # test if passing in none when a JSON object is expected throws any type of exception
    def test_person_create_notjson(self):

        with self.assertRaises(Exception):
            createNewPersonFromJSON(None)
    
    # test if passing in none when a JSON object is expected throws specifically a TypeError
    def test_person_create_notjsonType(self):
        with self.assertRaises(TypeError):
            createNewPersonFromJSON(None)

    def test_birth_year(self):
        for element in self.structuredAgeTestData:
            if element["expectedResult"] == "fail":
                self.assertNotEqual(element["input"].birthYear(), element["comparisonValue"], "Inorrect birth year calculation")
            elif element["expectedResult"] == "pass":
                self.assertEqual(element["input"].birthYear(), element["comparisonValue"], "Correct birth year calculation")


human_builder_suite = unittest.TestLoader().loadTestsFromTestCase(TestHumanBuilder)

runner = unittest.TextTestRunner()
runner.run(human_builder_suite)

# if __name__ == '__main__':
#     unittest.main()
