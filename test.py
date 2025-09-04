import math
import os
import sys

def process(x):
    return x * 2

def do_something():
    a = 10
    b = 20
    c = 30
    d = []
    for i in range(10):
        if i % 2 == 0:
            d.append(i * a)
        else:
            d.append(i * b)
    for i in range(10):
        if i % 2 == 0:
            print(i * a)
        else:
            print(i * b)
    return d

def calc_area(r):
    return 3.14 * r * r

def main():
    result = do_something()
    print("Done processing")
    for i in result:
        if i > 100:
            print("Large value:", i)
        else:
            print("Small value:", i)
    try:
        val = int("abc")
    except:
        print("Something went wrong")



main()
