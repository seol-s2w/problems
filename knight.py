from collections import deque


def solve():
    n = int(input())
    cases = []
    for _ in range(n):
        l = int(input())
        start_idx = tuple(map(int, input().split()))
        end_idx = tuple(map(int, input().split()))
        cases.append((l, start_idx, end_idx))

    for l, si, ei in cases:
        print(get_shortest_path_count(l, si, ei))


def get_shortest_path_count(length, start_idx, end_idx):
    directions = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
    visited = {start_idx}
    cnt = 0
    q = deque()
    q.append(start_idx)
    while True:
        for _ in range(len(q)):
            idx = q.popleft()
            if idx == end_idx:
                return cnt

            for di, dj in directions:
                ni, nj = idx[0] + di, idx[1] + dj
                if ni < 0 or nj < 0 or ni >= length or nj >= length:
                    continue

                next_idx = (ni, nj)
                if next_idx in visited:
                    continue

                q.append(next_idx)
                visited.add(next_idx)
        cnt += 1


if __name__ == "__main__":
    solve()
