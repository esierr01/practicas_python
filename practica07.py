'''
Programa que calcule el nuevo salario de un trabajador si el mismo recibió un aumento de # %
'''
import os as o
o.system('cls')

class Aumento:
    def __init__(self) -> None:
        while True:
            try:
                self.sueldo_anterior = float(input("Ingrese sueldo inicial: "))                
                if self.sueldo_anterior == 0:
                    print("Programa terminado ....")
                    break
                else:
                    self.porcen_aumento = float(input("Indique porcentaje de aumento %: "))
                    print(f"El nuevo sueldo del empleado es {self.calcula_sueldo(self.sueldo_anterior, self.porcen_aumento)}")
            except ValueError:
                print("Ingreso un dato erroneo, vuelva a intentar")

    def calcula_sueldo(self, actual, aumento):
        return ((actual * aumento) / 100) + actual

if __name__ == "__main__":
    Aumento()