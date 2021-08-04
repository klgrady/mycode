#!/usr/bin/env python3
import re

farms = [{"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "E Farm", "agriculture": ["bananas", "apples", "oranges"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]}]


animals = ["sheep", "cows", "pigs", "chickens", "turkeys", "llamas", "cats", "dogs", "hamsters", "pigs", "goats", "rabbits", "horses", "alpacas", "donkeys", "rabbits"]



def all_NE_animals():
    NE_farm = next(farm for farm in farms if farm["name"] == "NE Farm")
    return NE_farm["agriculture"]

def get_farm_agriculture(farm_choice):
    ret_farm = get_farm(farm_choice)
    if ret_farm == None:
        return "No such farm"
    
    return ret_farm["agriculture"]



def get_only_animals(farm_choice):
    ret_farm = get_farm(farm_choice)
    if ret_farm == None:
        return "No such farm"

    actual_list = []
    for thing in ret_farm["agriculture"]:
        if (thing in animals):
            actual_list.append(thing)

    return actual_list



def get_farm(farm_choice): 
    if re.search('farm', farm_choice.lower()) == None:
        farm_choice = farm_choice + " Farm"
    return next((farm for farm in farms if farm["name"] == farm_choice), None)



def get_options():
    name = []
    for farm in farms:
        name.append(farm["name"])
    print("\n\nFarms:")
    print(*name)



def main():
    print(all_NE_animals())
    get_options()
    ag = get_farm_agriculture(input("View agriculture from which farm?").strip())
    print(ag if ag != [] else "None")
    get_options()
    ag = get_only_animals(input("View animals ONLY from which farm?").strip())
    print(ag if ag != [] else "None")


if __name__ == "__main__":
    main()
