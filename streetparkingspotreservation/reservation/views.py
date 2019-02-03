from django.http import JsonResponse
from django.http import HttpResponse
from django.views import  View
from reservation.models import Reservations, User, ParkingSpots
import json
from streetparkingspotreservation.logger import log
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import math, decimal


class Reservation(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        """
        Get all existing reservations
        """
        reservations = Reservation.get_all_reservations()
        final_repoonse = [{"id" : reservation.id,
                           "user_id" : reservation.user_id.id ,
                           "parking_spot" : reservation.parking_spot.id} for reservation in reservations]
        return JsonResponse(final_repoonse, safe=False)

    def post(self, request):
        """
        Make a reservation
        """
        data = request.body.decode('utf-8')
        json_data = json.loads(data)
        available_spots = ParkingLocations.get_available_parking_spots()
        if available_spots:
            reservation = Reservation.make_reservation(json_data["user_id"], available_spots)
            response = {"id" : reservation.id,
                        "user_id" : reservation.user_id.id ,
                        "parking_spot" : reservation.parking_spot.id}
            return JsonResponse(response, safe=False)
        else:
            response = {"Status" : False,
                        "message" : "No availabe spots, please try aganin some time!!!"}
            return JsonResponse(response, safe=False)

    def delete(self, request):
        """
        Delete a reservation for a user
        """
        data = request.body.decode('utf-8')
        json_data = json.loads(data)
        try:
            reservation = Reservations.objects.get(id=json_data["reservation_id"])
            reservation.delete()
            response = {"Status": "Successfully deleted."}
            return JsonResponse(response, safe= True)
        except Exception as e:
            return JsonResponse({'message': e.__str__()})
			
			
    @staticmethod
    def make_reservation(user_id, available_spots):
        user = User.objects.get(id=user_id)
        log.info("making reservations for user id : {0}".format(user.id))
        available = available_spots[0]
        available.reserved = True
        available.save()
        reservation = Reservations.objects.create(user_id=user, parking_spot=available)
        return reservation

    @staticmethod
    def get_all_reservations():
        return Reservations.objects.all()


class ParkingLocations(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        """
        GET all the available parkings on the map
        """

        park_spots = ParkingSpots.objects.filter(reserved = False)
        final_spots = [{"id" : spot.id,
                        "lat" : spot.lat,
                        "lng": spot.lng} for spot in park_spots]
        return JsonResponse(final_spots, safe=False)

    def post(self, request):
        """
        Search for an address and find nearby parking spot
        """

        data = request.body.decode('utf-8')
        if data:
            json_data = json.loads(data)
            try:
                lat = decimal.Decimal(json_data["lat"])
                lng = decimal.Decimal(json_data["lng"])
                radius = decimal.Decimal(json_data["radius"])

                park_spots = ParkingSpots.objects.filter(reserved=False, lat__lte=lat)
                print (park_spots)
                nearest = list(filter(lambda x: radius >= math.hypot(x.lat - lat, x.lng - lng), park_spots))
                print(nearest)
                response = [{"id": spot.id,
                             "lat": spot.lat,
                             "lng": spot.lng} for spot in nearest]
                return JsonResponse(response, safe=False)
            except Exception as e:
                return JsonResponse({'message': e.__str__()}, status=400)

    @staticmethod
    def get_available_parking_spots():
        return ParkingSpots.objects.filter(reserved=False)