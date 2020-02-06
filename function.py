 #crear una funcion con el prefijo def 
def hello(name="anonimo"):           
    print(f"hello {name}")

hello("leonardo")
hello("pedro")
hello("andres")
hello()

def add(num1, num2):
    return (num1 + num2)


print(add(10,20))


 #funciones de una sola linea con lambda
add = lambda num1 , num2 : num1 + num2   

print(add(10,30))