import asyncio, json
from translate import translate_text as translate

def main():

    # Lectura y guardado en diccionario los lenguajes que se manejarán.
    with open("data/languages.json", "r") as document:
        languages = json.load(document)

    dest = languages["hindi"]

    params = {
        "src": "es",
        "dest": "de"
    }

    text = input("Texto a traducir: ")

    translated = asyncio.run(translate(text=text, params=params))

    print(f"\n{translated}\n")


if __name__ == "__main__":
    main()
    