#Write programs to understand the use of Python String, Tuple, List, Set, Dictionary, File input/output.

s = "This is String"
print(s)

#This is tuple
t1 = ("item1","item2",10,20)
print(t1.count(10)) #This method takes one argument and returns the number of times an item appears in the tuple.
print(t1.index(10)) #This method takes one argument and returns the index of the first appearance of an item in a tuple.
print("\n\n\n")

#This is List and their methods
l1 = ["item1","item2","item2",30,90,80,30]
print(l1)

l1.append(60) #It adds an item to the end of the list.
print(l1) 

l1.insert(1,70) #It inserts an item at a specified position.
print(l1)  

l1.remove("item1")
print(l1)

l1.pop(3) #It removes the element at the specified index, and prints it to the screen.
print(l1)

print(l1.count(30)) #It returns the count of the item specified.

print(l1.index("item2")) #It returns the first matching index of the item specified.

l1.reverse() #It reverses the order of elements in the Python lists.
print(l1)

l1.clear() #It empties the Python list.
print(l1)

print("\n\n")

#this is set and therir methods
s1 = {1,2,3,10} 
s2 = {4,5,6,10}

print(s1) #access set
print(s2) #access set

s1.discard(3) #This method takes the item to delete as an argument.
print(s1)

s1.remove(1) #Like the discard() method, remove() deletes an item from the set.
print(s1)

s1.add(6) #It takes as argument the item to be added to the set.
print(s1)

s1.update({5,6,9}) #This method can add multiple items to the set at once, which it takes as arguments.
print(s1)

#This is Dictionary 
dict1 = {
    "Name" : "Pj",
    "Class" : "MT12"
}

print(dict1)

#access value 
print(dict1["Name"])

print(dict1.keys()) #The keys() method returns a list of keys in a Python dictionary.

print(dict1.values()) #Likewise, the values() method returns a list of values in the dictionary.

print(dict1.items()) #This method returns a list of key-value pairs.

print(dict1.get("Name")) #It takes one to two arguments. While the first is the key to search for, the second is the value to return if the key isn’t found.

dict1.clear() #The clear function’s purpose is obvious. It empties the Python dictionary.
print(dict1)

# File Handling 

try:
    with open('file.txt','w') as file:
        file.write("testing")
        file.close()
except:
    pass
