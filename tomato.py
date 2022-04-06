from collections import deque
from sys import stdin


def solve():
    col, row = map(int, stdin.readline().split())
    box = [list(map(int, stdin.readline().split())) for _ in range(row)]
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    unriped_tomato_cnt = 0
    riped_tomatoes = deque()
    for i in range(row):
        for j in range(col):
            if box[i][j] == 0:
                unriped_tomato_cnt += 1
            elif box[i][j] == 1:
                riped_tomatoes.append((i, j))

    day = 0
    while riped_tomatoes and unriped_tomato_cnt > 0:
        for _ in range(len(riped_tomatoes)):
            i, j = riped_tomatoes.popleft()

            for di, dj in directions:
                ni, nj = i + di, j + dj
                if ni < 0 or nj < 0 or ni >= row or nj >= col:
                    continue

                if box[ni][nj] == 0:
                    box[ni][nj] = 1
                    unriped_tomato_cnt -= 1
                    riped_tomatoes.append((ni, nj))
        day += 1

    if unriped_tomato_cnt == 0:
        print(day)
    else:
        print(-1)


if __name__ == "__main__":
    solve()
