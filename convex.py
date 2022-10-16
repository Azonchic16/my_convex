from deq import Deq
from r2point import R2Point
from math import inf


class Figure:
    """ Абстрактная фигура """

    def perimeter(self):
        return 0.0

    def area(self):
        return 0.0


class Void(Figure):
    """ "Hульугольник" """

    def add(self, p):
        return Point(p)


class Point(Figure):
    """ "Одноугольник" """

    def __init__(self, p):
        self.p = p
        self.counter = 0

    def power(self):
        if R2Point.p_intersect(self.p, self.point_a, self.point_b) == 1 or \
                R2Point.p_intersect(self.p, self.point_b,
                                    self.point_c) == 1 or \
                R2Point.p_intersect(self.p, self.point_a,
                                    self.point_c) == 1:
            self.counter += 1
        elif R2Point.eq1(self.p, self.point_a) == 1 or \
                R2Point.eq1(self.p, self.point_b) == 1 or \
                R2Point.eq1(self.p, self.point_c) == 1:
            self.counter += 1
        return self.counter

    def add(self, q):
        return self if self.p == q else Segment(self.p, q)


class Segment(Figure):
    """ "Двуугольник" """

    def __init__(self, p, q):
        self.p, self.q, = p, q
        self.count = int()

    def perimeter(self):
        return 2.0 * self.p.dist(self.q)

    def power(self):
        s_1 = R2Point.inters(self.p, self.q, self.point_a, self.point_b)
        s_2 = R2Point.inters(self.p, self.q, self.point_a, self.point_c)
        s_3 = R2Point.inters(self.p, self.q, self.point_b, self.point_c)
        a_eq1 = R2Point.eq1(self.point_a, self.p)
        a_eq2 = R2Point.eq1(self.point_a, self.q)
        b_eq1 = R2Point.eq1(self.point_b, self.p)
        b_eq2 = R2Point.eq1(self.point_b, self.q)
        c_eq1 = R2Point.eq1(self.point_c, self.p)
        c_eq2 = R2Point.eq1(self.point_c, self.q)
        a_1 = R2Point.p_intersect(self.point_a, self.p, self.q)
        b_1 = R2Point.p_intersect(self.point_b, self.p, self.q)
        c_1 = R2Point.p_intersect(self.point_c, self.p, self.q)
        p_1 = R2Point.p_intersect(self.p, self.point_a, self.point_b)
        p_2 = R2Point.p_intersect(self.p, self.point_a, self.point_c)
        p_3 = R2Point.p_intersect(self.p, self.point_b, self.point_c)
        q_1 = R2Point.p_intersect(self.q, self.point_a, self.point_b)
        q_2 = R2Point.p_intersect(self.q, self.point_a, self.point_c)
        q_3 = R2Point.p_intersect(self.q, self.point_b, self.point_c)
        intersect = [a_eq1, a_eq2, b_eq1, b_eq2,
                     c_eq1, c_eq2, a_1, b_1, c_1,
                     s_1, s_2, s_3, p_1, p_2, p_3, q_1, q_2, q_3]
        return sum(intersect)

    def st(self, q, r):
        return Segment(self.q, self.r)

    def add(self, r):
        if R2Point.is_triangle(self.p, self.q, r):
            return Polygon(self.p, self.q, r)
        elif self.q.is_inside(self.p, r):
            return Segment(self.p, r)
        elif self.p.is_inside(r, self.q):
            return Segment(r, self.q)
        else:
            return self


class Polygon(Figure):
    """ Многоугольник """

    def __init__(self, a, b, c):
        self.points = Deq()
        self.points.push_first(b)
        if b.is_light(a, c):
            self.points.push_first(a)
            self.points.push_last(c)
        else:
            self.points.push_last(a)
            self.points.push_first(c)
        self._perimeter = a.dist(b) + b.dist(c) + c.dist(a)
        self._area = abs(R2Point.area(a, b, c))
        self.counter = 0
        self.inf1 = 0
        self.inf2 = 0
        self.inf3 = 0
        if self.points.size() == 3:
            self.inf1 = 0
            self.inf2 = 0
            self.inf3 = 0
            self.counter = 0
            # Пересечение первой стороны с фиксированном треугольником
            s1_ab = R2Point.inters(self.points.first(), self.points.second(),
                                   self.point_a, self.point_b)
            s1_ac = R2Point.inters(self.points.first(), self.points.second(),
                                   self.point_a, self.point_c)
            s1_bc = R2Point.inters(self.points.first(), self.points.second(),
                                   self.point_b, self.point_c)
            s1_a = R2Point.p_intersect(self.point_a, self.points.first(),
                                       self.points.second())
            s1_b = R2Point.p_intersect(self.point_b, self.points.first(),
                                       self.points.second())
            s1_c = R2Point.p_intersect(self.point_c, self.points.first(),
                                       self.points.second())
            s1_list = []
            s1_list.extend([s1_ab, s1_ac, s1_bc, s1_a, s1_b, s1_c])
            # Пересечение второй стороны с фиксировонным треугольником
            s2_ab = R2Point.inters(self.points.first(), self.points.last(),
                                   self.point_a, self.point_b)
            s2_ac = R2Point.inters(self.points.first(), self.points.last(),
                                   self.point_a, self.point_c)
            s2_bc = R2Point.inters(self.points.first(), self.points.last(),
                                   self.point_b, self.point_c)
            s2_a = R2Point.p_intersect(self.point_a, self.points.first(),
                                       self.points.last())
            s2_b = R2Point.p_intersect(self.point_b, self.points.first(),
                                       self.points.last())
            s2_c = R2Point.p_intersect(self.point_c, self.points.first(),
                                       self.points.last())
            s2_list = []
            s2_list.extend([s2_ab, s2_ac, s2_bc, s2_a, s2_b, s2_c])
            # Пересечение третьей стороны с фиксированном треугольником
            s3_ab = R2Point.inters(self.points.second(), self.points.last(),
                                   self.point_a, self.point_b)
            s3_ac = R2Point.inters(self.points.second(), self.points.last(),
                                   self.point_a, self.point_c)
            s3_bc = R2Point.inters(self.points.second(), self.points.last(),
                                   self.point_b, self.point_c)
            s3_a = R2Point.p_intersect(self.point_a, self.points.second(),
                                       self.points.last())
            s3_b = R2Point.p_intersect(self.point_b, self.points.second(),
                                       self.points.last())
            s3_c = R2Point.p_intersect(self.point_c, self.points.second(),
                                       self.points.last())
            s3_list = []
            s3_list.extend([s3_ab, s3_ac, s3_bc, s3_a, s3_b, s3_c])
            # Лежит ли точка first на фиксированном треугольнике
            first_eq_a = R2Point.eq1(self.points.first(), self.point_a)
            first_eq_b = R2Point.eq1(self.points.first(), self.point_b)
            first_eq_c = R2Point.eq1(self.points.first(), self.point_c)
            first_ab = R2Point.p_intersect(self.points.first(), self.point_a,
                                           self.point_b)
            first_ac = R2Point.p_intersect(self.points.first(), self.point_a,
                                           self.point_c)
            first_bc = R2Point.p_intersect(self.points.first(), self.point_b,
                                           self.point_c)
            first_list = []
            first_list.extend([first_eq_a, first_eq_b, first_eq_c,
                               first_ab, first_ac, first_bc])
            self.points.first().count_p = sum(first_list)
            # Лежит ли точка second на фиксированном треугольнике
            second_eq_a = R2Point.eq1(self.points.second(), self.point_a)
            second_eq_b = R2Point.eq1(self.points.second(), self.point_b)
            second_eq_c = R2Point.eq1(self.points.second(), self.point_c)
            second_ab = R2Point.p_intersect(self.points.second(),
                                            self.point_a, self.point_b)
            second_ac = R2Point.p_intersect(self.points.second(),
                                            self.point_a, self.point_c)
            second_bc = R2Point.p_intersect(self.points.second(),
                                            self.point_b, self.point_c)
            second_list = []
            second_list.extend([second_eq_a, second_eq_b, second_eq_c,
                                second_ab, second_ac, second_bc])
            self.points.second().count_p = sum(second_list)
            # Лежит ли точка last на фиксированном треугольнике
            last_eq_a = R2Point.eq1(self.points.last(), self.point_a)
            last_eq_b = R2Point.eq1(self.points.last(), self.point_b)
            last_eq_c = R2Point.eq1(self.points.last(), self.point_c)
            last_ab = R2Point.p_intersect(self.points.last(),
                                          self.point_a, self.point_b)
            last_ac = R2Point.p_intersect(self.points.last(),
                                          self.point_a, self.point_c)
            last_bc = R2Point.p_intersect(self.points.last(),
                                          self.point_b, self.point_c)
            last_list = []
            last_list.extend([last_eq_a, last_eq_b, last_eq_c,
                              last_ab, last_ac, last_bc])
            self.points.last().count_p = sum(last_list)
            # Складываем все атрибуты в один список
            triangle_attributes = []
            triangle_attributes += (s1_list + s2_list +
                                    s3_list + first_list +
                                    second_list + last_list)
            for i in range(len(triangle_attributes)):
                if triangle_attributes[i] == inf:
                    if self.inf1 == 0 and self.inf2 == 0 and self.inf3 == 0:
                        self.inf1 = inf
                    elif self.inf1 == inf and \
                            self.inf2 == 0 and self.inf3 == 0:
                        self.inf2 = inf
                    elif self.inf1 == inf and \
                            self.inf2 == inf and self.inf3 == 0:
                        self.inf3 = inf
                elif triangle_attributes[i] != 0:
                    self.counter += triangle_attributes[i]

    def perimeter(self):
        return self._perimeter

    def area(self):
        return self._area

    # добавление новой точки
    def add(self, t):

        # поиск освещённого ребра
        for n in range(self.points.size()):
            if t.is_light(self.points.last(), self.points.first()):
                s2_ab = R2Point.inters(self.points.first(), self.points.last(),
                                       self.point_a, self.point_b)
                s2_ac = R2Point.inters(self.points.first(), self.points.last(),
                                       self.point_a, self.point_c)
                s2_bc = R2Point.inters(self.points.first(), self.points.last(),
                                       self.point_b, self.point_c)
                s2_a = R2Point.p_intersect(self.point_a,
                                           self.points.first(),
                                           self.points.last())
                s2_b = R2Point.p_intersect(self.point_b,
                                           self.points.first(),
                                           self.points.last())
                s2_c = R2Point.p_intersect(self.point_c,
                                           self.points.first(),
                                           self.points.last())
                s2_list = []
                s2_list.extend([s2_ab, s2_ac, s2_bc, s2_a, s2_b, s2_c])
                for i in range(len(s2_list)):
                    if s2_list[i] == inf:
                        if self.inf1 == inf:
                            self.inf1 = 0
                        elif self.inf1 == 0 and self.inf2 == inf:
                            self.inf2 = 0
                        else:
                            self.inf3 = 0
                    else:
                        self.counter -= s2_list[i]
                break
            self.points.push_last(self.points.pop_first())

        # хотя бы одно освещённое ребро есть
        if t.is_light(self.points.last(), self.points.first()):

            # учёт удаления ребра, соединяющего конец и начало дека
            self._perimeter -= self.points.first().dist(self.points.last())
            self._area += abs(R2Point.area(t,
                                           self.points.last(),
                                           self.points.first()))

            # удаление освещённых рёбер из начала дека
            p = self.points.pop_first()
            while t.is_light(p, self.points.first()):
                self.counter -= p.count_p
                # считаем количество точек пересечения для удаляемого ребра
                s_ab = R2Point.inters(p, self.points.first(),
                                      self.point_a, self.point_b)
                s_ac = R2Point.inters(p, self.points.first(),
                                      self.point_a, self.point_c)
                s_bc = R2Point.inters(p, self.points.first(),
                                      self.point_b, self.point_c)
                s_a = R2Point.p_intersect(self.point_a,
                                          p, self.points.first())
                s_b = R2Point.p_intersect(self.point_b,
                                          p, self.points.first())
                s_c = R2Point.p_intersect(self.point_c,
                                          p, self.points.first())
                s_list = []
                s_list.extend([s_ab, s_ac, s_bc, s_a, s_b, s_c])
                for i in range(len(s_list)):
                    if s_list[i] == inf:
                        if self.inf1 == inf:
                            self.inf1 = 0
                        elif self.inf1 == 0 and self.inf2 == inf:
                            self.inf2 = 0
                        else:
                            self.inf3 = 0
                    else:
                        self.counter -= s_list[i]
                self._perimeter -= p.dist(self.points.first())
                self._area += abs(R2Point.area(t, p, self.points.first()))
                p = self.points.pop_first()
            self.points.push_first(p)

            # удаление освещённых рёбер из конца дека
            p = self.points.pop_last()
            while t.is_light(self.points.last(), p):
                self.counter -= p.count_p
                # считаем количество точек пересечения для удаляемого ребра
                s_ab = R2Point.inters(p, self.points.last(),
                                      self.point_a, self.point_b)
                s_ac = R2Point.inters(p, self.points.last(),
                                      self.point_a, self.point_c)
                s_bc = R2Point.inters(p, self.points.last(),
                                      self.point_b, self.point_c)
                s_a = R2Point.p_intersect(self.point_a,
                                          p, self.points.last())
                s_b = R2Point.p_intersect(self.point_b,
                                          p, self.points.last())
                s_c = R2Point.p_intersect(self.point_c,
                                          p, self.points.last())
                s_list = []
                s_list.extend([s_ab, s_ac, s_bc, s_a, s_b, s_c])
                for i in range(len(s_list)):
                    if s_list[i] == inf:
                        if self.inf1 == inf:
                            self.inf1 = 0
                        elif self.inf1 == 0 and self.inf2 == inf:
                            self.inf2 = 0
                        else:
                            self.inf3 = 0
                    else:
                        self.counter -= s_list[i]
                self._perimeter -= p.dist(self.points.last())
                self._area += abs(R2Point.area(t, p, self.points.last()))
                p = self.points.pop_last()
            self.points.push_last(p)

            # добавление двух новых рёбер
            self._perimeter += t.dist(self.points.first()) + \
                t.dist(self.points.last())
            self.points.push_first(t)

            s1_ab = R2Point.inters(self.points.first(), self.points.second(),
                                   self.point_a, self.point_b)
            s1_ac = R2Point.inters(self.points.first(), self.points.second(),
                                   self.point_a, self.point_c)
            s1_bc = R2Point.inters(self.points.first(), self.points.second(),
                                   self.point_b, self.point_c)
            s1_a = R2Point.p_intersect(self.point_a,
                                       self.points.first(),
                                       self.points.second())
            s1_b = R2Point.p_intersect(self.point_b,
                                       self.points.first(),
                                       self.points.second())
            s1_c = R2Point.p_intersect(self.point_c,
                                       self.points.first(),
                                       self.points.second())
            s1_list = []
            s1_list.extend([s1_ab, s1_ac, s1_bc, s1_a, s1_b, s1_c])
            # Считаем атрибут для второго добавленного ребра
            s2_ab = R2Point.inters(self.points.first(), self.points.last(),
                                   self.point_a, self.point_b)
            s2_ac = R2Point.inters(self.points.first(), self.points.last(),
                                   self.point_a, self.point_c)
            s2_bc = R2Point.inters(self.points.first(), self.points.last(),
                                   self.point_b, self.point_c)
            s2_a = R2Point.p_intersect(self.point_a,
                                       self.points.first(), self.points.last())
            s2_b = R2Point.p_intersect(self.point_b,
                                       self.points.first(), self.points.last())
            s2_c = R2Point.p_intersect(self.point_c,
                                       self.points.first(), self.points.last())
            s2_list = []
            s2_list.extend([s2_ab, s2_ac, s2_bc, s2_a, s2_b, s2_c])
            # Лежит ли добавленная точка на фиксированном треугольнике
            first_eq_a = R2Point.eq1(self.points.first(), self.point_a)
            first_eq_b = R2Point.eq1(self.points.first(), self.point_b)
            first_eq_c = R2Point.eq1(self.points.first(), self.point_c)
            first_ab = R2Point.p_intersect(self.points.first(),
                                           self.point_a, self.point_b)
            first_ac = R2Point.p_intersect(self.points.first(),
                                           self.point_a, self.point_c)
            first_bc = R2Point.p_intersect(self.points.first(),
                                           self.point_b, self.point_c)
            first_list = []
            first_list.extend([first_eq_a, first_eq_b, first_eq_c,
                               first_ab, first_ac, first_bc])
            self.points.first().count_p = sum(first_list)

            # прибавляем к счетчику пересечения новых сторон
            attributes = []
            attributes = (s1_list + s2_list)
            self.counter += self.points.first().count_p
            for i in range(len(attributes)):
                if attributes[i] == inf:
                    if self.inf1 == 0 and \
                            self.inf2 == 0 and self.inf3 == 0:
                        self.inf1 = inf
                    elif self.inf1 == inf and \
                            self.inf2 == 0 and self.inf3 == 0:
                        self.inf2 = inf
                    elif self.inf1 == inf and \
                            self.inf2 == inf and self.inf3 == 0:
                        self.inf3 = inf
                else:
                    self.counter += attributes[i]

        return self

    def power(self):
        if self.inf1 == inf or self.inf2 == inf or self.inf3 == inf:
            return inf
        else:
            return self.counter


if __name__ == "__main__":
    f = Void()
    print(type(f), f.__dict__)
    f = f.add(R2Point(0.0, 0.0))
    print(type(f), f.__dict__)
    f = f.add(R2Point(1.0, 0.0))
    print(type(f), f.__dict__)
    f = f.add(R2Point(0.0, 1.0))
    print(type(f), f.__dict__)
