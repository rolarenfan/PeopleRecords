from flask import make_response, abort

from file_parser.parse_file import parse_line
from model.person import (
    Person,
    sorted_list_1, sorted_list_2, sorted_list_3
)

DATA_STORE = []

# Create a handler for our sorted_birthdate (GET) people.
def sorted_birthdate():
    '''
        This function responds to a request for /api/records/birthdate

        :return: list of people, soted by birthdate ascending.
    '''
    return sorted_list_2(DATA_STORE)

# Create a handler for our sorted_gender (GET) people.
def sorted_gender():
    '''
        This function responds to a request for /api/records/gender

        :return: list of people, sorted by gender, then last name.
    '''
    return sorted_list_1(DATA_STORE)

# Create a handler for our sorted_name (GET) people.
def sorted_name():
    '''
        This function responds to a request for /api/records/name

        :return: list of people, sorted by last name descending.
    '''
    return sorted_list_3(DATA_STORE)

def create(person):
    '''
        Handler function for POST 'create' request to /api/records:
        creates a new person in the people structure based on the passed in person data.
        :param person:  person to create in people structure
        :return:        201 on success, 406 on person exists
    '''
    line = person.get('line', None)
    if not line:
        abort(
            422,
            f'Cannot create Person from "None" data',
        )

    person_object = Person(parse_line(line))
    if person_object in DATA_STORE:
        abort(
            406,
            f'Person with last name "{person_object.lname}" already exists',
        )
    else:
        DATA_STORE.append(person_object)
        return make_response(
            f'"{str(person_object)}" successfully created', 201
        )
