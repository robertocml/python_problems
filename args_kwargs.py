

def saludar(nombre):
    print(f"Hola {nombre}")


saludar("Roberto")




def ejemplo( *args ):
    print(args)


ejemplo(1, 2, 3, 4, 5, 6, 7)



def sumar( *args ):
    total = 0
    for numero in args:
        total += numero
    return total

print(sumar(1, 2, 3, 4, 5, 6, 7))




def ejemplo( **kwargs ):
    print(kwargs)

ejemplo(nombre="Roberto", edad=25, sexo="M")