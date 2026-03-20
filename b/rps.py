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

s, l = FastIO.getStr(), FastIO.getStr()

if s == l:
    print("Tie!")
    sys.exit()

win_map = {
    ("Scissors", "Paper"),
    ("Paper", "Rock"),
    ("Rock", "Lizard"),
    ("Lizard", "Spock"),
    ("Spock", "Scissors"),
    ("Scissors", "Lizard"),
    ("Lizard", "Paper"),
    ("Paper", "Spock"),
    ("Spock", "Rock"),
    ("Rock", "Scissors")

}

winner = "Sheldon" if (s, l) in win_map else "Leonard"
print(winner, "wins the game!")
