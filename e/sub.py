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

base = ord("A")
inp, tl, s = FastIO.getStr(), FastIO.getStr(), FastIO.getStr()
used_encode = {}
used_decode = {}

fail = False
for i in range(len(inp)):
    a, b = inp[i], tl[i]
    idx = ord(a) - base
    if used_encode.get(a, b) != b or used_decode.get(b, a) != a:
        fail = True
        break
    used_encode[a] = b
    used_decode[b] = a


fail = fail or len(used_encode) != 26

if fail:
    print("Failed")
else:
    print("".join([used_encode[c] for c in s]))

