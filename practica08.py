'''
Programa que pide dos números al usuario y una operación matemática a efectuar con los números
'''
import os as o

class OperacionCalcula:
    def __init__(self) -> None:
        while True:
            o.system('cls')

            try:
                self.num1 = float(input('Introduzca el primer número: '))
                self.num2 = float(input('Introduzca el segundo número: '))

                print("(s) para suma")
                print("(r) para restar el primero menos el segundo")
                print("(m) multiplicar los dos números")
                print("(d) dividir el primer número entre el segundo")
                print("(e) exponenciación (el primero es la base y el segundo el índice)")
                print("(q) raiz (el primer número es el radicando y el segundo es el índice)")
                print("(0) Para salir")
                self.opcion = input("Indique opción deseada _")
                if self.opcion == 0:
                     print("Programa terminado")
                     break
                self.operacion(self.num1, self.num2, self.opcion)   
                input("Presione cualquier tecla para continuar ........")             
            except ValueError:
                print("Datos incompletos, programa terminado")
                break

    def operacion(self, num1, num2, opcion):
        match opcion:
            case "s":
                print(f"La suma de {self.num1} + {self.num2} dio {self.num1 + self.num2}")
            case "r":
                print(f"La resta de {self.num1} - {self.num2} dio {self.num1 - self.num2}")
            case "m":
                print(f"La multiplicación de {self.num1} * {self.num2} dio {self.num1 * self.num2}")
            case "d":
                print(f"La división de {self.num1} / {self.num2} dio {self.num1 / self.num2}")
            case "e":
                print(f"La exponenciación de {self.num1} elevado a  {self.num2} dio {self.num1 ** self.num2}")
            case "q":
                print(f"La raiz de {self.num1} con indice  {self.num2} dio {self.num1 ** (1 / self.num2)}")
        


if __name__ == "__main__":
    OperacionCalcula()