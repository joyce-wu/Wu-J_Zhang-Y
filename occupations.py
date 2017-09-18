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
            occupation = line[0] #takes occupation from each line and converts to a decimal
            percent = Decimal(line[1]) #takes percent from eachline
            dictionary[occupation]= percent #pairs occupation with its respective percent
       

def rand_occupation():
    myList = []
    #goes through each list, multiplying each percentage by 10
    for occupation in dictionary: 
        val = dictionary.get(occupation) * 10
        for x in range(val):
            myList.append(occupation) #adds occupation by value
    print random.choice(myList) #randomly chooses occupation from list

rand_occupation()


