# Creating first class for the protected variable
class Protected:
    def __init__(self):
        self.protectedVar = 0

object = Protected()
object._protectedVar = 'This code is protected!'
print(object._protectedVar)


# Creating second class for the private variable
class Private:
    def __init__(self):
        self.__privateVar = 'This is a private variable!'

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private
# Calling them to work
object = Private()
object.getPrivate()
object.setPrivate(45)
object.getPrivate()