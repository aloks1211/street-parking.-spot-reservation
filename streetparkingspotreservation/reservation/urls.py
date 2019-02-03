from django.urls.conf import path
from .views import ParkingLocations, Reservation


urlpatterns = [
    path("locations/", ParkingLocations.as_view(), name="parkingslots list"),
    path("reservation/", Reservation.as_view(), name="reserve a parking"),

]