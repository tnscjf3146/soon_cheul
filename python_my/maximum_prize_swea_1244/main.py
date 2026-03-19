import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
# 아직까지 백트래킹이 약하다.
# + 가지치기도
# 인풋을 다양하게 받고 dfs를 어떻게 탐색해야하는지
# 익숙하지 않은 것 같다.
# 지피티 피셜 -> 일단 완전 탐색, 시간 초과, 가지치기, 백트래킹
def dfs(cnt):
    global max_price

    number = "".join(arr)

    if number in visited[cnt]:
        # 카운트 마다의 값이 중복이 되면 안된다.. 외않되....?
        return

    visited[cnt].append(number)
    # 이거를 어떻게 생각해서 쓰누...
    # O(n)을 생각해야 한다는 것인데.....

    if cnt == K:
        max_price = max(max_price, int(number))
        return

    for i in range(N):
        for j in range(i + 1, N):
            # 이것 까지는 알겠다 이거야... 백트래킹도 힘들누...
            arr[i], arr[j] = arr[j], arr[i]
            dfs(cnt + 1)
            arr[i], arr[j] = arr[j], arr[i]

T = int(input())
for test_case in range(1, T + 1):
    arr, K = input().split()

    arr = list(arr)
    K = int(K)

    visited = [[] for _ in range(K + 1)]
    N = len(arr)

    max_price = 0

    dfs(0)

    print(f"#{test_case}", max_price)
