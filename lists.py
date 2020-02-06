demo_list = [1,'leo', 1.2, [1,2,3]]
colors = ['red', 'green', 'blue', 'red']

#------- nameras de crear una lista ---------
numbers_list = [1,2,3,4]
numbers_list = list((1,2,3,4))
#print(numbers_list)


# --------lista basado en rago  -------
rango  = list(range(1,10))
#print(rango)

print(dir(colors))
print(len(colors))# cuanto elemenetos hasy en una lista 
print(colors[0]) # muestra las posisciones de la lista 
print(colors[-1]) #muesta la posiscion invera de la lista en este caso es blue 
print('green' in colors) # devuelve si el objeto esta en la lista true o false

print(colors);
colors[1] = 'yellow'; #se le asigna un nuevo velementoalor en la lista con base a su posiscion 
colors.append('violet')# agregar un elemento al fina de la lista 
colors.extend(['gray','pruple']) # agrega varios elemento a un alkista 
colors.insert(1,'violet')  #inserta  un elemento en la lista dada la posicion en este caso en la posisicon 1
colors.insert(len(colors), 'violet') # inserta un valor al final depediendo el tamaño de la lista por eso se utiliza len()
print(colors);
colors.pop() # elimina el elemento final de la lista 
print(colors)
colors.pop(1) # elimina el elemento del indice asignado 
print(colors)

colors.remove('red') # elimina el elemento depediendo el nombre
print(colors)
colors.clear() # elimina todo los elemento e la lista 

#colors.sort() # ordena alfabeticamenete la lista 
print(colors.index('green')) # busca el indice de la poicion de la lista 

print(colors.count('red')) #cuenta cuantas veces se reppite los elemento en las lista




