import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        
    def perimeter(self):
        return self.a + self.b + self.c
    
    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def __str__(self):
        return f"Triangle({self.a}, {self.b}, {self.c})"

class Rectangle:
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)
        
    def perimeter(self):
        return 2 * (self.a + self.b)
    
    def area(self):
        return self.a * self.b
    
    def __str__(self):
        return f"Rectangle({self.a}, {self.b})"

class Trapeze:
    def __init__(self, a, b, c, d):
        self.a = float(a) 
        self.b = float(b) 
        self.c = float(c) 
        self.d = float(d) 
        
    def perimeter(self):
        return self.a + self.b + self.c + self.d
    
    def area(self):
        h = math.sqrt(self.c**2 - (((self.b - self.a)**2 + self.c**2 - self.d**2) / (2 * (self.b - self.a)))**2)
        return (self.a + self.b) * h / 2
    
    def __str__(self):
        return f"Trapeze({self.a}, {self.b}, {self.c}, {self.d})"

class Parallelogram:
    def __init__(self, a, b, h):
        self.a = float(a)  
        self.b = float(b)  
        self.h = float(h)  
        
    def perimeter(self):
        return 2 * (self.a + self.b)
    
    def area(self):
        return self.a * self.h
    
    def __str__(self):
        return f"Parallelogram({self.a}, {self.b}, {self.h})"

class Circle:
    def __init__(self, r):
        self.r = float(r)
        
    def perimeter(self):
        return 2 * math.pi * self.r
    
    def area(self):
        return math.pi * self.r * self.r
    
    def __str__(self):
        return f"Circle({self.r})"

# створюємо об'єкт фігури з рядка
def create_shape(line):
    parts = line.strip().split()
    shape_type = parts[0]
    
    if shape_type == "Triangle":
        return Triangle(parts[1], parts[2], parts[3])
    elif shape_type == "Rectangle":
        return Rectangle(parts[1], parts[2])
    elif shape_type == "Trapeze":
        return Trapeze(parts[1], parts[2], parts[3], parts[4])
    elif shape_type == "Parallelogram":
        return Parallelogram(parts[1], parts[2], parts[3])
    elif shape_type == "Circle":
        return Circle(parts[1])
    return None

# обробка файлу
def process_file(filename):
    shapes = []
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                shape = create_shape(line)
                if shape:
                    shapes.append(shape)
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено")
        return None, None
    
    if not shapes:
        print("Список фігур порожній")
        return None, None
    
    max_area_shape = max(shapes, key=lambda x: x.area())
    max_perimeter_shape = max(shapes, key=lambda x: x.perimeter())
    
    return max_area_shape, max_perimeter_shape

def main():
    files = ["input01.txt", "input02.txt", "input03.txt"]
    
    for filename in files:
        print(f"\nОбробка файлу: {filename}")
        max_area_shape, max_perimeter_shape = process_file(filename)
        
        if max_area_shape and max_perimeter_shape:
            print(f"Фігура з найбільшою площею: {max_area_shape}")
            print(f"Площа: {max_area_shape.area():.2f}")
            print(f"Фігура з найбільшим периметром: {max_perimeter_shape}")
            print(f"Периметр: {max_perimeter_shape.perimeter():.2f}")

if __name__ == "__main__":
    main()
