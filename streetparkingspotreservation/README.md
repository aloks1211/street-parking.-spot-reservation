
Street Parking Spot Reservation service Using Django(Backend)

Requirements:

• See available parking spots on a map

• Search for an address and find nearby parking spot. (input: lat, lng, radius in meters. Output - list of parking spots within the radius).

• Reserve a parking spot.

• View existing reservations.

• Cancel an existing reservation.

• Show the user the cost of the reservation

####API SPECIFICAIONS:
* Get all the existing parking Spots.

        GET /reservation/locations/

* Get nearest parking spot within a radius of a given loation.
        
        POST /reservation/locations/
        Json body = {"lat" : 72.28372,
	            "lng" : 134.25193,
	            "radius" : 136}
	            
* Get all reservations.

        GET /reservation/reservation/
        
* Make a reservation for user 
    
            POST /reservation/reservation/
            Json body = {"user_id" : 5}
        
* Cancel a reservation

        DELETE /reservation/reservation/
        Json body = {"reservation_id" : 5}
       
Data population Script:
    
    python populate_data.py
   
#### Running Instructions
python manage.py runserver

##### There should now be server running:

http://127.0.0.1:8000 is the Django app

