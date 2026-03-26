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

from heapq import heappush, heappop

n, m = FastIO.getInts()

dist = [float("inf")] * n
bumps = [float("inf")] * n
dist[0] = 0
bumps[0] = 0

# Edge set up
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b, c, d = FastIO.getInts()
    edges[a].append((b, c, d))
    edges[b].append((a, c, d))


"""
Heap structure - 
(min_bumps, min_dist, vertex)

If you accidentally set vertex as first value in tuple,
you will get TLE!
"""

heap = [((0, 0, 0))]
while heap:
    best_bump, best_dist, v = heappop(heap)
    if bumps[v] != best_bump or dist[v] != best_dist:
        continue
    for conn, c, d in edges[v]:
        if c + best_bump < bumps[conn] or (c + best_bump == bumps[conn] and best_dist + d < dist[conn]):
            bumps[conn] = c + best_bump
            dist[conn] = best_dist + d
            heappush(heap, (bumps[conn], dist[conn], conn))
    
print(bumps[-1], dist[-1])

