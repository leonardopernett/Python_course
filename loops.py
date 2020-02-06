foods = ['cheese', 'milk', 'meail', 'apple'];

print(foods[0])
print(foods[1])
print(foods[2])
print(foods[3])

for food in foods:
    if food == "milk":
       break #teermina el bucle for 
    print(food)

for food in foods:
    if food == "milk":
       continue #continua el bucle for 
    print(food)  

for number in range(1,100):
    print(number)
    
for letter in "hello":
    print(letter)

count = 4

while count <=10 :
    print(count)
    count = count + 1
