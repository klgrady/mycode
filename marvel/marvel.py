#!/usr/bin/env python3

def do_batman():
    hero={'name':{'alias':'Batman','real name':'Bruce Wayne'},'background':{'origin':'Parents got murdered, got angry. Is super rich.','family':{'parents':'dead','siblings':None},'age':32,'number of deaths':19},'powers':['ninja training','money','batsuit'],'enemies':['joker','two face','scarecrow','poison ivy'],'allies':['cat woman','red robin','nightwing'],'rivals':['joker'],'weaknesses':['poverty','strict moral code']}

    choice = "e"
    while choice != "n":
        print("Would you like to see Batman's:\n\t(e) enemies\n\t(a) allies\n\t(r) rivals\n\t(p) powers\n\t(w) weaknesses\n\t(n) nope, exit\n")
        choice = input(">> ")
        if choice == "e":
            print("Enemies:")
            loop = hero["enemies"]
        elif choice == "a":
            print("Allies:")
            loop = hero["allies"]
        elif choice == "r":
            print("Rivals:")
            loop = hero["rivals"]
        elif choice == "p":
            print("Powers:")
            loop = hero["powers"]
        elif choice == "w":
            print("Weaknesses:")
            loop = hero["weaknesses"]
        else:
            return

        for stuff in loop:
            print(stuff.capitalize())


marvelchars = {
"starlord": {
	"real name": "peter quill",
	"powers": ["\tdance moves"],
	"archenemy": "Thanos",
  },
"mystique": {
	"real name": "raven darkholme",
	"powers": ["\tshape shifter"],
	"archenemy": "Professor X",
  },
"she-hulk": {
	"real name": "jennifer walters",
	"powers": ["\tsuper strength", "\tintelligence"],
	"archenemy": "Titania"
  },
"gwenpool": {
        "real name": "Gwendolyn Poole",
        "powers": ["\tmeta knowledge", "\tzf"],
        "archenemy": "M.O.D.O.K"
        }
}


print("Greetings, fellow nerd!")

choice = "None"
while(choice != ""):
    print("Which character do you want to know about?")
    for key in marvelchars.keys():
     print("\t" + key.title())

    print("\n\tOr simply hit [enter] to quit\n\n")
    choice = input(">> ")
    
    if choice == "":
        do_batman()
        quit()

    record = marvelchars.get(choice.lower(), "\nSorry, there's no " + choice)
    if type(record) is dict:
        name = choice.lower().title()
        print(name + "\n")
        print(name + "'s Real Name: " + record["real name"].title())
        print(name + "'s Powers:")
        print(*record["powers"], sep="\n")
        print(name + "'s Archenemy: " + record["archenemy"])
    else:
        print(record)

    print("\n\n")
