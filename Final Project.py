# Program name: GarciaPeralta_David_FINALPROJECT
# Author: David Garcia Peralta
# Date: 3/1/2022
# Summary: Add up the digits in a num
# Variables:

'''
import random

c_route = []


for i in range(8):
    val = random.randint(0, 4)
    c_route = c_route.append(val) 
    print("Correct route is: ", c_route)
'''

import random


def c_path():
    c_path = []
    count = 1
    for i in range(5):
        c_path.append(random.randint(1, 4))
    return(c_path)

def maze():
    c_path = main.c_path
    print("You are in a dark hedge maze. Your friends left you behind because they figured it would be funny.")
    print("1 goes up, 2 goes right, 3 goes down, and 4 goes left.")
    d = int(print(input("Please enter a number 1 - 4 to walk a direction: ")))
    for num in c_path: 
        if d == c_path[1]:
            print("So far so good.")

def main():
    l = input("Hello, would you like to go through a maze? (Y/N)?: ")
    L = l.upper()
    
    if l.upper() == 'Y':
        c_path()
        print("work")
    elif l.upper() == 'N':
        print("You'll be back")
        return quit()
    else:
        l = print(input("That wasn't a valid answer. Please enter Y or N: "))


main()
