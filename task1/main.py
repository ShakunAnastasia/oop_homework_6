import math


class Triangle:
    def __init__(self, a, b, c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        if not self.is_valid():
            raise ValueError(f"Задані сторони не утворюють трикутник: {a}, {b}, {c}")

    def is_valid(self):
        return (self.a > 0 and self.b > 0 and self.c > 0 and
                self.a + self.b > self.c and
                self.b + self.c > self.a and
                self.a + self.c > self.b)

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
        if not self.is_valid():
            raise ValueError(f"Прямокутник з параметрами {a}, {b} не існує")

    def is_valid(self):
        return self.a > 0 and self.b > 0

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b

    def __str__(self):
        return f"Rectangle({self.a}, {self.b})"


class Trapeze:
    def __init__(self, base1, base2, side1, side2):
        self.base1 = float(base1)
        self.base2 = float(base2)
        self.side1 = float(side1)
        self.side2 = float(side2)
        if not self.is_valid():
            raise ValueError(f"Трапеція з параметрами {base1}, {base2}, {side1}, {side2} не існує")

    def is_valid(self):
        if self.base1 <= 0 or self.base2 <= 0 or self.side1 <= 0 or self.side2 <= 0:
            return False
        if self.base1 == self.base2:
            return self.side1 == self.side2
        diff = abs(self.base2 - self.base1) / 2
        discriminant = self.side1 ** 2 - diff ** 2
        return discriminant >= 0 and self.side2 ** 2 - diff ** 2 >= 0

    def perimeter(self):
        return self.base1 + self.base2 + self.side1 + self.side2

    def area(self):
        if self.base1 == self.base2:
            return self.base1 * self.side1
        diff = abs(self.base2 - self.base1) / 2
        height = math.sqrt(self.side1 ** 2 - diff ** 2)
        return (self.base1 + self.base2) * height / 2

    def __str__(self):
        return f"Trapeze({self.base1}, {self.base2}, {self.side1}, {self.side2})"


class Parallelogram:
    def __init__(self, a, b, height):
        self.a = float(a)
        self.b = float(b)
        self.height = float(height)
        if not self.is_valid():
            raise ValueError(f"Паралелограм з параметрами {a}, {b}, {height} не існує")

    def is_valid(self):
        return self.a > 0 and self.b > 0 and self.height > 0

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.height

    def __str__(self):
        return f"Parallelogram({self.a}, {self.b}, {self.height})"


class Circle:
    def __init__(self, radius):
        self.radius = float(radius)
        if not self.is_valid():
            raise ValueError(f"Коло з радіусом {radius} не існує")

    def is_valid(self):
        return self.radius > 0

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle({self.radius})"


def read_shapes_from_file(filename):
    shapes = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split()
            if not parts:
                continue
            shape_type = parts[0]
            try:
                params = list(map(float, parts[1:]))
                if shape_type == "Triangle" and len(params) == 3:
                    shapes.append(Triangle(*params))
                elif shape_type == "Rectangle" and len(params) == 2:
                    shapes.append(Rectangle(*params))
                elif shape_type == "Trapeze" and len(params) == 4:
                    shapes.append(Trapeze(*params))
                elif shape_type == "Parallelogram" and len(params) == 3:
                    shapes.append(Parallelogram(*params))
                elif shape_type == "Circle" and len(params) == 1:
                    shapes.append(Circle(*params))
                else:
                    print(f"Невірна кількість параметрів або невідомий тип: {line.strip()}")
            except ValueError as ve:
                print(f"Помилка у файлі {filename}: {ve}")
    return shapes


def find_max_area_and_perimeter(shapes):
    valid_shapes = [shape for shape in shapes if shape is not None]
    if not valid_shapes:
        return None, None
    max_area_shape = max(valid_shapes, key=lambda shape: shape.area())
    max_perimeter_shape = max(valid_shapes, key=lambda shape: shape.perimeter())
    return max_area_shape, max_perimeter_shape


def write_output(output_file, filename, max_area_shape, max_perimeter_shape):
    with open(output_file, 'a', encoding='utf-8') as file:
        file.write(f"Файл {filename}:\n")
        if max_area_shape:
            file.write(f"  Фігура з найбільшою площею: {max_area_shape}, Площа: {max_area_shape.area():.2f}\n")
        else:
            file.write("  Фігура з найбільшою площею: None\n")
        if max_perimeter_shape:
            file.write(
                f"  Фігура з найбільшим периметром: {max_perimeter_shape}, Периметр: {max_perimeter_shape.perimeter():.2f}\n")
        else:
            file.write("  Фігура з найбільшим периметром: None\n")
        file.write("\n")


def main():
    input_files = ["input01.txt", "input02.txt", "input03.txt"]
    output_file = "output.txt"

    with open(output_file, 'w', encoding='utf-8'):
        pass

    for file in input_files:
        print(f"Обробка файлу: {file}")
        try:
            shapes = read_shapes_from_file(file)
            max_area_shape, max_perimeter_shape = find_max_area_and_perimeter(shapes)
            write_output(output_file, file, max_area_shape, max_perimeter_shape)
            print(f"Результати додано до файлу: {output_file}")
        except Exception as e:
            print(f"Неочікувана помилка у файлі {file}: {e}")
            with open(output_file, 'a', encoding='utf-8') as f:
                f.write(f"Файл {file}:\n  Помилка обробки: {e}\n\n")
        print()


if __name__ == "__main__":
    main()
