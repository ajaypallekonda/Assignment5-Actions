import math
from datetime import date


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


def function3(date1, date2):
    start = date(date1[0], date1[1], date1[2])
    finish = date(date2[0], date2[1], date2[2])
    time = finish - start

    return time.days
