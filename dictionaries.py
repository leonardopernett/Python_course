product = {
    "nombre":"book",
    "cuantity":3,
    "price":4.99
}

person = {
    "firs_name":"leonardo",
    "last_name":"pernett"
}

print(type(product))
#print(dir(product)) listado de metodos para los dictionaries

print(person.keys()) # muetsra solo las llave del dictionaries en este caso first_name y last_name
print(person.items())  # muestra todo el dictionaries su clave y valor 

del person  #elimina el dictionaries
person.clear() # vacia el dictionaries y lo deja vacip
print(person)

products = [
    {"name":'laptop' ,"price":23232},
    {"name2":'books'}
]

print(products)
