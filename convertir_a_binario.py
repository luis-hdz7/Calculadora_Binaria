from pilas import Pila
def decimal_a_binario(numero):
    if numero == 0:
        return "0"
    pila = Pila()
    # Dividir y apilar residuos
    while numero > 0:
        residuo = numero % 2
        pila.apilar(residuo)
        numero = numero // 2

    # Desapilar para formar binario
    binario = ""
    while not pila.esta_vacia():
            binario += str(pila.desapilar())
    return binario
# Ejemplo
def main():
    while True:
        opcion=input(f"""\n¿Qué opcion desea realizar
> 1.Convertir un decimal a binario
> 2.Salir del sistema
> """)
        match opcion:
            case "1":
                while True:
                    try:
                        numero =int(input(f"\nIngrese el numero que desea convertir a binario: "))
                        if numero<0:
                            raise ValueError("El numero no puede ser negativo")
                        resultado = decimal_a_binario(numero)
                        print(f"{numero} en binario: {resultado}")
                        break
                    except ValueError as e:
                        print("Debe ingresar un valor valido",e)
            case "2":
                print(f"\nGracias por usar nuestro sistema")
                break
            case _:
                print("\nValor no reconocido intentelo otra vez")
if __name__=="__main__":
    main()