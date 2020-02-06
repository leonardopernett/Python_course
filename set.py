colors = {'red', 'blue', 'yellow'}

print(dir(colors))
print(type(colors));
print(colors);
print('red' in colors) # condicion que dice si un elemento esta en los set devuelve true
colors.add('green') # agregar un elemento sin inportar la possicion porque no tiene un indice 
print(colors); 
colors.remove('blue') # elimina el elemento blue del set
print(colors);
colors.clear()# elimina todos los elemento del set
del colors #elimina el set
print(colors)  
