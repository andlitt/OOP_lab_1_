class Triangle:

    def __init__(self, a, b, c, alpha, beta, gamma):

        if not self.is_triangle_existence(a, b, c):
            raise ValueError(
                "Треугольник существует, когда сумма длин любых "
                "двух его сторон больше длины третьей стороны"
            )
        self.a = a
        self.b = b
        self.c = c

        if not (alpha + beta + gamma == 180):
            raise ValueError("Сумма углов треугольника должна быть равна 180 градусов")
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma

    # Проверка условия существования сторон треугольника
    def is_triangle_existence(self, a, b, c):
        return (a < b + c) and (b < a + c) and (c < a + b)

    def read(self):
        try:
            a = float(input("Введите длину стороны a "))
            b = float(input("Введите длину стороны b "))
            c = float(input("Введите длину стороны c "))

            if not self.is_triangle_existence(a, b, c):
                print(
                    "Ошибка: Треугольник существует, когда сумма длин "
                    "любых двух его сторон больше длины третьей стороны"
                )
                return False

            self.a = a
            self.b = b
            self.c = c

            alpha = float(input("Введите угол alpha  "))
            beta = float(input("Введите угол beta   "))
            gamma = float(input("Введите угол gamma  "))

            if not (alpha + beta + gamma == 180):
                print("Сумма углов треугольника должна быть 180 градусов")
                return False

            self.alpha = alpha
            self.beta = beta
            self.gamma = gamma
            return True

        except ValueError:
            print("Ошибка: Введите числовые значения")
            return False

    def display(self):
        print(f"Длина сторон:\n a = {self.a}\n b = {self.b}\n c = {self.c}\n")
        print(
            f"Величниа углов:\n alpha = {self.alpha}\n "
            f"beta = {self.beta}\n gamma = {self.gamma}\n"
        )
        print(f"Периметр: {self.perimeter()}")
        print(f"Площадь: {self.area():.1f}")
        height_a = self.сalculating_height(self.a)
        print(f"Высота, проведенная к стороне a: {height_a:.1f}")
        triangle_type = self.triangle_type(
            self.a, self.b, self.c, self.alpha, self.beta, self.gamma
        )
        print(f"Вид треугольника: {triangle_type}")

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        p = self.perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def сalculating_height(self, side):
        return 2 * self.area() / side

    def triangle_type(self, a, b, c, alpha, beta, gamma):
        type_triangle = "Обычный"

        triangle_angles = [alpha, beta, gamma]

        if (a == b) or (a == c) or (b == c):
            type_triangle = "Равнобедренный"
        if (alpha == beta == gamma == 60) and (a == b == c):
            type_triangle = "Равносторонний"

        for angle in triangle_angles:
            if ((a == b) or (a == c) or (b == c)) and (angle == 90):
                type_triangle = "Прямоугольный и равнобедренный"
                continue
            if angle == 90:
                type_triangle = "Прямоугольный"
        return type_triangle
