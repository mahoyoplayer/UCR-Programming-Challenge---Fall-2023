import sys

class FastIO:
    import os
    # Try to use local input file if exists
    if os.path.exists(input_file := os.path.splitext(__file__)[0] + ".txt"):
        sys.stdin = open(input_file, "r")
    input = sys.stdin.buffer.readline

    @staticmethod
    def getInt() -> int:
        return int(FastIO.input())

    @staticmethod
    def getInts():
        return list(map(int, FastIO.input().split()))

    @staticmethod
    def getFloat() -> float:
        return float(FastIO.input())

    @staticmethod
    def getFloats() -> list[float]:
        return list(map(float, FastIO.input().split()))

    @staticmethod
    def getStr() -> str:
        return FastIO.input().decode().strip()

    @staticmethod
    def getStrs() -> list[str]:
        return FastIO.input().decode().split()

import math
c_1, c_2, r_x, r_y = FastIO.getInts()
s, n = FastIO.getInts()
m = FastIO.getInt()

def radiator_test(p_x, p_y):
    dist = (r_x - p_x)**2 + (r_y-p_y)**2
    dist = math.sqrt(dist)
    return c_1 <= dist <= c_2

def tv_test(p_x, p_y):
    if 200 < p_y < 300: return False
    line_1 = lambda x: -x + 800#"y=-x+800"
    line_2 = lambda x: x - 300#"y=x-300"
    if p_y >= line_2(p_x) and p_y <= line_1(p_x):
        return True
    return False

def cross_test(p_x, p_y):
    if n == s:
        return n <= p_x <= n + 100
    m = 500 / (n-s) 
    line_1 = lambda x: m*(x - s)
    line_2 = lambda x: m*(x-(s+100))
    if n > s:
        return p_y <= line_1(p_x) and p_y >= line_2(p_x)
    else:
        return p_y >= line_1(p_x) and p_y <= line_2(p_x)

for _ in range(m):
    x, y = FastIO.getInts()
    r, t, c = radiator_test(x,y),  tv_test(x, y) ,  cross_test(x, y)
    if r and t and c:
        print("yes")
    else:
        print("no")