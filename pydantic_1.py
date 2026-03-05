from pydantic import BaseModel, EmailStr, ValidationError, field_validator

class Usuario(BaseModel):
    nombre: str
    edad: int
    email: EmailStr

    @field_validator("edad")
    @classmethod
    def validar_edad(cls, value):
        if not 25 <= value <= 35:
            raise ValueError("La edad debe estar entre 25 y 35 años")
        return value



usuario = Usuario(
    nombre="Roberto",
    edad="29",  # string que se convierte a int
    email="roberto@email.com"
)

print("Usuario: ", usuario)
print()
print("Datatype de edad: ", type(usuario.edad))  # int
print()

# Caso inválido
try:
    Usuario(
        nombre="Ana",
        edad=45,
        email="correo_invalido"
    )
except ValidationError as e:
    print(e)