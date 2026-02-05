import os
from google import genai

# Comandos para configurar el API KEY como variable de entorno (durante la sesión)

#  export GEMINI_API_KEY="TU_API_KEY_AQUI"     (Macos)
#  $env:GEMINI_API_KEY="TU_API_KEY_AQUI"       (Windows)

# El cliente agarra automaticamente la llave de GEMINI_API_KEY (que este como variable de entorno)
client = genai.Client()

def gemini(prompt_text:str) -> str:

    try:
        # Usamos un modelo que soporte generacion de texto e.g., "gemini-2.5-flash".
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt_text
        )
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"



if __name__ == "__main__":
    prompt = "Explícame muy brevemente como estan implementadas las listas en python "
    response_text = gemini(prompt)
    print(response_text)
