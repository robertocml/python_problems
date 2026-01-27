
class Persona:
    def asignar_nombre(self, nombre: str) -> None:
        self.nombre = nombre





if __name__ == '__main__':

    persona1 = Persona()
    persona2 = Persona()

    persona1.asignar_nombre("Roberto")
    persona2.asignar_nombre("Patricia")

    Persona.asignar_nombre(persona1, "Rob")


    print("Nombre de personas: ", persona1.nombre, persona2.nombre)