#!/usr/bin/python3
# https://anapioficeandfire.com/Documentation

import requests
import pprint
import pyfiglet
import argparse

parsival = argparse.ArgumentParser(description="Pick a GoT character to get amazing trivia!")
acceptable_chars=['Cersei Lannister','Daenerys Targaryen', 'Jon Snow', 'Sansa Stark', 'Arya Stark', 'Joffrey Baratheon', 'Tyrion Lannister', 'Margaery Tyrell', 'Brienne of Tarth', 'Lyanna Mormont']

parsival.add_argument("character", nargs='+', choices=acceptable_chars, help="The GoT character for which you wish to read cool trivia")

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters?name="

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
    info['books'] += info['povBooks']
    for book in info['books']:
        bookresp = requests.get(book)
        if not check_response(bookresp):
            print("API error")
            quit()
        bookj = bookresp.json()
        books.append(bookj['name'])
    return books

def print_aliases(aliases):
    if (len(aliases) > 1):
        alias_list = '\n\t'.join(aliases)
    elif (len(aliases) == 1):
        alias_list = aliases[0]
    else:
        alias_list = "No aliases"
    return alias_list

def check_response(info):
    if info.status_code > 299:
        return False
    return True

def print_houses(houses):
    if (len(houses) > 1):
        houselist = '\n\t'.join(houses)
    elif (len(houses) == 1):
        houselist = houses[0]
    else:
        houselist = 'No houses'
    return houselist


def print_books(books):
    if (len(books) > 1):
        booklist = '\n\t'.join(books)
    elif (len(books) == 1):
        booklist = books[0]
    else:
        booklist = '\n\tNo books, which is kinda weird'
    return booklist



def main():
    banner = pyfiglet.figlet_format("Getcher Game of Thrones")
    print(banner)
    ## Ask user for input
    #got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )
    name = parsival.parse_args()
    ' '.join(name.character)
    
    ## Send HTTPS GET to the API of ICE and Fire character resource
    gotresp = requests.get(AOIF_CHAR + name.character[0])
    if not check_response(gotresp):
        print("API error");
        quit()

    ## Decode the response
    got_dj = gotresp.json()
    name = got_dj[0]['name'] if got_dj[0]['name'] != "" else "Unnamed"
    houses = get_house(got_dj[0])
    books  = get_book(got_dj[0])
    aliases = got_dj[0]['aliases']
    print("Character Name:", name)
    print("Born: ", got_dj[0]['born'])
    print("Died: ", got_dj[0]['died'])
    print(f"Houses: \n\t{print_houses(houses)}")
    print(f"Books: \n\t{print_books(books)}")
    print(f"Aliases: \n\t{print_aliases(aliases)}")

if __name__ == "__main__":
    main()

