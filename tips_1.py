
a = 10
b = 20

a,b = b,a

print(f"a = {a}, b = {b}")


mensaje: str = [1,2,3]

print(mensaje[::-1])


asteriscos = "*"

print(asteriscos * 10)


nombres = ["Patricia", "Paola", "Roberto"]

print("Nombres: ", ", ".join(nombres))


informacion = {"Roberto" : 29}


print(informacion.get("Patricia", "No se encontro la llave"))