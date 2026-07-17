#Without List Comprehension

car = ['audi', 'bmw', 'toyota','honda']
newcar = []
for x in car:
    if 'o' in x:
        newcar.append(x)

print(newcar)

#with list comprehension

car = ['audi', 'bmw', 'toyota','honda']

newcar = [x for x in car if 'o' in x]
print(newcar)

newcar1 = [x for x in car if x != 'o']
print(newcar1)