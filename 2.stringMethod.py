print("\n")
#Assign String to a Variable

a = "Hello World"
print("Assign String to a Variable: ",a)

print("\n")

#Multiline Strings

a ="""Hello 
    World"""
print("Multiline Strings: ",a)

print("\n")

#Strings are Arrays

a = "Hello World"
print("a[0] = ",a[0])
print("a[0:2] = ", a[0:2])
print("a[2:] = ", a[2:])
print("a[:] = ", a[:])
print("a[:3] = ",a[:3])
print("a[-3:] = ", a[-3:])
print("a[-3:-1] = ", a[-3:-1])

print("\n")

#Looping Through a String
print("Looping Through a String -(Gamma): ")
for x in "Gamma":
 print(x)

print("\n")

#String Length
a = "Hello World"
print("String Length : ",len(a))

print("\n")

#Check String
text = "My name is David"
print("Find word in text: " + str("David" in text))  #Convert the boolean to a string
print("Find word in text: ", "David" in text)  #Use commas in print()
print(f"Find word in text: {'David' in text }")  #Use an f-string (Most Pythonic)

print("\n")

#Use it in an if statement

text = "Ay Duniya pittal de"
if "Duniya" in text:
    print("Word is found in the text")  #True
else:
    print("Word is not in the text")  #False

print("\n")

#Check if NOT
text = "Your are a ass h*le"
if "ass" not in text:
    print("Word is not in the text")
else:
    print("Word is found in the text")