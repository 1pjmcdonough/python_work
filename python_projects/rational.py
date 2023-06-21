# -*- coding: utf-8 -*-
"""
Defining a Rational number class

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Phillip McDonough
"""
__version__ = 1

class Rational:
    '''
    Initialize a new Rational object with value iNum/iDen stored in hidden __numerator and
    __denominator variables.  Calls the reduce() method to put the fraction in lowest terms.
    '''
    def __init__(self, iNum, iDen):
        self.__numerator = iNum
        self.__denominator = iDen
        self.reduce()
        
    '''
    Returns the object's numerator. 
    '''    
    def getNumerator(self):
        return self.__numerator
    
    '''
    Returns the object's denominator. 
    ''' 
    def getDenominator(self):
        return self.__denominator
    
    '''
    Changes the object's numerator. 
    ''' 
    def setNumerator(self, n):
        self.__numerator = n
        self.reduce()
        
    '''
    Changes the object's denominator. 
    '''     
    def setDenominator(self, d):
        self.__denominator = d
        self.reduce()   
        
    '''
    Validates the object does not have a zero denominator. Returns a boolean.
    '''
    def isValid(self):
        denom = self.__denominator
        if denom == 0:
            return False
        else:
            return True
    
    '''Adds one Rational object, num2, to another Rational object.'''
    def add(self, num2):
        num2Num = num2.getNumerator()      
        num2Denom = num2.getDenominator()  
        selfNum = self.__numerator         
        selfDenom = self.__denominator     

        if selfDenom == num2Denom:
            self.__numerator = selfNum + num2Num
            self.reduce()
        else:
            num2Num = num2.getNumerator() * selfDenom   
            num2Denom = num2.getDenominator() * selfDenom
            selfNum = self.__numerator * num2.getDenominator()       
            selfDenom = self.__denominator * num2.getDenominator()
            self.__denominator = selfDenom        
            self.__numerator = selfNum + num2Num
            self.reduce()

    '''Subtracts one Rational object, num2, from another Rational object.'''
    def sub(self, num2):
        num2Num = num2.getNumerator()      
        num2Denom = num2.getDenominator()  
        selfNum = self.__numerator         
        selfDenom = self.__denominator     

        if selfDenom == num2Denom:
            self.__numerator = selfNum - num2Num
            self.reduce()
        else:
            num2Num = num2.getNumerator() * selfDenom   
            num2Denom = num2.getDenominator() * selfDenom
            selfNum = self.__numerator * num2.getDenominator()       
            selfDenom = self.__denominator * num2.getDenominator()
            self.__denominator = selfDenom        
            self.__numerator = selfNum - num2Num
            self.reduce()
    
    '''Multiplies one Rational object with another Rational object.'''
    def mult(self, num2):
        num2Num = num2.getNumerator()      
        num2Denom = num2.getDenominator()  
        selfNum = self.__numerator         
        selfDenom = self.__denominator
        
        self.__denominator = selfDenom * num2Denom
        self.__numerator = selfNum * num2Num
        self.reduce()
        
    '''Divides one Rational object by another Rational object, num2.'''
    def div(self, num2):
        num2Num = num2.getNumerator()      
        num2Denom = num2.getDenominator()  
        selfNum = self.__numerator         
        selfDenom = self.__denominator
        
        self.__denominator = selfDenom * num2Num
        self.__numerator = selfNum * num2Denom
        self.reduce()
        
    ################################
    #    HELPER FUNCTIONS BELOW    #
    ################################
    '''
    Reduces the Rational to lowest terms
      - Checks if both the numerator and denominator are negative; if so, makes both positive
      - Calls gcf() to find the greatest common factor between the numerator and denominator, and
        continues to divide by that gcf until the greatest common factor is 1
    '''
    def reduce(self):
        if self.__numerator < 0 and self.__denominator < 0:
            self.__numerator = -self.__numerator
            self.__denominator = -self.__denominator
        common = 0
        while (common != 1):
            common = self.gcf()
            self.__numerator /= common
            self.__denominator /= common
    
    '''
    Determines the greatest common factor between the numerator and denominator
      - Starts checking numbers counting downward from the smaller of the numerator,denominator pair
      - When it finds a number divisble by both, it breaks the loop and returns that number
      - The smallest number that can be returned is 1
    '''
    def gcf(self):
        common_factor = 1
        for i in range(min(abs(int(self.__numerator)), abs(int(self.__denominator))), 1, -1):
            if self.__numerator % i == 0 and self.__denominator % i == 0:
                 common_factor = i
                 break
        return common_factor
    
    '''
    Returns a string representation of the Rational, e.g. "1/8"
    '''
    def __str__(self):
        return str(int(self.__numerator)) + "/" + str(int(self.__denominator))
    
    '''
    Determines if two Rationals are exactly equal to each other (same numerator and same
    denominator, no consideration of reducing the numbers)
    '''
    def __eq__(self, r2):
        return self.__numerator == r2.__numerator and self.__denominator == r2.__denominator
    
    ################################
    #     END HELPER FUNCTIONS     #
    ################################    

def main():
    testGetters()
    testSetters()
    testisValid()
    testaddAndsub()
    testmultAnddiv()
        
###############################################################

def testGetters():
    # Testing getter functions return the correct numerator and denominator.
    assert Rational(3,4).getNumerator() == 3, 'getNumerator(3,4) is not returning the right numerator.'
    assert Rational(-4,8).getNumerator() == -1, 'getNumerator(-4,8) is not returning the right numerator.'
    assert Rational(6,0).getNumerator() == 6, 'getNumerator(6,0) is not returning the right numerator.'
    assert Rational(4,-2).getNumerator() == 2, 'getNumerator(4,-2) is not returning the right numerator.'
    
    assert Rational(3,4).getDenominator() == 4, 'getNumerator(3,4) is not returning the right numerator.'
    assert Rational(-4,8).getDenominator() == 2, 'getNumerator(4,8) is not returning the right numerator.'
    assert Rational(6,0).getDenominator() == 0, 'getNumerator(6,0) is not returning the right numerator.'
    assert Rational(4,-2).getDenominator() == -1, 'getNumerator(4,2) is not returning the right numerator.'
    
def testSetters():
    # Testing setter functions change the numerator and denominator correctly.
    x = Rational(3,4)
    x.setNumerator(0)
    assert x.getNumerator() == 0, 'Rational(3,4).setNumerator(0) is not returning the right numerator.'
    x = Rational(-4,8)
    x.setNumerator(8)
    assert x.getNumerator() == 4, 'Rational(4,8).setNumerator(8) is not returning the right numerator.'
    x = Rational(6,0)
    x.setNumerator(-11)
    assert x.getNumerator() == -11, 'Rational(6,0).setNumerator(11) is not returning the right numerator.'
    x = Rational(4,2)
    x.setNumerator(6)
    assert x.getNumerator() == 6, 'Rational(4,2).setNumerator(6) is not returning the right numerator.'
    
    y = Rational(3,-4)
    y.setDenominator(0)
    assert y.getDenominator() == 0, 'Rational(3,4).setDenominator(0) is not returning the right numerator.'
    y = Rational(4,8)
    y.setDenominator(-4)
    assert y.getDenominator() == -4, 'Rational(4,8).setDenominator(4) is not returning the right numerator.'
    y = Rational(-6,0)
    y.setDenominator(3)
    assert y.getDenominator() == 1, 'Rational(6,0).setDenominator(3) is not returning the right numerator.'
    y = Rational(4,2)
    y.setDenominator(8)
    assert y.getDenominator() == 4, 'Rational(4,2).setDenominator(8) is not returning the right numerator.'

def testisValid():
    # Testing isValid() returns False if there is a zero in the denominator and True otherwise.
    assert Rational(7,4).isValid() == True, 'Rational(7,4).isValid() is not returning True'
    assert Rational(-7,0).isValid() == False, 'Rational(-7,0).isValid() is not returning False'
    assert Rational(0,0).isValid() == False, 'Rational(11,0).isValid() is not returning False'
    assert Rational(2,4).isValid() == True, 'Rational(2,4).isValid() is not returning True'
    
def testaddAndsub():
    # Testing add() and sub() add and subtract rational objects correctly
    x = Rational(1,4)
    x.add(Rational(1,8))
    assert x == Rational(3,8), 'Rational(1,4).add(Rational(1,8)) is not adding correctly'
    x = Rational(1,2)
    x.add(Rational(-3,6))
    assert x == Rational(0,2), 'Rational(1,2).add(Rational(-3,6)) is not adding correctly'
    x = Rational(0,4)
    x.add(Rational(2,4))
    assert x == Rational(1,2), 'Rational(0,4).add(Rational(2,4)) is not adding correctly'
    x = Rational(4,-10)
    x.add(Rational(2,3))
    assert x == Rational(4,15), 'Rational(4,-10).add(Rational(2,3)) is not adding correctly'
    
    y = Rational(1,4)
    y.sub(Rational(1,8))
    assert y == Rational(1,8), 'Rational(1,4).sub(Rational(1,8)) is not subtracting correctly'
    y = Rational(1,2)
    y.sub(Rational(3,6))
    assert y == Rational(0,2), 'Rational(1,2).sub(Rational(3,6)) is not subtracting correctly'
    y = Rational(0,4)
    y.sub(Rational(2,4))
    assert y == Rational(-1,2), 'Rational(0,4).sub(Rational(2,4)) is not subtracting correctly'
    y = Rational(8,-10)
    y.sub(Rational(2,3))
    assert y == Rational(22,-15), 'Rational(8,-10).sub(Rational(2,3)) is not subtracting correctly'
    
def testmultAnddiv():
    # Testing mult() and div() add and subtract rational objects correctly
    x = Rational(1,4)
    x.mult(Rational(1,8))
    assert x == Rational(1,32), 'Rational(1,4).mult(Rational(1,8)) is not multiplying correctly'
    x = Rational(1,2)
    x.mult(Rational(-3,6))
    assert x == Rational(-1,4), 'Rational(1,2).mult(Rational(-3,6)) is not multiplying correctly'
    x = Rational(0,4)
    x.mult(Rational(2,4))
    assert x == Rational(0,8), 'Rational(0,4).mult(Rational(2,4)) is not multiplying correctly'
    x = Rational(4,-10)
    x.mult(Rational(2,3))
    assert x == Rational(4,-15), 'Rational(4,-10).mult(Rational(2,3)) is not multiplying correctly'
    
    y = Rational(1,4)
    y.div(Rational(1,8))
    assert y == Rational(2,1), 'Rational(1,4).div(Rational(1,8)) is not dividing correctly'
    y = Rational(1,2)
    y.div(Rational(3,6))
    assert y == Rational(1,1), 'Rational(1,2).div(Rational(3,6)) is not dividing correctly'
    y = Rational(0,4)
    y.div(Rational(2,4))
    assert y == Rational(0,4), 'Rational(0,4).div(Rational(2,4)) is not dividing correctly'
    y = Rational(8,-10)
    y.div(Rational(2,3))
    assert y == Rational(6,-5), 'Rational(8,-10).div(Rational(2,3)) is not dividing correctly'

###############################################################    
    
if __name__ == "__main__":
    main()