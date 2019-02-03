from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=128, default=None)
    last_name = models.CharField(max_length=128, default=None)
    contact = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)


class ParkingSpots(models.Model):
    lat = models.DecimalField(max_digits=10, decimal_places=5, name="lat")
    lng = models.DecimalField(max_digits=10, decimal_places=5, name="lng")
    reserved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.lat) + "," + str(self.lng)


class Reservations(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    parking_spot = models.ForeignKey(ParkingSpots, on_delete=models.CASCADE)




