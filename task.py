import math


def firstrun():
    return "success"


def function1(radius):
    pi = math.pi
    area = (radius * radius) * pi

    return area


def function2(list):
    a = list[0]
    b = list[len(list) - 1]

    return a, b
