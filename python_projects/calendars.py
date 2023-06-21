# -*- coding: utf-8 -*-
"""
Functions about calendars

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Phillip McDonough
"""
__version__ = 1


def gregorian(year):
    #determines if a year is a Gregorian leap year
    #takes in an integer year as an argument 
    #returns boolean result
    
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False
    

def milankovic(year):
    #determines if a year is a Milankovic leap year
    #takes in an integer year as an argument
    #returns boolean result
    
    if year % 4 == 0 and year % 100 != 0:
        return True 
    elif year % 4 == 0 and year % 100 == 0 and (year % 900 == 200 or year % 900 == 600):
        return True
    else:
        return False
    

def gregorian_count(year1, year2):
    # determines the number of leap years that lie 
    #between two dates on the Gregorian calendar
    #takes in two integer years as arguments 
    #returns a count of the leap years 
    
   count = 0
   
   for year in range(year1,year2):
        if gregorian(year) == True:
            count += 1
            
   return count
        

def milankovic_count(year1, year2):
    # determines the number of leap years that lie 
    #between two dates on the milankovic calendar
    #takes in two integer years as arguments 
    #returns a count of the leap years
    
    count = 0
   
    for year in range(year1,year2):
        if milankovic(year) == True:
            count += 1
            
    return count


def main():
    gregorian_test()
    milankovic_test()
    gregorian_count_test()
    milankovic_count_test()
    
###############################################################

def gregorian_test():
    # testing that gregorian() can determine if a year is a gregorian leap year
    assert gregorian(1696) == True, 'gregorian(1696) is not returning the right boolean'
    assert gregorian(1697) == False, 'gregorian(1697) is not returning the right boolean'
    assert gregorian(2100) == False, 'gregorian(2100) is not returning the right boolean'
    assert gregorian(2800) == True, 'gregorian(2800) is not returning the right boolean'
    
def milankovic_test():
    # testing that milankovic() can determine if a year is a milankovic leap year 
    assert milankovic(1696) == True, 'milankovic(1696) is not returning the right boolean'
    assert milankovic(1697) == False, 'milankovic(1697) is not returning the right boolean'
    assert milankovic(2100) == False, 'milankovic(2100) is not returning the right boolean'
    assert milankovic(2800) == False, 'milankovic(2800) is not returning the right boolean'

def gregorian_count_test():
    # testing that gregorian_count() can determine the number of leap years between two years
    assert gregorian_count(1696, 1697) == 1, 'gregorian_count(1696, 1697) is not returning the right count'
    assert gregorian_count(1900, 1901) == 0, 'gregorian_count(1900, 1901) is not returning the right count'
    assert gregorian_count(2000, 3000) == 243, 'gregorian_count(2000, 3000) is not returning the right count'
    assert gregorian_count(2000, 2850) == 207, 'gregorian_count(2000, 2850) is not returning the right count'

def milankovic_count_test():
    # testing that milankovic_count() can determine the number of leap years between two years
    assert milankovic_count(1696, 1697) == 1, 'milankovic_count(1696, 1697) is not returning the right count'
    assert milankovic_count(1900, 1901) == 0, 'milankovic_count(1900, 1901) is not returning the right count'
    assert milankovic_count(2000, 3000) == 243, 'milankovic_count(2000, 3000) is not returning the right count'
    assert milankovic_count(2000, 2850) == 206, 'milankovic_count(2000, 2850) is not returning the right count'
    
###############################################################    
    
if __name__ == "__main__":
    main()  