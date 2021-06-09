# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Exercise1

calc1= 2**3 / 3**2
calc2 = 2 ** (3 / 5)

print("ENGG1811 LAB Week 1")
print("Exercise 1:")
print("Calculation 1: " + str(calc1))
print("Calculation 2: " + str(calc2))
print("")

print("Exercise 2:")

mins = 10**6

years = int(mins / 60 / 24 /365)
print("years: " + str(years))
mins = mins - years * 365 * 24 * 60

days = int(mins / 24 / 60)
print("days: " + str(days))
mins = mins - days * 24 * 60

hours = int(mins / 60)
print("hours: " + str(hours))

mins = mins - hours * 60
print("minutes: " + str(mins))

print("1 million minutes = " + str(years) + " years " 
      + str(days) + " days " + str(hours) + " hours "
      + str(mins) + " minutes ")




