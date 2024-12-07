'''
Programa que calcule el IVA de una compra, siendo el IVA el 19% del valor total de la compra
'''
import os as o
o.system('cls')

class CalculaIVA:
    def __init__(self) -> None:
        print('Calculo del IVA de Compra')
        self.valor_compra = float(input('Ingrese el valor total de la compra = '))
        if self.valor_compra != 0 and self.valor_compra != '':
            iva_calculado = self.calcula_iva(self.valor_compra)
            print(f'El valor del IVA calculado de la compra de {self.valor_compra} $ fue de {iva_calculado:.2f} $')
            print(f'La compra total dió {(self.valor_compra + iva_calculado):.2f}')
        else:
            print('Programa terminado')

    def calcula_iva(self, valor_compra):
        return valor_compra * .19


if __name__ == "__main__":
    CalculaIVA()