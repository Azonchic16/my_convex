#!/usr/bin/env -S python3 -B
from tk_drawer import TkDrawer
from r2point import R2Point
from convex import Void, Point, Segment, Polygon, Figure


def void_draw(self, tk):
    pass


def point_draw(self, tk):
    tk.draw_line(Figure.point_a, Figure.point_b)
    tk.draw_line(Figure.point_a, Figure.point_c)
    tk.draw_line(Figure.point_b, Figure.point_c)
    tk.draw_point(self.p)


def segment_draw(self, tk):
    tk.draw_line(Figure.point_a, Figure.point_b)
    tk.draw_line(Figure.point_a, Figure.point_c)
    tk.draw_line(Figure.point_b, Figure.point_c)
    tk.draw_line(self.p, self.q)


def polygon_draw(self, tk):
    tk.draw_line(Figure.point_a, Figure.point_b)
    tk.draw_line(Figure.point_a, Figure.point_c)
    tk.draw_line(Figure.point_b, Figure.point_c)
    for n in range(self.points.size()):
        tk.draw_line(self.points.last(), self.points.first())
        self.points.push_last(self.points.pop_first())


setattr(Void, 'draw', void_draw)
setattr(Point, 'draw', point_draw)
setattr(Segment, 'draw', segment_draw)
setattr(Polygon, 'draw', polygon_draw)


tk = TkDrawer()
f = Void()
tk.clean()

try:
    x_1 = float(input('x_1 -> '))
    y_1 = float(input('y_1 -> '))
    x_2 = float(input('x_2 -> '))
    y_2 = float(input('y_2 -> '))
    x_3 = float(input('x_3 -> '))
    y_3 = float(input('y_3 -> '))
    Figure.point_a = R2Point(x_1, y_1)
    Figure.point_b = R2Point(x_2, y_2)
    Figure.point_c = R2Point(x_3, y_3)
    while True:
        f = f.add(R2Point())
        tk.clean()
        f.draw(tk)
        print(f"S = {f.area()}, P = {f.perimeter()}, Po = {f.power()}\n")
except(EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
