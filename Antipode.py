import geopy  # This library is used for its geocoding abilities
import webbrowser # This library lets you open a web browser to a specific URL.
from geopy.geocoders import Nominatim # The geocoding service that is used in this scripts is the Nominatim.

geocoder = Nominatim()


def anti_y(original_y):     #The opposite of  a location in terms of latitude is simply the positive or negative counterpart of the original y-value.
    return (original_y*-1)


def anti_x(original_x):     #The opposite of a location in terms of longitude is the distance that the location is from greenwich, either in a East or West direction.
    if original_x <= 0:
        x_dist = (180 - abs(original_x))
        new_x = 0 + x_dist
    else:
        new_x = (-180.0 + original_x)
    return new_x     


address = input("Please input the name of the town you live in: ")
location = geocoder.geocode(str(address)) # This is the user defined query that gives their current location.
x = location.longitude  #This extracts the longitude value of the user-defined location
y = location.latitude   #This extracts the latitude value of the user-defined location

new_y = anti_y(y)
print("Opposite latitude is: {}".format(str(new_y)))
new_x = anti_x(x)
print("Opposite longitude is: {}".format(str(new_x)))

wb = webbrowser.open("http://wikimapia.org/#lang=en&lat={}&lon={}&z=10&m=b".format(new_y,new_x)) # This opens a web browser to the antipode of the location that the user specified.
