# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 12:34:28 2025

"""

from enum import Enum

class tipoPlaneta(Enum):
    GASEOSO = 1
    TERRESTRE = 2
    ENANO = 3


class Planeta:
    
    def __init__(self, nombre, cantidadSatelites, masa, volumen, diametro, distanciaSol, tipo, esObservable):
        self.nombre = nombre
        self.cantidadSatelites = cantidadSatelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distanciaSol = distanciaSol
        self.tipo = tipo
        self.esObservable = esObservable

    def imprimir(self):
        print("Nombre del planeta = " + str(self.nombre))
        print("Cantidad de satélites = " + str(self.cantidadSatelites))
        print("Masa del planeta = " + str(self.masa))
        print("Volumen del planeta = " + str(self.volumen))
        print("Diámetro del planeta = " + str(self.diametro))
        print("Distancia al sol = " + str(self.distanciaSol))
        print("Tipo de planeta = " + str(self.tipo.name))
        print("Es observable = " + str(self.esObservable))

    def calcularDensidad(self):
        return self.masa / self.volumen

    def esPlanetaExterior(self):
        limite = 149597870 * 3.4
        # Un planeta exterior está situado más allá del cinturón de asteroides
        if self.distanciaSol > limite:
            return True
        else:
            return False


class Ejercicio2Actividad2:

    @staticmethod
    def main():
        p1 = Planeta("Tierra", 1, 5.9736E24, 1.08321E12, 12742, 150000000, tipoPlaneta.TERRESTRE, True)
        p1.imprimir()
        print("Densidad del planeta = " + str(p1.calcularDensidad()))
        print("Es planeta exterior = " + str(p1.esPlanetaExterior()))
        print()

        p2 = Planeta("Júpiter", 79, 1.899E27, 1.4313E15, 139820, 750000000, tipoPlaneta.GASEOSO, True)
        p2.imprimir()
        print("Densidad del planeta = " + str(p2.calcularDensidad()))
        print("Es planeta exterior = " + str(p2.esPlanetaExterior()))


if __name__ == "__main__":
    Ejercicio2Actividad2.main()
