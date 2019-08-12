from datetime import date

class Person:
    """
        Simple data-class holding the values of a person, as aprsed from the data-files.
    """
    def __init__(self, data):
        # Assumes data is from the parsing function, i.e., in format YYYY/MM/DD.
        (self.lname, self.fname, self.gender, self.fcolor, birthdate) = data
        (year, month, day) = birthdate.split('/')
        self.birthdate = date(int(year), int(month), int(day))

    def __str__(self):
        birthdate = self.birthdate.strftime(('%m/%d/%Y'))
        return f'{self.fname} {self.lname} ({self.gender}), born {birthdate}: favorite color {self.fcolor}'


def sort_by_birthdate(person):
    return person.birthdate

def sort_by_gender(person):
    return person.gender

def sort_by_lastname(person):
    return person.lname
