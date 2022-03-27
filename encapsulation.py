# 3/27/2022
# Author: Lawrence M
# Encapsulation Submission
# Practicing encapusting functions and variables.

class Protected: 
    def __init__(self):
        self._protectedVar = 12
        """This variable is proctected, denoted by
        the single undescore before the variable
        name. The underscore doesn't change the
        code it is just a warning to self and
        develeopers to not use this variable
        outside of this class."""

    
obj = Protected()
obj._protectedVar = 34
print(obj._protectedVar)

class Protected2:
    """The extra code used to define this class
    ensures that the private variable can not be
    changed unless on purpose."""
    def __init__(self):
        self.__privateVar = 12
        """This variable is private, denoted by
        the double undescore before the variable
        name."""

    def getPrivate(self):
        print(self.__privateVar)
        """The value is retrieved by calling the
        getPrivate() method."""

    def setPrivate(self, private):
        """It has to be set to another value by
        using the setPrivate method"""
        self.__privateVar = private

obj = Protected2()
obj.getPrivate()
obj.setPrivate(23)
obj.getPrivate()
