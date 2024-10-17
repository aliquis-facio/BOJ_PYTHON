import sys
input = sys.stdin.readline

string: str = input().strip()
bomb: str = input().strip()

string_len: int = len(string)
bomb_len: int = len(bomb)

lst = []

for i in range(string_len):
    if string[i] in bomb:
        lst.append(string[i])
        if string[i] == bomb[-1]:
            for j in range(bomb_len):
                pass
