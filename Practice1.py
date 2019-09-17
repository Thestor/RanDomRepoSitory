# -*- coding: utf-8 -*-'

"""
Name: Exercise 1
@author: Matthew
"""

print("Enter your height.")

try:
    heightinfeet = eval(input("Feet: "))
    heightininches = eval(input("Inches: "))
except:
    print("That is an invalid input.")
else:
    heightincm = (heightinfeet * 30.48) + (heightininches * 2.54)
    length = heightincm * 0.88
    print ("\nSuggested board length:", length, "cm")