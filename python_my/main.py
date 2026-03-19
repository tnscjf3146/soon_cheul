import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

def simulate(times, stair_val):
    if not times:
        return 0

    times.sort()
    finish = []

    for i in range(len(times)):
        if i < 3:
            start = times[i]
        else:
            start = max(times[i], finish[i - 3])

        finish.append(start + stair_val)

    return finish[-1]

def dfs(idx):
    global answer

    if idx == len(people):
        stair1 = []
        stair2 = []

        for i in range(len(people)):
            pr, pc = people[i]
            if selected[i] == 0:
                sr, sc, slen = stairs[0]
                stair1.append(abs(pr - sr) + abs(pc - sc) + 1)

            else:
                sr, sc, slen = stairs[1]
                stair2.append(abs(pr - sr) + abs(pc - sc) + 1)

        time1 = simulate(stair1, stairs[0][2])
        time2 = simulate(stair2, stairs[1][2])

        answer = min(answer, max(time1, time2))
        return

    selected[idx] = 1
    dfs(idx + 1)

    selected[idx] = 0
    dfs(idx + 1)

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]

    people = []
    stairs = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                if arr[i][j] == 1:
                    people.append((i, j))
                else:
                    stairs.append((i, j, arr[i][j]))

    selected = [0] * len(people)
    answer = float("inf")

    dfs(0)
