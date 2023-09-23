def contar_letra(string, letra):
    contador = string.lower().count(letra.lower())
    return contador
texto = input("Ingrese un texto: ")
letra = input("Ingrese una letra: ")
resultado = contar_letra(texto, letra)

print(f"La letra '{letra}' aparece {resultado} veces en el texto.")