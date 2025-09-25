import math

class Circulo:  
    def __init__(self, radio):
        self.radio = radio  
    def area(self):  
        return math.pi * (self.radio ** 2)  
    def perimetro(self):  
        return 2 * math.pi * self.radio  



class Rectangulo:  
    def __init__(self, base, altura):  
        self.base = base 
        self.altura = altura 
    def area(self):  
        return self.base * self.altura  
    def perimetro(self): 
        return 2 * (self.base + self.altura)  



class Cuadrado:  
    def __init__(self, lado):  
        self.lado = lado  
    def area(self):  
        return self.lado * self.lado  
    def perimetro(self):  
        return 4 * self.lado  



class TrianguloRectangulo: 
    def __init__(self, base, altura):  
        self.base = base  
        self.altura = altura  
    def area(self): 
        return (self.base * self.altura) / 2  
    def hipotenusa(self):  
        return math.sqrt(self.base ** 2 + self.altura ** 2)  
    def perimetro(self):  
        return self.base + self.altura + self.hipotenusa()  
    def tipo_triangulo(self):  
        h = round(self.hipotenusa(), 5)  
        b = round(self.base, 5)  
        a = round(self.altura, 5)  
        if a == b == h: 
            return "Equilátero"
        elif a == b or b == h or a == h:  
            return "Isósceles"
        else:  
            return "Escaleno"



class Rombo:  
    def __init__(self, diagonal_mayor, diagonal_menor, lado):  
        self.D = diagonal_mayor  
        self.d = diagonal_menor  
        self.lado = lado  
    def area(self): 
        return (self.D * self.d) / 2  
    def perimetro(self):  
        return 4 * self.lado 



class Trapecio:  
    def __init__(self, base_mayor, base_menor, lado1, lado2, altura): 
        self.B = base_mayor  
        self.b = base_menor 
        self.lado1 = lado1 
        self.lado2 = lado2  
        self.altura = altura  
    def area(self):  
        return ((self.B + self.b) * self.altura) / 2  
    def perimetro(self):  
        return self.B + self.b + self.lado1 + self.lado2  
    


def main():
    print("  CÍRCULO  ")
    c = Circulo(5)  
    print("Área:", c.area())  
    print("Perímetro:", c.perimetro())  
    print("\n   RECTÁNGULO  ")
    r = Rectangulo(4, 6)  
    print("Área:", r.area())  
    print("Perímetro:", r.perimetro())  
    print("\n   CUADRADO   ")
    q = Cuadrado(4)  
    print("Área:", q.area())  
    print("Perímetro:", q.perimetro())  
    print("\n   TRIÁNGULO RECTÁNGULO   ")
    t = TrianguloRectangulo(3, 4) 
    print("Área:", t.area())  
    print("Hipotenusa:", t.hipotenusa())  
    print("Perímetro:", t.perimetro()) 
    print("Tipo de triángulo:", t.tipo_triangulo())  
    print("\n   ROMBO   ")
    rom = Rombo(10, 8, 6)  
    print("Área:", rom.area())  
    print("Perímetro:", rom.perimetro())  
    print("\n=== TRAPECIO ===")
    tra = Trapecio(10, 6, 5, 5, 4)  
    print("Área:", tra.area())  
    print("Perímetro:", tra.perimetro())  

if __name__ == "__main__":
    main()