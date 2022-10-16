from r2point import R2Point
from convex import Figure, Void, Point, Segment, Polygon
from math import inf


class Test1:

    def setup_method(self):
        self.f = Point(R2Point(0.0, 2.0))
        Figure.point_a = R2Point(-1.0, 0.5)
        Figure.point_b = R2Point(1.0, 0.5)
        Figure.point_c = R2Point(0.0, 0.0)

    # Точка не принадлежит треугольнику
    def test1_power(self):
        assert self.f.power() == 0


class Test2:

    def setup_method(self):
        self.f = Point(R2Point(0.0, 0.0))
        Figure.point_a = R2Point(-1.0, 0.5)
        Figure.point_b = R2Point(1.0, 0.5)
        Figure.point_c = R2Point(0.0, 0.0)

    # Точка принадлежит треугольнику
    def test2_power(self):
        assert self.f.power() == 1


class Test3:

    def setup_method(self):
        self.f = Segment(R2Point(0.0, 0.0), R2Point(2.0, 2.0))
        Figure.point_a = R2Point(0.0, 0.0)
        Figure.point_b = R2Point(1.0, 0.0)
        Figure.point_c = R2Point(0.0, 1.0)

    # пересечение отрезка и фиксированного треугольника
    def test3_power(self):
        assert self.f.power() == 2

    # Пересечение двух треугольников
    def test4_power(self):
        print('4')
        assert self.f.add(R2Point(-1.0, 2.0)).power() == 2

    # При добавлении точки до треугольника количество точек пересечения
    # бесконечно
    def test5_power(self):
        print('5')
        assert self.f.add(R2Point(0.0, 2.0)).power() == inf


class Test4:

    def setup_method(self):
        self.f = Segment(R2Point(0.0, 0.0), R2Point(1.0, 0.5))
        Figure.point_a = R2Point(1.0, 0.0)
        Figure.point_b = R2Point(0.0, 1.0)
        Figure.point_c = R2Point(0.0, 0.0)

    # пересечение двух треугольников
    def test6_power(self):
        assert self.f.add(R2Point(-1.0, 0.5)).power() == 4

    # Добавление точки до 4-хугольника
    def test7_power(self):
        assert self.f.add(R2Point(-1.0, 0.5)).add(
            R2Point(0.0, 2.0)).power() == 2

    # Добавление точки до 5-тиугольника
    def test8_power(self):
        assert self.f.add(R2Point(-1.0, 0.5)).add(
            R2Point(0.0, 2.0)).add(R2Point(1.0, -1.0)).power() == 1

    # Добавление точки до 6-тиугольника
    def test9_power(self):
        assert self.f.add(R2Point(-1.0, 0.5)).add(
            R2Point(0.0, 2.0)).add(
            R2Point(1.0, -1.0)).add(R2Point(2.0, 0.0)).power() == 0


class Test5:

    def setup_method(self):
        self.f = Segment(R2Point(0.0, 0.0), R2Point(2.0, 0.0))
        Figure.point_a = R2Point(1.0, 0.0)
        Figure.point_b = R2Point(0.0, 1.0)
        Figure.point_c = R2Point(0.0, 0.0)

    # пересечение двух треугольников бесконечно
    def test10_power(self):
        assert self.f.add(R2Point(0.0, 2.0)).power() == inf

    # при добавлении точки до 4-хугольника количество точек пересечния остается
    # бесконечным
    def test11_power(self):
        assert self.f.add(R2Point(0.0, 2.0)).add(
            R2Point(1.0, 1.0)).power() == inf

    # при добавлении до 5-тиугольника количество точек пересечения уже не
    # бесконечно
    def test12_power(self):
        assert self.f.add(R2Point(0.0, 2.0)).add(
            R2Point(1.0, 1.0)).add(R2Point(-1.0, -1.0)).power() == 0
