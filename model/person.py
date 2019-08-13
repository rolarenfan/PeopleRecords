from datetime import date

class Person:
    """
        Simple data-class holding the values of a person, as parsed from the files in /tests/data
    """
    def __init__(self, data):
        (self.lname, self.fname, self.gender, self.fcolor, birthdate) = data

        # Assumes data is from the parsing function, i.e., in format YYYY/MM/DD.
        (year, month, day) = birthdate.split('/')
        self.birthdate = date(int(year), int(month), int(day))

    def __str__(self):
        birthdate = self.birthdate.strftime(('%m/%d/%Y'))
        return f'{self.fname} {self.lname} ({self.gender}), born {birthdate}: favorite color {self.fcolor}'


def sort_by_birthdate(person):
    """
        Key function to sort Person objects by birthdate.
        :param: Person
    """
    return person.birthdate

def sort_by_gender(person):
    """
        Key function to sort Person objects by gender.
        :param: Person
    """
    return person.gender

def sort_by_lastname(person):
    """
        Key function to sort Person objects by last name.
        :param: Person
    """
    return person.lname

def sorted_list_1(people):
    """
        Function to perform required sort #1: sort Person objects by gender, then by last name.
        :param: Person[]
    """
    return [str(person) for person in sorted(sorted(people, key=sort_by_lastname), key=sort_by_gender)]

def sorted_list_2(people):
    """
        Function to perform required sort #1: sort Person objects by birthdate.
        :param: Person[]
    """
    return [str(person) for person in sorted(people, key=sort_by_birthdate)]

def sorted_list_3(people):
    """
        Function to perform required sort #1: sort Person objects by last name, descending.
        :param: Person[]
    """
    return [str(person) for person in sorted(people, key=sort_by_lastname, reverse=True)]

sorts = [
    (sorted_list_1, '\n{} ascending then {} ascending'.format(sort_by_gender.__name__, sort_by_lastname.__name__)),
    (sorted_list_2, '\n{} ascending'.format(sort_by_birthdate.__name__)),
    (sorted_list_3, '\n{} descending'.format(sort_by_lastname.__name__)),
]
