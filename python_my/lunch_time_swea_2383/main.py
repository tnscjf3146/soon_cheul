import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

def calc(arr, slen):
    if not arr:
        return 0

    finish = []
    arr.sort()

    for i in range(len(arr)):
        if i < 3:
            start = arr[i]

        else:
            start = max(arr[i], finish[i - 3])

        finish.append(start + slen)

    return finish[-1]

def dfs(idx):
    global result

    if idx == len(people):
        stair_1 = []
        stair_2 = []
        for i in range(len(people)):
            px, py = people[i]

            if selected[i] == 0:
                sx, sy, slen = stairs[0]
                stair_1.append(abs(px - sx) + abs(py - sy) + 1)

            else:
                sx, sy, slen = stairs[1]
                stair_2.append(abs(px - sx) + abs(py - sy) + 1)

        time_1 = calc(stair_1, stairs[0][2])
        time_2 = calc(stair_2, stairs[1][2])

        result = min(result, max(time_1, time_2))
        return

    selected[idx] = 1
    dfs(idx + 1)

    selected[idx] = 0
    dfs(idx + 1)

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    people = []
    stairs = []

    for i in range(N):
        for j in range(N):
            if matrix[i][j] != 0:
                if matrix[i][j] == 1:
                    people.append((i, j))

                else:
                    stairs.append((i, j, matrix[i][j]))

    result = float("inf")
    selected = [0] * len(people)

    dfs(0)

    print(f"#{test_case}", result)