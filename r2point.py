from math import sqrt
from math import inf


class R2Point:
    """ Точка (Point) на плоскости (R2) """

    # Конструктор
    def __init__(self, x=None, y=None):
        if x is None:
            x = float(input("x -> "))
        if y is None:
            y = float(input("y -> "))
        self.x, self.y = x, y
        self.count_p = 0

    # Площадь треугольника
    @staticmethod
    def area(a, b, c):
        return 0.5 * ((a.x - c.x) * (b.y - c.y) - (a.y - c.y) * (b.x - c.x))

    # Лежат ли точки на одной прямой?
    @staticmethod
    def is_triangle(a, b, c):
        return R2Point.area(a, b, c) != 0.0

    # Расстояние до другой точки
    def dist(self, other):
        return sqrt((other.x - self.x)**2 + (other.y - self.y)**2)

    # Лежит ли точка внутри "стандартного" прямоугольника?
    def is_inside(self, a, b):
        return (((a.x <= self.x and self.x <= b.x) or
                 (a.x >= self.x and self.x >= b.x)) and
                ((a.y <= self.y and self.y <= b.y) or
                 (a.y >= self.y and self.y >= b.y)))

    # Освещено ли из данной точки ребро (a,b)?
    def is_light(self, a, b):
        s = R2Point.area(a, b, self)
        return s < 0.0 or (s == 0.0 and not self.is_inside(a, b))

    # Совпадает ли точка с другой?
    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.x == other.x and self.y == other.y
        return False

    @staticmethod
    def eq1(a, b):
        if a.x == b.x and a.y == b.y:
            return 1
        else:
            return 0

    # Метод определения пересечения отрезков
    @staticmethod
    def inters(a, b, c, d):
        if (b.x - a.x) == 0 and (c.x - d.x) == 0:
            if a.x == c.x:
                if (max(c.y, d.y) <= max(a.y, b.y) and
                    max(c.y, d.y) >= min(a.y, b.y)) or \
                    (max(a.y, b.y) <= max(c.y, d.y) and
                        max(a.y, b.y) >= min(c.y, d.y)):
                    return inf
            else:
                return 0
        elif (b.x - a.x) == 0 and (c.x - d.x) != 0:
            k_2 = (c.y - d.y) / (c.x - d.x)
            b_2 = (d.y * c.x - d.x * c.y) / (c.x - d.x)
            if (c.x > a.x and d.x < a.x) or (c.x < a.x and d.x > a.x):
                if (a.y > k_2 * a.x + b_2 and b.y < k_2 * b.x + b_2) or \
                       (a.y < k_2 * a.x + b_2 and b.y > k_2 * b.x + b_2):
                    return 1
                else:
                    return 0
            elif (a.y > k_2 * a.x + b_2 and b.y < k_2 * b.x + b_2) or \
                    (a.y < k_2 * a.x + b_2 and b.y > k_2 * b.x + b_2):
                if (c.x > a.x and d.x < a.x) or (c.x < a.x and d.x > a.x):
                    return 1
                else:
                    return 0
            else:
                return 0
        elif (b.x - a.x) != 0 and (c.x - d.x) == 0:
            k_1 = (b.y - a.y) / (b.x - a.x)
            b_1 = (a.y * b.x - a.x * b.y) / (b.x - a.x)
            if (b.x > c.x and a.x < c.x) or (b.x < c.x and a.x > c.x):
                if (c.y > k_1 * c.x + b_1 and d.y < k_1 * d.x + b_1) or \
                        (c.y < k_1 * c.x + b_1 and d.y > k_1 * d.x + b_1):
                    return 1
                else:
                    return 0
            elif (c.y > k_1 * c.x + b_1 and d.y < k_1 * d.x + b_1) or \
                    (c.y < k_1 * c.x + b_1 and d.y > k_1 * d.x + b_1):
                if (b.x > c.x and a.x < c.x) or (b.x < c.x and a.x > c.x):
                    return 1
                else:
                    return 0
            else:
                return 0
        else:
            k_1 = (b.y - a.y) / (b.x - a.x)
            b_1 = (a.y * b.x - a.x * b.y) / (b.x - a.x)
            k_2 = (c.y - d.y) / (c.x - d.x)
            b_2 = (d.y * c.x - d.x * c.y) / (c.x - d.x)
            if (k_1 == k_2 and b_1 == b_2) and \
                    ((max(c.x, d.x) > min(a.x, b.x) and
                        max(c.x, d.x) <= max(a.x, b.x)) or
                        (max(a.x, b.x) > min(c.x, d.x) and
                            max(a.x, b.x) <= max(c.x, d.x))):
                return inf
            if (c.y < k_1 * c.x + b_1 and d.y > k_1 * d.x + b_1) or \
                    (c.y > k_1 * c.x + b_1 and d.y < k_1 * d.x + b_1):
                if (a.y < k_2 * a.x + b_2 and b.y > k_2 * b.x + b_2) or \
                        (a.y > k_2 * a.x + b_2 and b.y < k_2 * b.x + b_2):
                    return 1
                else:
                    return 0
            elif (a.y < k_2 * a.x + b_2 and b.y > k_2 * b.x + b_2) or \
                    (a.y > k_2 * a.x + b_2 and b.y < k_2 * b.x + b_2):
                if (c.y < k_1 * c.x + b_1 and d.y > k_1 * d.x + b_1) or \
                        (c.y > k_1 * c.x + b_1 and d.y < k_1 * d.x + b_1):
                    return 1
                else:
                    return 0
            else:
                return 0

    # Принадлежит ли точка отрезку
    @staticmethod
    def p_intersect(p, a, b):
        if (b.x - a.x) != 0:
            k = (b.y - a.y) / (b.x - a.x)
            d = (a.y * b.x - a.x * b.y) / (b.x - a.x)
            if (p.y == p.x * k + d) and \
                    ((p.x < a.x and p.x > b.x) or (p.x > a.x and p.x < b.x)):
                return 1
            else:
                return 0
        else:
            if (p.y * 0 == p.x - a.x) and \
                    (p.y > min(a.y, b.y) and p.y < max(a.y, b.y)):
                return 1
            else:
                return 0


if __name__ == "__main__":
    x = R2Point(1.0, 1.0)
    print(type(x), x.__dict__)
    print(x.dist(R2Point(1.0, 0.0)))
    a, b = R2Point(0, 0), R2Point(1, 0)
    c, d = R2Point(0.5, -1.0), R2Point(1.0, 1.0)
    print(R2Point.inters(a, b, c, d))
