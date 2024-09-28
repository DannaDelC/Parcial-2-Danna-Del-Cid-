#1 Plantear una función que reciba un string en mayuscula o minusculas y retorne la cantidad de letras ´a´ o ´A´.

def contar_letras_a(texto):
    contador = 0
    for caracter in texto:
        if caracter == 'a' or caracter == 'A':
            contador += 1
    return contador

cadena = "Danna Lucrecia Del Cid López"
cantidad_a = contar_letras_a(cadena)
print(f"La cantidad de letras 'a' o 'A' en '{cadena}' es: {cantidad_a}")
