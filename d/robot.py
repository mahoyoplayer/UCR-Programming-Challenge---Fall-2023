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
robots = FastIO.getInts()

rank = n
monte = robots[0]

"""
There are faster ways to do this problem.
But, this simulates the entire competition.
The idea is that Monte should always fight most powerful robot that 
is still weaker than him. The rest of the robots should also
fight the weakest robot they can beat.
"""
def simulation_sol():
    from bisect import bisect_left, insort
    robots.sort()

    while len(robots) > 1:
        new = []
        if monte == robots[0]:
            print(rank)
            sys.exit()
        else:
            # bisect_left actually returns Monte's index, so subtract 1
            best_loser = robots[bisect_left(robots, monte)-1]
            robots.remove(monte)
            robots.remove(best_loser)


        for i in range(1, len(robots), 2):
            loser, winner = robots[i-1], robots[i]
            new.append(winner)

        insort(new, monte)
        rank //= 2
        robots = new[:]
    
    # We reached the end. Monte was the best
    print(1)


"""
The fastest way is to find number of weaker
robots than Monte. Find the best round he can make
and best rank based off of that.
"""
def best_sol():
    weak_count = sum([1 if x < monte else 0 for x in robots])
    import math
    #print(weak_count)
    best_round = int(math.log(weak_count+1, 2))
    best_rank = n // (2 ** best_round)
    print(best_rank)

best_sol()