'''
Se nos pide que validemos si una contraseña nueva definida por el usuario es segura.
Consideraciones para que la contraseña sea segura:
- Tiene más de 8 carácteres
- Tiene al menos una letra mayuscula
- Tiene al menos un número
'''
import os as o
o.system('cls')

class ValidaContrasena:
    def __init__(self) -> None:
        self.contra_validar = input('Ingrese contraseña a evaluar: ')
        if self.contra_validar != "":
            print(f'La contraseña introducida es: {self.valida(self.contra_validar)}')

    def valida(self, contra):
        self.letras_mayuscula = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        self.numeros = "0123456789"
        self.valida1 = False
        self.valida2 = False
        self.valida3 = False

        # primera validación
        if len(contra) > 8:
            self.valida1 = True

        # segunda validación
        for letra in self.letras_mayuscula:
            if letra in contra:
                self.valida2 = True
                break

        # tercera validación
        for num in self.numeros:
            if num in contra:
                self.valida3 = True
                break

        if self.valida1 and self.valida2 and self.valida3:
            return "VALIDA"
        else:
            return "INVALIDA"


if __name__ == '__main__':
    ValidaContrasena()
