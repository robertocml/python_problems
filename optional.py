# Sintaxis: Optional[T] o puede ser str | None


from typing import Optional


def obtener_correo(correo_id: int ) -> Optional[str]:




    correos = { 1: "codeando_unidos@temp.com"}

    return correos.get(correo_id)




if __name__ == "__main__":

    correo = obtener_correo(2)
    
    print("Correo en mayusculas: ", correo.upper() )
    print