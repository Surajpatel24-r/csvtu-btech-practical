#Write  a program to understand  the use of python identifiers,Keywords, identations,Comments in python,operator, membership operators.

#Python keywords are special reserved words that have specific meanings and purposes and can’t be used for anything but those specific purposes. 
#there is "class" which is a keyword

#A comment in Python starts with the hash character, #, and extends to the end of the physical line.

#A Python identifier is a name used to identify a variable, function, class, module or other object. An identifier starts with a letter A to Z or a to z or an underscore (_) followed by zero or more letters, underscores and digits (0 to 9).
#The name of class "mathematic" is identifier

class mathematic:
    #Indentation in Python refers to the (spaces and tabs) that are used at the beginning of a statement.
    def add_two_num(a,b):
        #An operator is a symbol that operates on a value or a variable. For example: + is an operator to perform addition.
        print(a+b)

#An memebership operator is special symbol to access the member function and data member of a class
#There is mathematic is class and add_two_member is member fuction, a (.) is symbol that access the member function
m = mathematic.add_two_num()
