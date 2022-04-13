class Protected:
    def __init__(self):
        self.protectedVar = 0

object = Protected()
object._protectedVar = 'This code is protected!'
print(object._protectedVar)



class Private:
    def __init__(self):
        self.__privateVar = 'This is a private variable!'

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

object = Private()
object.getPrivate()
object.setPrivate(45)
object.getPrivate()