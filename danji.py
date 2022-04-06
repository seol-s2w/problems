from collections import deque


def main():
    n = int(input())
    map_ = [list(map(int, list(input()))) for _ in range(n)]
    visited = [list(False for _ in range(n)) for _ in range(n)]

    def __is_new_home(row, col):
        return not visited[row][col] and map_[row][col]

    # left, top, right, bottom
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    results = []
    for idx in range(n * n):
        i, j = idx // n, idx % n
        if not __is_new_home(i, j):
            continue

        visited[i][j] = True

        q = deque()
        q.append((i, j))
        results.append(list())
        while q:
            ci, cj = q.popleft()
            results[-1].append((ci, cj))
            for di, dj in directions:
                ni, nj = ci + di, cj + dj
                if ni < 0 or nj < 0 or ni >= n or nj >= n:
                    continue

                if not __is_new_home(ni, nj):
                    continue

                visited[ni][nj] = True
                q.append((ni, nj))

    results.sort(key=lambda x: len(x))
    print(len(results))
    for result in results:
        print(len(result), result)


if __name__ == "__main__":
    main()
