class WGS84Coord:
    def __init__(self, longitude=0, latitude=0):
        self._longitude = longitude
        self._latitude = latitude
 
    def get_longitude(self):
        return self._longitude
 
    def set_longitude(self, value):
        if -180 <= value <= 180:
            self._longitude = value
        else:
            self._longitude = max(min(value, 180), -180)
            print("Warnung: Longitude wurde korrigiert.")
 
    def get_latitude(self):
        return self._latitude
 
    def set_latitude(self, value):
        if -90 <= value <= 90:
            self._latitude = value
        else:
            self._latitude = max(min(value, 90), -90)
            print("Warnung: Latitude wurde korrigiert.")
 

coord = WGS84Coord(200, 100)
coord.set_longitude(150)  
coord.set_latitude(-95)   
 
print(f"Longitude: {coord.get_longitude()}, Latitude: {coord.get_latitude()}")