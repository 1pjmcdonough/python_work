# -*- coding: utf-8 -*-
"""
Functions about word reductions

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Phillip McDonough
"""
__version__ = 1

def loadWords():
    '''
    This function opens the words_alpha.txt file, reads it
    line-by-line, and adds each word into a list.  It returns
    the list containing all words in the file.
    '''
    with open('words_alpha.txt') as wordFile:
        wordList = []
        
        for line in wordFile:
            wordList.append(line.rstrip('\n'))

    return wordList



def reduceOne(firstString, secondString, wordList):
    '''
    This function takes in two strings and a list of words
    as arguments, checks that the two strings are in the word list, 
    checks if the second string is a reduction of the first string,
    and returns a boolean result.
    '''
    wordBank = []
    firstStringLength = len(firstString)
    
    if (firstString in wordList and secondString in wordList):
        for i in range(firstStringLength):
            reduction = firstString[:i] + firstString[i+1:]
            wordBank.append(reduction)
    else:
        return False
        
    if secondString in wordBank:
        return True
    else:
        return False
            

        
def reduceAll(word, wordList):
    '''
    This function takes in a word and a list of words as arguments,
    loops through the letters of the given word, creates reductions and 
    checks if they are in the wordList,then adds those reductions into a
    seperate list. It returns the seperate list with all the valid reductions.
    '''
    wordBank = []
    wordLength = len(word)
    
    for i in range(wordLength):
        reduction = word[:i] + word[i+1:]
        if reduction in wordList:
            wordBank.append(reduction)
        
    return wordBank
            
    
        
def reduceTwoAll(word, wordList):
    '''
    This function takes in a word and a list of words as arguments. It first uses
    a for loop to add words reduced by 1 to a list, and then another for loop calls 
    the reduceAll() function for each word in the list. Each element in the list
    made in the for loop is then added to a seperate list called wordBank.
    Another for loop is then used to loop through the letters of the given word, 
    creates double reductions and checks if they are in the wordList,then adds 
    those reductions into wordBank. wordBank is then returned.
    '''
    wordBank = []
    wordLength = len(word) - 1
    reducedAllWords = []
    
    for i in range(len(word)):
        reduction = word[:i] + word[i+1:]
        reducedAllWords.append(reduction)
        
    
    for reducedWord in reducedAllWords:
        reduceTwo = reduceAll(reducedWord, wordList)
        for elm in reduceTwo:
            wordBank.append(elm)
    
    
    for i in range(wordLength):
        twoReduction = word[:i] + word[i+2:]
        if twoReduction in wordList:
            wordBank.append(twoReduction)
            
    
    return wordBank

        

def validateReduction(reduction, wordList):
    '''
    This function takes in two lists as arguments. It first tests that all the 
    words in the reduction list are also in wordList. It then tests if the 
    reduction list is a valid sequence of reductions. This function returns a 
    boolean result.
    '''
    testList = []
    reductionLength = len(reduction) - 1 
    
    for word in reduction:
        if word not in wordList:
            return False
        
    for i in range(reductionLength):
        if reduceOne(reduction[i], reduction[i+1], wordList):
            testList.append(reduction[i])
             
    # takes both lists and checks if all values are the same up to the last value.
    # The last values does not need to be checked because the value before it would
    # not be in the test list if the two words were not reductions     
    if testList[:reductionLength] == reduction[:reductionLength]:  
        return True
    else:
        return False
                            
        
        
def main():
    wordList = loadWords()
    reduceOneTests(wordList)
    reduceAllTests(wordList)
    reduceTwoAllTests(wordList)
    validateReductionTests(wordList)
    

###############################################################

def reduceOneTests(wordList):
    # This is testing that reduceOne() returns the correct boolean and that it5
    # doesn't allow for reductions of more than one letter
    
    assert reduceOne('lea', 'eave', wordList) == False, 'reduceOne() did not return the right boolean when given an invalid first string'
    assert reduceOne('leave', 'boats', wordList) == False, 'reduceOne() did not return the right boolean when given an invalid second string'
    assert reduceOne('leaves', 'eave', wordList) == False, 'reduceOne() reduced by more than one character'
    assert reduceOne('boats', 'bats', wordList) == True, 'reduceOne() did not return the right boolean when reducing a middle character'
 
    
def reduceAllTests(wordList):
    # This is testing that reduceAll() returns the right reductions when given a valid word,
    # an emtpy string, jibberish, and a single letter
    
    assert reduceAll('boats', wordList) == ["oats", "bats", "bots", "boas", "boat"], 'reduceAll() did not return the correct reductions when given a word'
    assert reduceAll('', wordList) == [] , 'reduceAll() did not return the correct reductions when given an empty string'
    assert reduceAll('jkl;', wordList) == [], 'reduceAll() returned a list of words not in the wordList'
    assert reduceAll('a', wordList) == [], 'reduceAll() did not return an empty string when given one letter'


def reduceTwoAllTests(wordList):
    # This is testing that reduceTwoAll() returns the right reductions when given a valid word,
    # an emtpy string, jibberish, and a single letter
    
    assert reduceTwoAll('eerie', wordList) == ['rie', 'ere', 'rie', 'ere', 'rie', 'eer'], 'reduceTwoAll() did not return the correct reductions by 2'
    assert reduceTwoAll('', wordList) == [] , 'reduceTwoAll() did not return the correct reductions when given an empty string'
    assert reduceTwoAll('jkl;', wordList) == [], 'reduceTwoAll() returned a list of words not in the wordList'
    assert reduceTwoAll('a', wordList) == [], 'reduceTwoAll() did not return an empty string when given one letter'

    
def validateReductionTests(wordList):
    # this is testing that validateReduction() returns the right boolean when given a valid list, 
    # an invalid list, a word with no reduction, and an empty list
    
    assert validateReduction(['turntables', 'turntable', 'turnable', 'tunable', 'unable'], wordList) == True, 'validateReduction() is not returning the correct boolean when given a valid reduction list'
    assert validateReduction(["affidavit"], wordList) == True, 'validateReduction() is not returning the correct boolean when given a list where no reductions exist'
    assert validateReduction(['turntables', 'turnt', 'turnable', 'tunable', 'unable'], wordList) == False, 'validateReduction() is not returning the correct boolean when given an invalid reduction list'
    assert validateReduction(['jkl;'], wordList) == False, 'validateReduction() is not returning the correct boolean when given a word not in wordList'
    
###############################################################    
    

if __name__ == "__main__":
    main()    
    
    
    
    
    
    
    
    
    
    
    
    
    