#!/usr/bin/python3

import requests
from datetime import datetime
from datetime import time
import reverse_geocoder as rg

class ISS:
    def __init__(self):
        self.url="http://api.open-notify.org/iss-now.json"
        

    def get_location(self):
        data = requests.get(self.url)
        self.location = data.json()
        return data.json()

    def time_stamp(self, time):
        time_obj = datetime.fromtimestamp(time)
        return time_obj

    def get_city(self):
        long = self.location['iss_position']['longitude']
        lat  = self.location['iss_position']['latitude']
        data = rg.search((lat, long))
        output = [data[0]['name'], data[0]['admin1'], data[0]['admin2']]
        try:
            output.remove('')
        except:
            #no op, who cares...
            pass
        return ', '.join(output)

    def get_printout(self):
        location = self.get_location()
        print("CURRENT LOCAITON OF THE ISS:")
        print("Timestamp: " + str(self.time_stamp(location['timestamp'])))
        print(f"Lon: {location['iss_position']['longitude']}")
        print(f"Lat: {location['iss_position']['latitude']}")
        print(f"City: {self.get_city()}")


def main():
    newIss = ISS()
    newIss.get_printout()



if __name__ == "__main__":
    main()
