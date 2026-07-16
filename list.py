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

mylist = ['Sabit','Tanvir','Ovi','Wasim']
mylist.insert(2, "Jayanto")
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