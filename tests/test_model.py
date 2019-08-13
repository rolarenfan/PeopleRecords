import os
import unittest

from file_parser.parse_file import parse_line
from model.person import (
    Person,
    sorted_list_1, sorted_list_2, sorted_list_3
)

TEST_FILE = 'tests/data/sample.csv'

SORTED_1_GENDER_THEN_LASTNAME = [
    'Easter Bunny (Female), born 04/19/1835: favorite color White',
    'Jane Doe (Female), born 10/21/1967: favorite color Teal',
    'Diana WonderWoman (Female), born 10/25/1941: favorite color Red',
    'Tooth Fairy (Male), born 01/31/1220: favorite color White',
    'Clark Kent (Male), born 06/21/1938: favorite color Gold',
    'John Smith (Male), born 09/29/2010: favorite color Blue',
    'Doctor Who (Non-Binary), born 11/23/1963: favorite color Pink',
]

SORTED_2_BIRTHDATE = [
    'Tooth Fairy (Male), born 01/31/1220: favorite color White',
    'Easter Bunny (Female), born 04/19/1835: favorite color White',
    'Clark Kent (Male), born 06/21/1938: favorite color Gold',
    'Diana WonderWoman (Female), born 10/25/1941: favorite color Red',
    'Doctor Who (Non-Binary), born 11/23/1963: favorite color Pink',
    'Jane Doe (Female), born 10/21/1967: favorite color Teal',
    'John Smith (Male), born 09/29/2010: favorite color Blue',
]

SORTED_3_LASTNAME_DESCENDING = [
    'Diana WonderWoman (Female), born 10/25/1941: favorite color Red',
    'Doctor Who (Non-Binary), born 11/23/1963: favorite color Pink',
    'John Smith (Male), born 09/29/2010: favorite color Blue',
    'Clark Kent (Male), born 06/21/1938: favorite color Gold',
    'Tooth Fairy (Male), born 01/31/1220: favorite color White',
    'Jane Doe (Female), born 10/21/1967: favorite color Teal',
    'Easter Bunny (Female), born 04/19/1835: favorite color White',
]

class TestPersonMethods(unittest.TestCase):
    # python -m unittest test_model.TestPersonMethods

    def test_create_person(self):
        who = Person(['Who', 'Doctor', 'Non-Binary', 'Pink', '1963/11/23'])
        self.assertEqual(str(who), 'Doctor Who (Non-Binary), born 11/23/1963: favorite color Pink')

    def test_find_file(self):
        self.assertTrue(os.path.isfile(TEST_FILE))

    def test_sort_people(self):
        people = []
        with open(TEST_FILE, 'r') as reader:
            for line in reader.readlines():
                people.append(Person(parse_line(line)))

        self.assertEqual(sorted_list_1(people), SORTED_1_GENDER_THEN_LASTNAME)
        self.assertEqual(sorted_list_2(people), SORTED_2_BIRTHDATE)
        self.assertEqual(sorted_list_3(people), SORTED_3_LASTNAME_DESCENDING)


if __name__ == '__main__':
    unittest.main()
