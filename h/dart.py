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


"""
Want to minimize score as much as possible
m is the starting amount of points
output should be 1-indexed

Idea:
Find highest sum <= m of a two_throw
Sum of 2 two_throws = 1 four-throw
Track indices that make up a two_throw
using a map.

Use binary search to find best 
complement of a two_throw. 
"""

n, m = FastIO.getInts()
points = [FastIO.getInt() for _ in range(n)]

two_throws = set([0] + points)
throw_map = {}
throw_map[0] = [0, 0]
for i, p in enumerate(points):
    throw_map[p] = [0, i + 1]

for i, p in enumerate(points):
    for j, p_2 in enumerate(points):
        two_throws.add(p + p_2)
        throw_map[p + p_2] = [i + 1, j + 1]

highest = 0
high_list = [0, 0, 0, 0]
two_throws = sorted(list(two_throws))
from bisect import bisect_right
for i, throw in enumerate(two_throws):
    complement = m - throw
    # Want greatest throw <= complement
    # Find greatest throw > complement, then -1
    idx = bisect_right(two_throws, complement) - 1
    if  idx < 0: continue

    ans = throw + two_throws[idx]
    if ans > highest:
        highest = ans
        high_list = throw_map[throw] + throw_map[two_throws[idx]]

#print(two_throws)
#print(highest)
print(*high_list)