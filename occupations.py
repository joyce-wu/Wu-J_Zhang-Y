'''
Joyce Wu & Yuyang Zhang
SoftDev1 pd07
K02 -- StI/O: Divine your Destiny!
2017-09-14
'''


file = open("occupations.csv", "r")

dictionary = {}

for line in file: #at each line
    x = line.split(",") #split at the comma
    occupation = x[0] #occupation before
    percent = x[1] #percent after
    percentupdate = len(percent)-2 #removes \n and \r after percent
    percent = percent[0:percentupdate] #start from 0 to final value before \n and \r
    dictionary[occupation] = percent


print dictionary
