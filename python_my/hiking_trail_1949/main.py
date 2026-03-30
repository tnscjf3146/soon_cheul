import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def dfs(i, j, length, skill_used):
    global max_length

    # 매번 가장 긴 등산로 길이를 갱신해 줘
    if length > max_length:
        max_length = length

    for dx in range(4):
        ni = i + di[dx]
        nj = j + dj[dx]

        # 맵의 범위 안에 있고, 아직 방문하지 않은 곳이라면
        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:

            # 케이스 1: 다음 칸이 현재 칸보다 낮아서 그냥 갈 수 있는 경우
            if matrix[ni][nj] < matrix[i][j]:
                visited[ni][nj] = 1
                dfs(ni, nj, length + 1, skill_used)
                visited[ni][nj] = 0  # 백트래킹 (원상복구)

            # 케이스 2: 다음 칸이 높거나 같지만, 아직 공사(skill)를 안 했고 깎아서 갈 수 있는 경우
            elif not skill_used and matrix[ni][nj] - K < matrix[i][j]:
                # 💡 핵심 포인트: 깎을 때는 무조건 내 현재 높이보다 '딱 1'만 낮게 깎는 게 가장 유리해!
                # (너무 많이 깎아버리면 그 다음 칸으로 이동할 때 불리해지니까)
                original_height = matrix[ni][nj]
                matrix[ni][nj] = matrix[i][j] - 1
                visited[ni][nj] = 1

                # 공사를 했다는 표시(True)를 달고 다음 탐색 진행
                dfs(ni, nj, length + 1, True)

                # 백트래킹 (원상복구)
                visited[ni][nj] = 0
                matrix[ni][nj] = original_height


T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 1. 맵에서 가장 높은 봉우리의 높이 찾기
    max_h = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] > max_h:
                max_h = matrix[i][j]

    # 2. 가장 높은 봉우리의 좌표들을 리스트에 모으기 (시작점들)
    peaks = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == max_h:
                peaks.append((i, j))

    max_length = 0
    visited = [[0] * N for _ in range(N)]

    # 3. 모든 봉우리에서 각각 DFS 탐색 시작
    for r, c in peaks:
        visited[r][c] = 1
        dfs(r, c, 1, False)  # 시작 길이는 1, 공사 찬스는 아직 안 썼으므로 False
        visited[r][c] = 0  # 다른 봉우리 탐색을 위해 시작점 방문 기록도 초기화

    print(f"#{test_case} {max_length}")