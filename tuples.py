
# maneras para crear una tuple
x = (1,2 ,3,3,5,3)
y = tuple((4,5,6))
print(x)
print(y)

# cuando hay un solo valor no se considera una tuple al menos que precide de una coma
z  = (1) # no es una tuple es un entero
z1  = (1,) # es una tuple de un solo elemeento

print(dir(x))
print(type(z))
print(z1)

print(x[0]) # muestar el elemento de la posiciond e la tuple 

del x  #elimina la tuple 

print(x.count(3))  # cuenta cuantas veces esta el elemento en la tuple 
print(x.index(5))  #indica  en donde esta la possicion del elemento en la tuple en este caso la respuesta es 4