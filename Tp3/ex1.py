import math
class Vecteur3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def coincide(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z
    def normax(self, other):
        norm1 = math.sqrt(self.x**2 + self.y**2 + self.z**2)
        norm2 = math.sqrt(other.x**2 + other.y**2 + other.z**2)
        return self if norm1 >= norm2 else other
    def __add__(self, other):
        return Vecteur3D(self.x + other.x, self.y + other.y, self.z + other.z)
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

if __name__ == "__main__":
    v1 = Vecteur3D(1,2,3)
    v2 = Vecteur3D(4,5,6)
    v3 = v1 + v2
    print("Vecteur v1 :", v1)
    print("Vecteur v2 :", v2)
    print("Vecteur v3 (v1 + v2) :", v3)
    print("v1 et v2 ont les memes composantes :", v1.coincide(v2))
    print("Le vecteur avec la plus grande norme :", v1.normax(v2))
