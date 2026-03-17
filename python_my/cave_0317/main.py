import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


# 과목평가 4회차 2번 이진트리 문제

def dfs(idx, weight, value):
    global max_value
    if weight > K:
        return

    if not tree[idx]:
        if max_value < value:
            max_value = value
        return

    for r, w, v in tree[idx]:
        dfs(r, weight + w, value + v)
        dfs(r, weight, value)


T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    tree = [[] for _ in range(N + 1)]

    for _ in range(N):
        r, w, v, p = map(int, input().split())
        tree[p].append((r, w, v))

    max_value = 0

    dfs(0, 0, 0)

    print(f"#{test_case} {max_value}")