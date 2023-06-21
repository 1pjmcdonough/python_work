# -*- coding: utf-8 -*-
"""
Detect valid Roman numerals

Refer to the instructions on Canavs for more information.

"I have neither given nor received help on this assignment."
author: Phillip McDonough
"""
__version__ = 1

def valid_numeral(test_case):
    '''
    This function takes in a string and calls each helper function. If 
    all functions return True valid_numeral() returns True, else False.
    '''
    if not charsCheck(test_case):
        return False
    
    if not fourInARow(test_case):
        return False
    
    if not numeralOrderCheck(test_case):
        return False
    
    if not validSequences(test_case):
        return False
    
    return True
    
    
def charsCheck(string):
    '''
    This function handles rules 1 and 2 of valid roman numerals. It takes in a 
    string as a parameter, validates it only contains roman numeral letters, 
    and returns a boolean
    '''
    if string == '':
        return False
    
    validCharsList = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    for char in string:
        if char not in validCharsList:
            return False
    return True

            
def fourInARow(string):
    '''
    This function handles rule 3 of valid roman numerals. It takes in a 
    string as a parameter, then validates the string doesn't have 4 of 
    the same character in a row. It return a boolean
    '''
    listOfFours = ['IIII', 'VVVV', 'XXXX', 'LLLL', 'CCCC', 'DDDD', 'MMMM']
    
    for fours in listOfFours:
        if fours in string:
            return False
    return True
    
 
def numeralOrderCheck(string):
    '''
    This function handles rules four, five, and six of valid roman numerals.
    It takes in a string as a parameter, checks if the order of the string 
    is valid for a roman numeral, and returns a boolean.
    '''
    length = len(string) - 1
    symbolsDict = {'I' : 1, 
                    'V' : 5,
                    'X' : 10,
                    'L' : 50,
                    'C' : 100,
                    'D' : 500,
                    'M' : 1000}
    
    powersOfTen = {'V':'I',
                  'X':'I',
                  'L':'X',
                  'C':'X',
                  'D':'C',
                  'M':'C'}

    for i in range(length):
        if not symbolsDict[string[i]] >= symbolsDict[string[i+1]]:
            if powersOfTen[string[i+1]] != string[i]:
                return False
    return True


def validSequences(string): 
    '''
    This function handles rule 7 of valid roman numerals. It takes in a 
    string as a parameter,checks if there are any sequential numerals of 2 or 3, 
    and returns true if they are powers of 10 or false otherwise.
    '''
    charsList = [char for char in string]
    for char in charsList:
        if charsList.count(char) == 2 or charsList.count(char) == 3:
            if (char == 'V' or char == 'L'
            or char == 'D'):
                return False
            else:
                continue
    return True


def main():
    testRulesOneAndTwo()
    testRuleThree()
    testRulesFourFiveSix()
    testRuleSeven()
    testvalidNumeral()
    
###############################################################
def testRulesOneAndTwo():
    # testing charsCheck() returns False when given anything other than valid roman 
    # numerals and returns True if it contains valid roman numerals 
    assert charsCheck('XVIII') == True, 'charsCheck() is returning a string containing roman numerals as False'
    assert charsCheck('24') == False, 'charsCheck() is returning a number as a valid roman numeral'
    assert charsCheck('Busch') == False, 'charsCheck() is returning invalid chars as a valid roman numeral'

def testRuleThree():
    # testing fourInARow() returns False when a roman numeral has 4 or more repeated 
    # chars and returns True if there are less than 4 repeated chars
    assert fourInARow('XVIII') == True, 'fourInARow() is returning a string with 3 repeated characters as False'
    assert fourInARow('XVIIII') == False, 'fourInARow() is returning a string with 4 repeated characters as True'
    assert fourInARow('XVIIIII') == False, 'fourInARow() is returning a string with 5 repeated characters as True'

def testRulesFourFiveSix():
    # testing numeralOrderCheck() returns False when given an invalid order of numerals 
    # and returns True when given a valid order 
    assert numeralOrderCheck('XVIII') == True, 'numeralOrderCheck() is returning a valid numeral order as False'
    assert numeralOrderCheck('IL') == False, 'numeralOrderCheck() is returing an invalid numeral order as True'
    assert numeralOrderCheck('IX') == True, 'numeralOrderCheck() is returing a valid numeral order as False'
    assert numeralOrderCheck('DM') == False, 'numeralOrderCheck() is returing an invalid numeral order as True'

def testRuleSeven():
    # testing validSequences() returns false if there is a sequence of 2 or 3 of a roman
    # numeral that's not a power of 10 and true if it is a power of 10
    assert validSequences('II') == True, 'validSequences() is returning a valid roman numeral sequence as false'
    assert validSequences('XXX') == True, 'validSequences() is returning a valid roman numeral sequence as false'
    assert validSequences('VV') == False, 'validSequences() is returning an invalid roman numeral sequence as True'
    assert validSequences('DDD') == False, 'validSequences() is returning an invalid roman numeral sequence as True'
    
def testvalidNumeral():
    #testing valid_numeral() returns True if given a valid roman numeral and 
    # false if given an invalid roman numeral
    assert valid_numeral('XVIII') == True, 'valid_numeral() is returning a valid roman numeral as false'
    assert valid_numeral('MCXIV') == True, 'valid_numeral() is returning a valid roman numeral as false'
    assert valid_numeral('CCCC') == False, 'valid_numeral() is returning an invalid roman numeral as True'
    assert valid_numeral('CIL') == False, 'valid_numeral() is returning an invalid roman numeral as True'
###############################################################    
    
if __name__ == "__main__":
    main()
    
    
    
    