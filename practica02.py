'''
Script que reciba 3 notas de un estudiante y calcule nota final 
NOTA: tomar en cuenta que las 2 primeras notas valen 30% cada una de la nota y la última un 40%
'''
import os as o
o.system('cls')

class Calcula:
    def __init__(self) -> None:
        print('Módulo de calculo de nota final de estudiante (3 notas, la 1 y 2 valen 30% c/u y la 3 40%)')
        self.nota_1 = float(input("Introduzca nota 1 = "))
        self.nota_2 = float(input("Introduzca nota 2 = "))
        self.nota_3 = float(input("Introduzca nota 3 = "))
        
        if (self.nota_1!='' and self.nota_1!=0):
            print(f'El resultado del promedio del estudiante fue: {(self.calcula_promedio(self.nota_1, self.nota_2, self.nota_3)):.2f} Puntos')
        else:
            print('Programa terminado')

    def calcula_promedio(self, n1, n2, n3):
        return (n1 * 0.3) + (n2 * 0.3) + (n3 * 0.4)

if __name__ == "__main__":
    Calcula()
