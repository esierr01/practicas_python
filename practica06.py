'''
Programa que valida si un numero es primo

Un número primo es un número natural (numeros enteros positivos desede 1) que solo puede ser dividido exactamente entre 1 y el mismo.
'''
import os as o
o.system('cls')

class ValidaNúmero:
    def __init__(self) -> None:
        try:
            self.numero_a_validar = int(input("Ingrese número a evaluar: "))

            print(f"El número evaluado ({self.numero_a_validar}) es un número {self.evalua(self.numero_a_validar)}")
        except ValueError:
            print("Número ingresado fue erroneo, programa terminado")
        
    def evalua(self, num):
        if num > 1:            
            if num == 2:
                return "PRIMO"
            else:
                # para determinar si un número es primo, comencemos con el 5, dividimos entre los números menores a el, comenzando por 2, si alguna de estas divisiones da exacta no es un número primo
                # 5 / 2
                # 5 / 3
                # 5 / 4
                for i in range(2, num):
                    if num % i == 0:    # con esto verificamos si la operación tiene residuo
                        return "NO ES PRIMO"
                
                return "PRIMO"
        else:
            return "NO ES PRIMO"

if __name__ == "__main__":
    ValidaNúmero()