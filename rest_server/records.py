from datetime import datetime

from flask import make_response, abort

def get_timestamp():
    return datetime.now().strftime(('%Y-%m-%d %H:%M:%S'))

# Data to serve with our API: LastName | FirstName | Gender | FavoriteColor | DateOfBirth
PEOPLE = {
    'Fairy': {
        'lname': 'Fairy',
        'fname': 'Tooth',
        'gender': 'Male',
        'fcolor': 'white',
        'birthdate': '1220/01/01',
    },
    'Who': {
        'lname': 'Who',
        'fname': 'Doctor',
        'gender': 'Non-Binary',
        'fcolor': 'pink',
        'birthdate': '1963/11/23',
    },
    'Woman': {
        'lname': 'Woman',
        'fname': 'Wonder',
        'gender': 'Female',
        'fcolor': 'red',
        'birthdate': '1941/10/25',
    },
    'Clark': {
        'lname': 'Clark',
        'fname': 'Kent',
        'gender': 'Male',
        'fcolor': 'gold',
        'birthdate': '1938/06/01',
    },
    'Easter': {
        'lname': 'Easter',
        'fname': 'Bunny',
        'gender': 'Female',
        'fcolor': 'white',
        'birthdate': '1835/04/19',
    }
}

# Create a handler for our read_all (GET) people, just a temporary placeholder.
def read_all():
    '''
    This function responds to a request for /api/records
    with the complete lists of people

    :return:        sorted list of people
    '''
    # Create the list of people from our data
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]

def create(person):
    '''
    This function creates a new person in the people structure
    based on the passed in person data
    :param person:  person to create in people structure
    :return:        201 on success, 406 on person exists
    '''
    lname = person.get('lname', None)
    fname = person.get('fname', None)
    gender = person.get('gender', None)
    fcolor = person.get('fcolor', None)
    birthdate = person.get('birthdate', None)

    # Does the person exist already?
    if lname not in PEOPLE and lname is not None:
        PEOPLE[lname] = {
            'lname': lname,
            'fname': fname,
            'gender': gender,
            'fcolor': fcolor,
            'birthdate': birthdate,
        }
        return make_response(
            '{lname} successfully created'.format(lname=lname), 201
        )

    # Otherwise, they exist, that's an error
    else:
        abort(
            406,
            'Person with last name {lname} already exists'.format(lname=lname),
        )
