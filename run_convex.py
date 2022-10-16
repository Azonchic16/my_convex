#!/usr/bin/env -S python3 -B
from r2point import R2Point
from convex import Void, Figure

f = Void()
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
        print(f"S = {f.area()}, P = {f.perimeter()}, Po = {f.power()}")
        print()
except(EOFError, KeyboardInterrupt):
    print("\nStop")
