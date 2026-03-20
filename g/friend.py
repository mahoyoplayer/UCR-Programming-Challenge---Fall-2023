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

n = FastIO.getInt()
sheldon, raj = FastIO.getStr(), FastIO.getStr()

# O(n^2) space solution
def bad_sol():
    dp = [[0] * (n+1) for _ in range(n+1)]

    # Base Case
    for i in range(1, n+1):
        dp[0][i] = i
        dp[i][0] = i

    for i in range(1, n+1):
        for j in range(1, n+1):
            if sheldon[i-1] == raj[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                ins = dp[i][j-1] + 1
                remv = dp[i-1][j] + 1
                sub = dp[i-1][j-1] + 1
                dp[i][j] = min(ins, remv, sub)

    print(dp[n][n])

def good_sol():
    pass
good_sol()