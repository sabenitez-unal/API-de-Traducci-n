import asyncio
from translate import translate_text as translate

def main():
    params = dict()

    params["text"] = input()
 
    texto = asyncio.run(translate(params))
    print(texto)

if __name__ == "__main__":
    main()
    