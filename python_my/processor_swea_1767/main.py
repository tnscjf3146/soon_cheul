import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def set_line(path, value):
    for i, j in path:
        board[i][j] = value

def dfs(idx, connected, length):
    global max_connected, min_length

    if idx == len(cores):
        if max_connected < connected:
            max_connected = connected
            min_length = length

        elif max_connected == connected and min_length > length:
            min_length = length

        return

    if max_connected > connected + (len(cores) - idx):
        return

    i, j = cores[idx]
    for dx in range(4):
        path = []
        ni = i + di[dx]
        nj = j + dj[dx]

        while 0 <= ni < N and 0 <= nj < N:
            if board[ni][nj] != 0:
                path = []
                break

            path.append((ni, nj))
            ni += di[dx]
            nj += dj[dx]

        if path:
            set_line(path, 2)
            dfs(idx + 1, connected + 1, length + len(path))
            set_line(path, 0)

    dfs(idx + 1, connected, length)

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    board = [list(map(int, input().split())) for _ in range(N)]

    cores = []

    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if board[i][j] == 1:
                cores.append((i, j))

    max_connected = 0

    min_length = float("inf")

    dfs(0, 0, 0)

    print(f"#{test_case} {min_length}")