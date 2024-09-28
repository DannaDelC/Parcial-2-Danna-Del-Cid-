#2. Desarrollar un programa con dos funciones. La primera solicite el ingreso de un entero y muestre el cuadrado de dicho valor.
#La segunda que solicite la carga de dos valores y muestre el producto de los mismos. Llamar desde el bloque del programa principal a ambas funciones. 
def mostrarcuadrado():
    numero = int(input("Ingrese un número entero: "))
    cuadrado = numero ** 2
    print(f"El cuadrado de {numero} es: {cuadrado}")

def mostrarproducto():
    num1 = float(input("Ingrese un primer valor: "))
    num2 = float(input("Ingrese un segundo valor: "))
    producto = num1 * num2
    print(f"El producto de {num1} y {num2} es: {producto}")

def main():
    mostrarcuadrado()  
    mostrarproducto()  

if __name__ == "__main__":
    main()
