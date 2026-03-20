import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

def dfs(idx):
    global result

    number = "".join(arr)
    if number in cnt_lst[idx]:
        return

    if idx == K:
        result = max(result, int(number))
        return

    cnt_lst[idx].append(number)

    for i in range(N):
        for j in range(i + 1, N):
            arr[i], arr[j] = arr[j], arr[i]
            dfs(idx + 1)
            arr[i], arr[j] = arr[j], arr[i]

T = int(input())
for test_case in range(1, T + 1):
    arr, K = input().split()

    K = int(K)
    arr = list(arr)

    N = len(arr)
    cnt_lst = [[] for _ in range(K + 1)]

    result = 0

    dfs(0)

    print(f"#{test_case}", result)
