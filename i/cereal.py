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
A cereal box is useless if I can make its value using smaller cereal boxes
15 is useless if there are bags of 7 and 8 b.c. 7 + 8 = 15.

Can use dp b.c. highest cereal box value is 20,000
"""

n = FastIO.getInt()
boxes = FastIO.getInts()
big_box = max(boxes)

# dp[i] = Can we make value of i using previous boxes?
dp = [False] * (big_box+1)
dp[0] = True

useless = 0

for j, val in enumerate(boxes):
    # If already true, this box is useless, we can already make it
    if dp[val]: 
        useless += 1
        continue
    for i in range(val, big_box +1):
        # If it is already true, ignore.
        if dp[i]: continue
        dp[i] = dp[i-val]


print(useless)