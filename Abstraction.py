
#importing the abstract method 
from abc import ABC, abstractmethod
# creating the first class 
class purchase(ABC):
    def Reciept(self, amount):
        print('Your total is: ',amount)

    @abstractmethod
    def payment(self, amount):
        pass
# second class creation
class creditPayment(purchase):

    def payment(self, amount):
        print('You have used {} of your $2000 monthly credit! '.format(amount))
# calling on the functions to work
Object = creditPayment()
Object.Reciept("363.78")
Object.payment("363.78")
