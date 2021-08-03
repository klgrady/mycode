#!/usr/bin/python3
import random

questions_array = [
        {"question": "What is your level of attention to detail? [0-5] ", 
         "1": 3, 
         "2": 4, 
         "7": 5, 
         "9": 4, 
         "10": 4, 
         "14": 2
         },

        {"question": "How focused are you on safety? [0-5] ", 
         "4": 5,
         "8": 2,
         "11": 3,
         "12": 1,
         "13": 4,
         "15": 5,
         "16": 2
         },

        {"question": "How much abuse can you take in a day? [0-5] ",
         "4": 1,
         "5": 5,
         "6": 5,
         "10": 4,
         "11": 3,
         "13": 5
         },

        {"question": "How well can you stay on script? [0-5] ",
         "5": 3,
         "10": 5,
         "14": 2
         },

        {"question": "How BAD is your sense of smell? [0-5] ", 
         "6": 5,
         "8": 4,
         "12": 2
         },

        {"question": "How fearless are you? [0-5] ", 
         "4": 5,
         "6": 3,
         "7": 2,
         "8": 1,
         "13": 2,
         "15": 5,
         "11": 2,
         "16": 4
         },

        {"question": "How likely are you to try any food? [0-5] ", 
         "3": 3,
         "7": 4,
         "13": 5
         },

        {"question": "How much do you love animals? [0-5] ", 
         "1": 5,
         "3": 3,
         "4": 5,
         "8": 1,
         "12": 2
         },

        {"question": "How into weird stuff are you? [0-5] ", 
         "1": 3,
         "7": 5,
         "12": 4,
         "14": 5,
         "16": 5
         },
        
        {"question": "How much of a perpetual kid are you? [0-5] ", 
         "9": 5,
         "11": 4,
         "12": 3
         }

        ]

professions = [
        ["Chicken Sexer", "You'll determine the sex of chicks. Hurray!"], 
        ["Netflix Tagger", "You'll watch endless Netflix to tag the genre. Woot!"], 
        ["Dog Food Taster", "You'll determine whether dog food is delicious and has a nice crunch. Good for you!"], 
        ["Snake Milker", "You get to (carefully) help snakes drool some venom to create anti-venin. Lucky you."], 
        ["Telemarketer", "We hope you love to talk on the phone to people who hate you!"], 
        ["Port-a-Potty Cleaner", "You love the smell of napalm in the morning, right?"], 
        ["Forensic Entomologist", "Determine time of death of corpses by way of the insect population it's gathered. Sounds like fun, right?"], 
        ["Roadkill Removal Specialist", "Drive around, listen to tunes, scrape carcasses off the road. Every day is a vacay."], 
        ["Lego Sculptor", "Make incredible art with Legos. Just try not to step on any."], 
        ["Professional Bridesmaid", "Not only do you have the pleasure of helping to plan and run the wedding, you a godawful dress to wear, too. Yayayay!"], 
        ["Waterslide Tester", "It's all fun and games until there's a tragic accident. Until then, enjoy!"], 
        ["Goat Yoga Instructor", "Yoga. People yoga. But with goats there. What could go wrong?"], 
        ["Poison Taster", "Yes, these still exist. Travel around with famous people and make sure nobody tried to poison them. If they did... at least you won't need the job anymore."], 
        ["UFO Reports Taker", "Listen to people talk about what they saw, write it down, bring stories back to your friends and family."], 
        ["Wind Turbine Technician", "We hope you love heights because wind turbines are reeeeeeally high up there. Hang on tight and enjoy the ride!"], 
        ["Paranormal Investigator", "Stay up all night, run around in the dark, scream like a kindergartener, and make sure it's all on video."]
        ]


def main():
    # Welcome screen
    print("\n\n\n  What Should I Be When I Grow Up?")
    print("a quiz for adults dealing with failure")
    print("\n\nFor each question, answer on a scale from 0 to 5, where 0 is a hard pass and 5 is an I'M IN.")

    # initialize a list to keep answer tallies
    final_tally = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    # Prompt with questions
    for key in questions_array:
        response = (input(key["question"]))
        while (not response.isdigit() or int(response) > 5): 
             print("Nope, that answer is not valid. Try again.")
             response = (input(key["question"]))   

        response = int(response)

        # if/elif/else requirement complete!
        if response < 2:
            print("Y'know, therapy might help with that.")
        elif response == 2:
            print("Maybe you can take a class?")
        elif response == 3:
            print("Well, you have other qualities, right?")
        elif response == 4:
            print("So, you have commitment issues? Is that it?")
        else:
            print("Cool, we can work with that.")
        print("\n")

        # And calculate a new tally depending on that response for related questions
        for item in key:
            if item.isdigit():
                final_tally[int(item) - 1] += key[item] * response
       

    # Find the highest score
    max_val = max(final_tally)
    max_index = final_tally.index(max_val)

    # Print result
    print("\n\n\nYou will be a " + professions[max_index][0] + "!")
    print(professions[max_index][1])
    print("Congrats!")

    # Print the womp womp
    random_index = random.randint(0,15)
    print("If that doesn't sound great to you, too bad. Maybe try " + professions[random_index][0] + " instead?\n\n\n")


# run main if it's a script
if __name__ == "__main__":
    main()
