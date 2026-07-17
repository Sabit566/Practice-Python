print("\n")
#List - allow duplicates, contain different data types

mylist = ['Sabit','Tanvir','Ovi','Wasim','Sabit']
print(f"List: {mylist}")

#List Length

mylist = ['Sabit','Tanvir','Ovi','Wasim','Sabit']
print(f"Length of list: {len(mylist)}")

#Check list class
mylist = ['Sabit','Tanvir','Ovi','Wasim']
print(f"Check type: {type(mylist)}")

#The list() Constructor
thislist = list(("apple","banana","Mango"))
print(f"Using list constructor: {thislist}")

#Acces Items

mylist = ['Sabit','Tanvir','Ovi','Wasim']

print(f"first position item: {mylist[0]}")
print(f"second position item: {mylist[1]}")
print(f"The last position item: {mylist[-1]}")
print(f"The second last position item: {mylist[-2]}")

#Range of indexes
mylist = ['Sabit','Tanvir','Ovi','Wasim','Sabit','Rana']

print(f"Show items position 2 to 5 : {mylist[2:5]}")
print(f"Show items position -5 to -1 : {mylist[-5:-1]}")

#Check if Item Exists

mylist = ['Sabit','Tanvir','Ovi','Wasim','Sabit']
search_name = 'Sabit'
if search_name in mylist:
    print(f"The name {search_name} is present in list")
else:
    print(f"The name {search_name} is not present in list")


#Change Item Value

mylist = ['Sabit','Tanvir','Ovi','Wasim']
mylist[1] = "Jayanto"
print(f"The list after change: {mylist}")

#Change a Range of Item Values

mylist = ['Sabit','Tanvir','Ovi','Wasim']
mylist[1:3] = ["Jayanto","Kabbo"]
print(f"The list after change using range: {mylist}")

#Append Items -To add an item to the end of the list

mylist = ['Sabit','Tanvir','Ovi','Wasim']
thislist.append("Jayanto")
print(f"The list after appending to list: {thislist}")

#Insert Items -To insert a list item at a specified index

mylists = ['Sabit','Tanvir','Ovi','Wasim']
mylists.insert(2, "Jayanto")
print(f"The list after inserting to list: {mylist}")

#Extend List -To append elements from another list to the current list

mylist = ['Sabit','Tanvir','Ovi','Wasim']
yourlist = ['Alok','Fardin','Badhon','Kabbo']

mylist.extend(yourlist)
print(f"The list after extending to list: {mylist}")

#Add Any Iterable -add any iterable object (tuples, sets, dictionaries)

thislist = ['Sabit','Tanvir','Ovi','Wasim']
thistuple = ("Kabbo","Fardin","Badhon")

thislist.extend(thistuple)

print(f"The list after extending to tuple: {thislist}")

#Remove Specified Item -Remove the first occurrence of "banana"

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(f"The list after removing from list: {thislist}")

#Remove Specified Index -removes the specified index
#If you do not specify the index, the pop() method removes the last item.

thislist = ["apple", "banana", "cherry", "kiwi"]
thislist.pop(1)
print(f"The list after removing from list: {thislist}")

thislists = ["apple", "banana", "cherry", "kiwi"]
del thislists[0] # The del keyword also removes the specified index
print(f"The list after removing from list: {thislists}")

del thislists  # Delete the list completely
#print(f"After deleting entire list: {thislists}")
#Error: #this will cause an error because you have successfully deleted "thislist".

#Clear the List -The list still remains, but it has no content
thislists = ["apple", "banana", "cherry", "kiwi"]
thislists.clear()
print(f"The list after clear(): {thislists}")

#Loop Through a List

thislists = ["apple", "banana", "cherry", "kiwi"]

for i, x in enumerate(thislists, start=1):
    print(f"{i}. {x}")

#for x in thislists:
#print(x)

print("\n")

#Loop Through the Index Numbers

thislists = ["apple", "banana", "cherry", "kiwi"]
print(f"The length of list: {len(thislists)}")
for i in range(len(thislists)):
    print(f"{i+1}. {thislists[i]}")

print("\n")

#Using a While Loop

thislists = ["apple", "banana", "cherry", "kiwi"]

i = 0
print("Using a While Loop")
while i < len(thislists):
    print(f"{i}. {thislists[i]}")
    i += 1
print("\n")

#Looping Using List Comprehension -shortest syntax for looping through lists

thislists = ["apple", "banana", "cherry", "kiwi"]

print("Looping Using List Comprehension")
[print(f"{i}. {x}") for i, x in enumerate(thislists, start=1)]

print("\n")

#Based on a list of fruits, you want a new list,
# containing only the fruits with the letter "a" in the name.

fruits = ["apple", "banana", "cherry", "kiwi"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(f"The list items only contains letter 'a' : {newlist}")

