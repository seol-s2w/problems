from collections import deque


def get_shortest_path(maze: list):
    row = len(maze)
    col = len(maze[0])

    visited = [list(False for _ in range(col)) for _ in range(row)]
    visited[0][0] = True

    # left, top, right, bottom
    di_dj_lst = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    q = deque()
    q.append((0, 0))

    path_map = {}
    exit = (row - 1, col - 1)
    found_exit = False
    while not found_exit:
        i, j = q.popleft()
        for di, dj in di_dj_lst:
            ni, nj = i + di, j + dj
            if ni < 0 or nj < 0 or ni >= n or nj >= m:
                continue

            if visited[ni][nj]:
                continue
            visited[ni][nj] = True

            if not maze[ni][nj]:
                continue

            next = (ni, nj)
            q.append(next)
            path_map[next] = (i, j)

            if next == exit:
                found_exit = True
                break

    shortest_path = [exit]
    next = path_map[exit]
    while next:
        shortest_path.append(next)
        next = path_map.get(next, None)

    return list(reversed(shortest_path))


n, m = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(n)]

shortest_path = get_shortest_path(maze)

print(len(shortest_path))
print(" -> ".join(map(str, shortest_path)))
