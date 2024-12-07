'''
Audio Libro en Python

pip install gtts
'''
import os as o
from gtts import gTTS
o.system('cls')

class AudioLibro:
    def __init__(self) -> None:
        self.archivo = input("Ingrese el Nombre del Archivo fuente: ")
        if self.archivo != "":
            if o.path.isfile(self.archivo):
                self.genera_mp3(self.archivo)
                print("Archivo de audio generado ... Programa terminado con éxito")
            else: 
                print('El archivo indicado no existe, programa terminado')
        else:
            print('Programa terminado')

    def genera_mp3(self, archivo):
        self.file = open(archivo, 'r', encoding='utf-8')
        self.text_archivo = self.file.read()
        self.file.close()

        self.audio = gTTS(text=self.text_archivo, lang='es')
        self.nombre_audio = archivo.rsplit('.', 1)[0]
        self.audio.save(f'{self.nombre_audio}.mp3')

if __name__ == "__main__":
    AudioLibro()

