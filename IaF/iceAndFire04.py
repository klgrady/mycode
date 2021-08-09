#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def get_name(info):
    return info['name']


def get_house(info):
    houses = []
    for allegiance in info['allegiances']:
        houseresp = requests.get(allegiance)
        if not check_response(houseresp):
            print("API error")
            quit()
        housej = houseresp.json()
        houses.append(housej['name'])
    return houses


def get_book(info):
    books = []
    for book in info['books']:
        bookresp = requests.get(book)
        if not check_response(bookresp):
            print("API error")
            quit()
        bookj = bookresp.json()
        books.append(bookj['name'])
    return books

def check_response(info):
    if info.status_code > 299:
        return False
    return True

def print_houses(houses):
    if (len(houses) > 1):
        houselist = '\n\t'.join(houses)
    elif (len(houses) == 1):
        houselist = '\t' + houses[0]
    else:
        houselist = '\nNo houses'
    return houselist


def print_books(books):
    if (len(books) > 1):
        booklist = '\n\t'.join(books)
    elif (len(books) == 1):
        booklist = '\t' + books[0]
    else:
        booklist = '\nNo books, which is kinda weird'
    return booklist



def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)
        if not check_response(gotresp):
            print("API error");
            quit()

        ## Decode the response
        got_dj = gotresp.json()
        name = got_dj['name']
        houses = get_house(got_dj)
        books  = get_book(got_dj)
        print("Character Name:", name)
        print(f"Houses: \n{print_houses(houses)}")
        print(f"Books: \n{print_books(books)}")

if __name__ == "__main__":
        main()

