my_str = "hello world" 

print(dir(my_str))  #listado de todos los metodo del string

#method string
print(my_str.title()) # string como titulo
print(my_str.upper()) # string mayuscula
print(my_str.lower()) # strign minuscula
print(my_str.capitalize()) # primera letra en mayuscula
print(my_str.replace('hello', 'bye').upper()) # reemplaza el texto del string por uno nuevo
print(my_str.count('l')) #cuneta los caracteres del string
print(my_str.startswith("hello")) # con que empieza el string returna falso o verdadero
print(my_str.endswith("world")) # con que termina el string returna falso o verdadero
print(my_str.split()) # divir el string
valor = my_str.split()
print(valor[1])
print(my_str.find('o')) # encuentra la psosicion del string sino encuentra el valor en el string devuelve -1

#ejemplo 
if(my_str.find('world') != -1):
    print('si esta en el string')
else :
    print('no esta en el string')

print(len(my_str)) # buscar la longitud del string
print(my_str.index('e')) #buscar el indice seleccionado del string

print(my_str.isnumeric()) # comrpueba si el string es numerico
print(my_str.isalpha())   # compara si el extring es alphanumerico
print(my_str[6]) #muestra el caracter del string en este caso es  "w"
print(my_str[-1]) # nuestra el caracter del string pero cuando es -1 es el inverso es decir seria la letra "d"


# tipos concatenaciones en python
name= "leonardo"
print("mi nombre es: " , name)
print("mi bombre es: " + name)
print(f"mi nombre es: {name}")