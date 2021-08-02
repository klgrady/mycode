#!/usr/bin/env python3

import random

icecream=["flavors", "salty"]
tlgclass= ["Adrian","Bikash","Chas","Chathula","Chris","Hongyi","Jauric","Joe L.","Joe V.","Josh","Justin","Karlo","Kerri-Leigh","Jason","Nicholas","Peng","Philippe","Pierre","Stephen","Yun"]

icecream.append(99)

victim = int(input("Input a number from 0 to 19: "))
print(f"{icecream[2]} {icecream[0]}, and {tlgclass[victim]} chooses to be {icecream[1]}")

#random
victim = random.choice(tlgclass)
print(f"{icecream[2]} {icecream[0]}, and {victim} chooses to be {icecream[1]}")


# if it's a name...
victim = input("Input a number or a name: ")
if victim.isdigit():
    victim = tlgclass[int(victim)]



print(f"{icecream[2]} {icecream[0]}, and {victim} chooses to be {icecream[1]}")

