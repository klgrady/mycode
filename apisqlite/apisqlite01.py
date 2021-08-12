#!/usr/bin/env python3
""" Author: RZFeeser || Alta3 Research
Gather data returned by various APIs published on OMDB, and cache in a local SQLite DB
"""

import json
import sqlite3
import requests

# Define the base URL
OMDBURL = "http://www.omdbapi.com/?"
movietypes = {"1": "movie", "2": "series", "3": "episode"}

# search for all movies containing string
def movielookup(mykey, searchstring):
    """Interactions with OMDB API
       mykey = omdb api key
       searchstring = string to search for"""
    try:
        # begin constructing API
        api = f"{OMDBURL}apikey={mykey}&s={searchstring}"

        ## open URL to return 200 response
        resp = requests.get(api)
        ## read the file-like object decode JSON to Python data structure
        return resp.json()
    except:
        return False


#search for movies with string and by type
def movielookuptype(mykey, searchstring, mtype):
    if mtype not in movietypes.values():
        print("Bad type")
        return False

    try:
        api = f"{OMDBURL}apikey={mykey}&s={searchstring}&type={mtype}"
        resp = requests.get(api)
        return resp.json()
    except:
        return False


#search for movies with string and by year
def movielookupyear(mykey, searchstring, year):
    try:
        api = f"{OMDBURL}apikey={mykey}&s={searchstring}&y={year}"
        resp = requests.get(api)
        return resp.json()
    except:
        return False

#search for movies with string and by year and type
def movielookupyeartype(mykey, searchstring, year, mtype):
    if mtype not in movietypes.values():
        print("Bad type")
        return False

    try:
        api = f"{OMDBURL}apikey={mykey}&s={searchstring}&type={mtype}&y={year}"
        resp = requests.get(api)
        return resp.json()
    except:
        return False


def writedb():
    conn = sqlite3.connect('mymovie.db')
    try:
        results = conn.execute('''SELECT * FROM MOVIES ORDER BY YEAR, TITLE''')

        for row in results:
            print(f"TITLE: {row[0]} ({row[1]})")

    except Exception as e:
        print("Error:", e)

    conn.close()

def trackmeplease(datatotrack):
    conn = sqlite3.connect('mymovie.db')
    try:
        conn.execute('''CREATE TABLE IF NOT EXISTS MOVIES (TITLE TEXT PRIMARY KEY NOT NULL, YEAR INT  NOT NULL);''')

        # loop through the list of movies that was passed in
        for data in datatotrack:
            # in the line below, the ? are examples of "bind vars"
            # this is best practice, and prevents sql injection attacks
            # never ever use f-strings or concatenate (+) to build your executions
            conn.execute("INSERT INTO MOVIES (TITLE,YEAR) VALUES (?,?)",(data.get("Title"), data.get("Year")))
            conn.commit()

        print("Database operation done")
        conn.close()
        return True
    except:
        return False

# Read in API key for OMDB
def harvestkey():
    with open("/home/student/omdb.key") as apikeyfile:
        return apikeyfile.read().rstrip("\n") # grab the api key out of omdb.key

def printlocaldb():
    pass
    #cursor = conn.execute("SELECT * from MOVIES")
    #for row in cursor:
    #    print("MOVIE = ", row[0])
    #    print("YEAR = ", row[1])


def main():

    # read the API key out of a file in the home directory
    mykey = harvestkey()

    # enter a loop condition with menu prompting
    while True:
        # initialize answer
        answer = ""
        while answer == "":
            print("""\n**** Welcome to the OMDB Movie Client and DB ****
            ** Returned data will be written into the local database **
            1) Search for All Movies Containing String
            2) Search for Movies Containing String, and by Type
            3) Search for Movies Containing String, and by Year
            4) Search for Movies Containing String, and by Type and Year
            5) Display Entries in Local DB
            99) Exit""")

            answer = input("> ") # collect an answer for testing

        # testing the answer
        if answer in ["1", "2", "3", "4", "5"]:
            # All searches require a string to include in the search
            if answer != "5":
                searchstring = input("Search all movies in the OMDB. Enter search string: ")

            if answer == "1":
                resp = movielookup(mykey, searchstring)
            
            if answer == "2" or answer == "4":
                print("""\nWhich type of movie?
                          1) Movie
                          2) Series
                          3) Episode
                          """)

                movietype = input("> ") # collect type
               
            if answer == "3" or answer == "4":
                searchyear = input("Year of release: ")


            if answer == "2":
                resp = movielookuptype(mykey, searchstring, movietypes[movietype.strip()])
            elif answer == "3":
                resp = movielookupyear(mykey, searchstring, searchyear)
            elif answer == "4":
                resp = movielookupyeartype(mykey, searchstring, searchyear, movietypes[movietype.strip()])


            elif answer == "5":
                writedb()
                resp = None

            if resp:
                # display the results
                resp = resp.get("Search")
                print(resp)
                # write the results into the database
                trackmeplease(resp)
            elif answer != "5":
                print("That search did not return any results.")

        # user wants to exit
        elif answer == "99":
            print("See you next time!")
            break

if __name__ == "__main__":
    main()

