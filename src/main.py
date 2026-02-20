import asyncio, json
from translate import translate_text as translate

def main():

    # Lectura y guardado en diccionario los lenguajes que se manejarán.
    with open("data/languages.json", "r") as document:
        languages = json.load(document)
 

if __name__ == "__main__":
    main()
    