from googletrans import Translator

async def translate_text(params: dict[str, str]) -> str:
    """
    Traduce un texto de un idioma a otro utilizando un servicio de traducción asincrónico.
    Esta función envuelve la funcionalidad del traductor para manejar la traducción
    de texto con parámetros especificados y gestionar errores comunes.
    Args:
        params (dict[str, str]): Diccionario con los parámetros de traducción.
            Parámetros esperados:
            - 'text' (str): Texto a traducir (requerido).
            - 'src' (str): Idioma de origen (opcional).
            - 'dest' (str): Idioma destino (opcional).
            Otros parámetros opcionales según la configuración del servicio de traducción.
    Returns:
        str: Texto traducido.
    Raises:
        SystemExit: Se ejecuta cuando ocurre un error durante la traducción,
            generalmente por idiomas de origen o destino inválidos.
    Example:
        >>> import asyncio
        >>> params = {
        ...     'text': 'Hola mundo',
        ...     'src': 'es',
        ...     'dest': 'en'
        ... }
        >>> resultado = asyncio.run(translate_text(params))
        >>> print(resultado)
        'Hello world'
    """

    
    try:
        async with Translator() as translator:
            result = await translator.translate(**params)
            print(result)
            return result.text

    except:
        print("Tuvimos problemas traduciendo... ¿indicaste una lengua fuente o destino correcta?")
        exit()

