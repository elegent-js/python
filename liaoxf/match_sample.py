#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 演示match
score = 'B'
match score:
    case 'A':
        print('优秀')
    case 'B':
        print('良好')
    case 'C':
        print('及格')
    case _:
        print('不及格')


age = 2
match age:
    case x if x < 3:
        print('婴儿, year:', x)
    case 3 | 4 | 5:
        print('幼儿')
    case 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15:
        print('青少年')
    case _:
        print('成年人')


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    
    if x > 0:
        return x
    else:
        return -x
    
print(my_abs(-1))
print(my_abs(1))
print(my_abs(0))
print(my_abs(-1.1))
print(my_abs(1.1))
print(my_abs(0.1))
print(my_abs(-0.1))


import math

# 返回的多个值实际上是一个tuple
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

(x, y) = move(100, 100, 60, math.pi / 6)
print(x, y)


