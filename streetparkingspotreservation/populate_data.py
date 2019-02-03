import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','streetparkingspotreservation.settings')

import django
django.setup()

from reservation.models import User,ParkingSpots
from faker import Faker

fakegen = Faker()


def populate_users(n=20):
    # Create Fake Data for entry
    for i in range(n):
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_contact = fakegen.phone_number()
        # Create new User Entry
        User.objects.create(first_name=fake_first_name,last_name=fake_last_name,
                            contact=fake_contact)


def populate_parkinspots(n=50):
    for i in range(n):
        fake_lat = fakegen.latitude()
        fake_lng = fakegen.longitude()
        ParkingSpots.objects.create(lat=fake_lat,lng = fake_lng)


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate_parkinspots()
    populate_users()
    print('Populating Complete')
