class Account:
    def __init__(self, sOwner, iID, fBalance):
        '''
    Initialize a new Account object with value sOwner stored in __owner,
    iID stored in __id, and fBalance stored in __balance.
    '''
        self.__owner = sOwner
        self.__id = iID
        self.__balance = fBalance
        
    '''
    Returns the name of the account owner.
    '''    
    def getOwner(self):
        return self.__owner
    
    '''
    Returns the account ID.
    '''
    def getID(self):
        return self.__id
    
    '''
    Returns the account balance.
    '''
    def getBalance(self):
        return self.__balance
    
    '''
    Changes the name of the account owner.
    '''
    def setOwner(self, sOwner):
        self.__owner = sOwner
        
    '''
    Changes the account ID.
    '''
    def setID(self, iID):
        self.__id = iID
    
    '''
    Changes the account balance.
    '''
    def setBalance(self, fBalance):
        self.__balance = fBalance
        
    '''
    Adds a deposit amount into the account balance.
    '''
    def deposit(self, amount):
        self.__balance += amount 
    
    '''
    Subtracts a withdrawl amount from the account balance.
    If the account balance falls below 0, there is a $5 penaly charge.
    '''
    def withdraw(self, amount):
        self.__balance -= amount
        if self.__balance < 0:
            print('Warning: account balance below zero. A $5 penalty will be deducted from account.')
            self.__balance -= 5
    
    '''
    Prints the account owner, ID, and balance.
    '''    
    def printAccountInfo(self):
        print('  Account Owner:', self.__owner)
        print('     Account ID:', self.__id)
        print('Account Balance:', self.__balance)


class CheckingAccount(Account):
    '''
    Initialize a new CheckingAccount object and inherits the Account class.  
    Initializes __transactionCount to 0 and stores iTF in __transactionFee.
    '''
    def __init__(self, sOwner, iID, fBalance, iTF):
        self.__transactionCount = 0
        self.__transactionFee = iTF
        super().__init__(sOwner, iID, fBalance)
    
    '''
    Returns the transaction count.
    ''' 
    def getTransactionCount(self):
        return self.__transactionCount 
        
    '''
    Returns the transaction fee.
    ''' 
    def getTransactionFee(self):
        return self.__transactionFee
    
    '''
    Changes the transaction count by iTC.
    ''' 
    def setTransactionCount(self, iTC):
        self.__transactionCount += iTC
        
    '''
    Changes the transaction fee.
    ''' 
    def setTransactionFee(self, iTF):
        self.__transactionFee = iTF
    
    '''
    Adds a deposit amount into the account balance, adds 1 to the transaction
    count and calls the deductFees() method.
    '''
    def deposit(self, amount):
        super().deposit(amount)
        self.__transactionCount += 1
        self.deductFees()
    
    '''
    Subtracts a withdrawl amount from the account balance.
    If the account balance falls below 0, there is a $5 penaly charge. 
    Adds 1 to the transaction count and calls the deductFees() method.
    '''
    def withdraw(self, amount):
        super().withdraw(amount)
        self.__transactionCount += 1
        self.deductFees()
    
    '''
    Deducts the transaction fee from a account balance if the transaction 
    count is 5 and resets transaction count back to 0.
    '''
    def deductFees(self):
        if self.__transactionCount == 5:
            self.setBalance(self.getBalance() - self.__transactionFee)
            self.setTransactionCount(0)
            

class SavingsAccount(Account):
    '''
    Initialize a new SavingsAccount object and inherits the Account class.  
    Stores fIR in __interestRate.
    '''
    def __init__(self, sOwner, iID, fBalance, fIR):
        self.__interestRate = fIR
        super().__init__(sOwner, iID, fBalance)
    
    '''
    Returns the interest rate.
    '''
    def getInterestRate(self):
        return self.__interestRate
    
    '''
    Changes the interest rate.
    '''
    def setInterestRate(self, fIR):
        self.__interestRate = fIR
    
    '''
    Subtracts a withdrawl amount from the account balance.
    If the account balance falls below 0, there is a $5 penaly charge. 
    Sets the interest rate to 0.
    '''
    def withdraw(self, amount):
        super().withdraw(amount)
        self.__interestRate = 0
        
    '''
    Applys the interest rate to an account balance.
    '''
    def applyInterest(self):
        self.setBalance(self.getBalance() * (1 + self.__interestRate))
            
            
def main():
    testAccountGetters()
    testAccountSetters()
    testAccount()
    testCheckingAccountGetters()
    testCheckingAccountSetters()
    testCheckingAccount()
    testSavingsAccountGetters()
    
############################################################    
    
def testAccountGetters():
    # Testing account getter functions return the correct values
    account = Account('Rick', 137, 42.0)
    account1 = Account('Morty', 14, 24.0)
    
    assert account.getOwner() == 'Rick', "getOwner() is returning the wrong owner; != Rick."
    assert account1.getOwner() == 'Morty', "getOwner() is returning the wrong owner; != Morty."
    
    assert account.getID() == 137, 'getID() is returning the wrong ID; != 137.'
    assert account1.getID() == 14, 'getID() is returning the wrong ID; != 14.'
    
    assert account.getBalance() == 42.0, 'getBalance() is returning the wrong balance; != 42.0.'
    assert account1.getBalance() == 24.0, 'getBalance() is returning the wrong balance; != 24.0.'
    
def testAccountSetters():
    # Testing account setter functions return the correct values
    account = Account('Rick', 137, 42.0)
    
    account.setOwner('Beth')
    assert account.getOwner() == 'Beth', "setOwner('Beth') is returning the wrong owner."
    account.setOwner('Summer')
    assert account.getOwner() == 'Summer', "setOwner('Summer') is returning the wrong owner."
    
    account.setID(1)
    assert account.getID() == 1, 'setID(1) is returning the wrong ID.'
    account.setID(1234)
    assert account.getID() == 1234, 'setID(1234) is returning the wrong ID.'
    
    account.setBalance(52.86)
    assert account.getBalance() == 52.86, 'setBalance(52.86) is returning the wrong ID.'
    account.setBalance(-123.56)
    assert account.getBalance() == -123.56, 'setBalance(-123.56) is returning the wrong ID.'
    
def testAccount():
    # Tests the deposit and withdraw methods of the Account class add to 
    # and subtract from the account balance, respectively
    account = Account('Morty', 14, 24.0)
    
    account.deposit(1000.5)
    assert account.getBalance() == 1024.5, 'deposit(1000.5) is returning the wrong balance.'
    account.deposit(50)
    assert account.getBalance() == 1074.5, 'deposit(50) is returning the wrong balance.'
    
    account.withdraw(1012)
    assert account.getBalance() == 62.5, 'withdraw(1012) is returning the wrong balance.'
    account.withdraw(63)
    assert account.getBalance() == -5.5, 'withdraw(63) is returning the wrong balance.'
    
def testCheckingAccountGetters():
    # Testing CheckingAccount getters return the correct values
    account = CheckingAccount('Jerry', 23, 45.45, 5.0)
    
    assert account.getTransactionCount() == 0, 'getTransactionCount() is returning the wrong count; != 0.'
    account.deposit(5)
    account.withdraw(5)
    assert account.getTransactionCount() == 2, 'getTransactionCount() is returning the wrong count; != 2.'
    
    assert account.getTransactionFee() == 5.0, 'getTransactionFee() is returning the wrong count; != 5.0.'
    account.setTransactionFee(15.5)
    assert account.getTransactionFee() == 15.5, 'getTransactionFee() is returning the wrong count; != 15.5.'
    
def testCheckingAccountSetters():
    # Testing CheckingAccount setters return the correct values
    account = CheckingAccount('Jerry', 23, 45.45, 5.0)
    
    account.setTransactionCount(7)
    assert account.getTransactionCount() == 7, 'setTransactionCount() is returning the wrong count; != 7.'
    account.setTransactionCount(2)
    assert account.getTransactionCount() == 9, 'setTransactionCount() is returning the wrong count; != 9.'
    
    account.setTransactionFee(2.0)
    assert account.getTransactionFee() == 2.0, 'getTransactionFee() is returning the wrong count; != 2.0.'
    account.setTransactionFee(4.2)
    assert account.getTransactionFee() == 4.2, 'getTransactionFee() is returning the wrong count; != 4.2.'
    
def testCheckingAccount():
    # Tests the deposit and withdraw methods of the CheckingAccount class add to 
    # and subtract from the account balance, respectively
    account = CheckingAccount('Rob', 1, 3000, 4.5)
    
    account.deposit(5)
    assert account.getBalance() == 3005, 'deposit(5) is returning the wrong balance.'
    account.deposit(50)
    assert account.getBalance() == 3055, 'deposit(5) is returning the wrong balance.'
    
    account.withdraw(5)
    assert account.getBalance() == 3050, 'withdraw(5) is returning the wrong balance.'
    account.withdraw(3000)
    assert account.getBalance() == 50, 'withdraw(3000) is returning the wrong balance.'
    
    #testing deductFees()
    account.deposit(5)
    assert account.getBalance() == 50.5, 'deductFees() is not deducting the correct fees; != 50.5.'
    account.deductFees()
    assert account.getBalance() == 46.0, 'deductFees() is not deducting the correct fees; != 46.0.'
    
def testSavingsAccountGetters():
    # Testing SavingsAccount getters return the correct values
    account = SavingsAccount('Dan', 1, 3000, .2)
    
    assert account.getInterestRate() == .2, 'getInterestRate() is not returning the correct rate; != .2.'
    account.setInterestRate(.5)
    assert account.getInterestRate() == .5, 'getInterestRate() is not returning the correct rate; != .5.'
    

def testSavingsAccountSetters():
    # Testing SavingsAccount setters return the correct values
    account = SavingsAccount('Larry', 96, 34, .22)
    
    account.setInterestRate(.4)
    assert account.getInterestRate() == .4, 'setInterestRate(.4) is not returning the correct rate.'
    account.setInterestRate(.34)
    assert account.getInterestRate() == .34, 'setInterestRate(.34) is not returning the correct rate.'
    
def testSavingsAccount():
    # Tests the withdraw method of the SavingsAccount class
    # subtracts from the account balance and the applyInterest method
    # applies the correct interest rate
    account = SavingsAccount('Ben', 7, 1000000, .8)
    
    account.withdraw(1000)
    assert account.getBalance() == 999000, 'withdraw(1000) is returning the wrong balance.'
    assert account.getInterestRate() == 0, 'withdraw(1000) is returning the wrong interest rate.'
    
    account.applyInterest()
    assert account.balance() == 1798200, 'applyInterest() is returning the wrong balance; != 1798200.'
    account.applyInterest()
    assert account.balance() == 3236760, 'applyInterest() is returning the wrong balance; != 3236760'

############################################################    
    
if __name__ == "__main__":    
    main()