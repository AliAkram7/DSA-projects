from faker import Faker

from faker import Faker
import requests

# Initialize the Faker generator
fake = Faker()

# Generate fake data
first_name = fake.first_name()
last_name = fake.last_name()
address = fake.address().replace('\n', ', ')
tel_number = fake.phone_number()
birth_day = fake.date_of_birth(minimum_age=18, maximum_age=40)

# Combine the data into a dictionary

def generatePerson(n) :
    list = []
    for i in range(0, n):
        first_name = fake.first_name()
        last_name = fake.last_name()
        address = fake.address().replace('\n', ', ')
        tel_number = fake.phone_number()
        birth_day = str(fake.date_of_birth(minimum_age=18, maximum_age=40))
        data = {
            'first_name': first_name,
            'last_name': last_name,
            'adress': address,
            'tel_number': tel_number,
            'birth_day': birth_day
        }
        list.append(data)
    return list
