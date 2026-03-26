import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def copy_board(board):
    # 보드를 복사하는 함수
    new_board = []
    for i in range(H):
        new_board.append(board[i][:])
        # 그냥 복사하면 얕은복사가 되므로,
        # 깊은 복사를 위해 원소 하나하나 복사

    return new_board

def cnt_bricks(board):
    cnt = 0
    for i in range(H):
        for j in range(W):
            if board[i][j] != 0:
                cnt += 1

    return cnt

def boom(i, j, board):
    value = board[i][j]
    board[i][j] = 0
    for dx in range(4):
        for m in range(1, value):
            ni = i + di[dx] * m
            nj = j + dj[dx] * m
            if 0 <= ni < H and 0 <= nj < W:
                if board[ni][nj] > 1:
                    boom(ni, nj, board)
                    # 재귀해서 연쇄폭발

                board[ni][nj] = 0

def gravity(board):
    for j in range(W):
        path = []
        for i in range(H):
            if board[i][j] > 0:
                path.append(board[i][j])
                board[i][j] = 0

        for i in range(H - 1, -1, -1):
            if not path:
                break
            board[i][j] = path.pop()

def drop(idx, board):
    global min_bricks

    if idx == N:
        cnt = cnt_bricks(board)
        min_bricks = min(min_bricks, cnt)
        return

    for j in range(W):
        copy = copy_board(board)
        for i in range(H):
            if copy[i][j] != 0:
                boom(i, j, copy)
                gravity(copy)
                drop(idx + 1, copy)
                break

            elif copy[i][j] == 0 and i == H - 1:
                drop(idx + 1, copy)

T = int(input())
for test_case in range(1, T + 1):
    N, W, H = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(H)]

    min_bricks = float("inf")

    drop(0, matrix)

    print(f"#{test_case}", min_bricks)