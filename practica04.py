'''
Programa para calcular la tabla de multiplicar de cualquier número dado por el usuario.
Debe calcular la tabla del 0 al 12
'''
import os as o
o.system('cls')

class Calcula:
    def __init__(self) -> None:
        try:
            self.numero = int(input('Ingrese número para calcular Tabla: '))
            if self.numero != 0 and self.numero != "":
                self.crea_tabla(self.numero)
            else:
                print('Programa terminado')
        except ValueError:
            print('No ingreso un número válido, programa terminado')

    def crea_tabla(self, num):
        self.tabla = []

        for i in range(13):
            self.tabla.append(self.multiplica(num, i))
        print(f'\nTabla generada del {self.numero}\n')

        # for tabl in self.tabla:
        #     print(tabl)

        # La anterior funciona, pero tambien se puede asi
        print(*self.tabla, sep='\n')

    def multiplica(self, n1, n2):
        return str(n1) + ' + ' + str(n2) + ' = ' + str(n1 * n2)


if __name__ == '__main__':
    Calcula()