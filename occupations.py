'''
Joyce Wu & Yuyang Zhang
SoftDev1 pd07
K02 -- StI/O: Divine your Destiny!
2017-09-14
'''


import csv

dictionary = {} #creates blank dictionary 

with open('occupations.csv', 'r') as csv_file: #opens csv file and reads it
    csv_reader = csv.reader(csv_file) 

    next(csv_reader) #skips headings 
    for line in csv_reader: #goes through line by line
       occupation = line[0] #takes occupation from each line
       percent = line[1] #takes percent from eachline
       dictionary[occupation]= percent #pairs occupation with its respective percent

print dictionary
