'''
Joyce Wu & Yuyang Zhang
SoftDev1 pd07
K03 -- StI/O: Divine your Destiny!
2017-09-14
'''


import csv
import random
from decimal import Decimal

dictionary = {} #creates blank dictionary 

with open('occupations.csv', 'r') as csv_file: #opens csv file and reads it
    csv_reader = csv.reader(csv_file) 
    next(csv_reader) #skips headings
    for line in csv_reader: #goes through line by line
        if not (line[0] == "Total"): #does not include total in dictionary
            occupation = line[0] #takes occupation from each line
            percent = line[1] #takes percent from eachline
            dictionary[occupation]= percent #pairs occupation with its respective percent
       

#print dictionary

def rand_occupation():
    randnum = random.randint(0,100) #picks a number from 0-100
    #print randnum
    for occupation in dictionary:  #goes through each percent in the dictionary
        val = dictionary.get(occupation)
        if (randnum < Decimal(val)): #if number is less than percent 
            #print 10 * Decimal(val)
            print(occupation) #print the occupation
            break #allows only for one occupation to be printed

            
      
for x in range(100):
    rand_occupation()
