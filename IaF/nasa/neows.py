#!/usr/bin/python3
import requests

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

def get_asteroids(startdate, nasacreds):
    resp = requests.get('https://api.nasa.gov/neo/rest/v1/feed?' + startdate + '&' + nasacreds)
    startdate = startdate.replace("start_date=","")
    death_dict = resp.json()
    num_asteroids = death_dict['element_count']
    num_hazardous = 0
    largest_asteroid = ""
    la_size = 0.0
    fastest_asteroid = ""
    fa_speed = 0.0
    closest_asteroid = ""
    ca_dist = 1000000000.0

    for day in death_dict['near_earth_objects'].keys():
        for item in death_dict['near_earth_objects'][day]:
            if item['is_potentially_hazardous_asteroid']:
                num_hazardous += 1
            if float(item['estimated_diameter']['kilometers']['estimated_diameter_max']) > la_size:
                la_size = float(item['estimated_diameter']['kilometers']['estimated_diameter_max'])
                largest_asteroid = item['name']
            if float(item['close_approach_data'][0]['relative_velocity']['kilometers_per_hour']) > fa_speed:
                fa_speed = float(item['close_approach_data'][0]['relative_velocity']['kilometers_per_hour'])
                fastest_asteroid = item['name']
            if float(item['close_approach_data'][0]['miss_distance']['kilometers']) < ca_dist:
                ca_dist = float(item['close_approach_data'][0]['miss_distance']['kilometers'])
                closest_asteroid = item['name']


    print(f"{num_hazardous} asteroids could kill us")
    print(f"{largest_asteroid} is the largest at {la_size} km")
    print(f"{fastest_asteroid} is the fastest at {fa_speed} km/h")
    print(f"{closest_asteroid} is the closest at a mere {ca_dist} km away")


# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    ## update the date below, if you like
    startdate = "start_date=2019-11-11"

    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    # make a request with the request library
    #neowrequest = requests.get(NEOURL + startdate + "&" + nasacreds)

    # strip off json attachment from our response
    #neodata = neowrequest.json()

    ## display NASAs NEOW data
    #print(neodata)


    get_asteroids(startdate, nasacreds)

if __name__ == "__main__":
    main()

