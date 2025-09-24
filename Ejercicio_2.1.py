# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 11:27:58 2025

"""

class Persona:
    
    # Método contructor

    def __init__(self, nombre, apellidos, DocumentoIdentidad, anoNacimiento):
        # asigna los valores
        self.nombre = nombre
        self.apellidos = apellidos
        self.DocumentoIdentidad = DocumentoIdentidad
        self.anoNacimiento = anoNacimiento

    # Definir un método que imprima en pantalla los valores de los atributos del objeto.

    def imprimir(self):
        
        print("Nombre = " + self.nombre)
        print("Apellidos = " + self.apellidos)
        print("Número de documento de identidad = " + self.DocumentoIdentidad)
        print("Año de nacimiento = " + str(self.anoNacimiento))


class Ejercicio1Actividad2:

    @staticmethod
    def main():
        persona1 = Persona("Pedro", "Pérez", "1053121010", 1998)
        persona2 = Persona("Luis", "León", "1053223344", 2001)

        persona1.imprimir()
        persona2.imprimir()


# Llamar al método main para ejecutar el programa
if __name__ == "__main__":
    Ejercicio1Actividad2.main()
