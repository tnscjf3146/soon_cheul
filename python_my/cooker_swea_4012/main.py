import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

def calc(food):
    '''
    맛의 synergy 를 계산하는 함수
    :param food: 재료 리스트
    :return: synergy
    '''
    synergy = 0
    for i in range(N // 2):
        for j in range(i + 1, N // 2):

            idx = food[i]
            jdx = food[j]

            synergy += ingredient[idx][jdx] + ingredient[jdx][idx]

    return synergy

def dfs(idx, picked):
    '''
    재료를 N // 2 개 선택하고, A 요리를 만들고
    나머지 재료로 B 요리를 구성하는 함수
    :param idx: 인덱스로 재료 사용 고려
    :param picked: 사용하는 재료 리스트에 저장
    :return: result 값 직접 변환 min 함수를 사용해서 맛차이의 절댓값으로 재할당
    '''
    global result

    if len(picked) == N // 2:
        # 요리 A의 재료를 다 선택했다면,

        other = []
        # 요리 B의 재료를 선택

        for j in range(N):
            if j not in picked:
                other.append(j)

        a_dish = calc(picked)
        b_dish = calc(other)

        result = min(result, abs(a_dish - b_dish))
        return

    for i in range(idx, N):
        picked.append(i)
        dfs(i + 1, picked)
        picked.pop()
        # 백트래킹

# 인풋 받기
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    ingredient = [list(map(int, input().split())) for _ in range(N)]

    result = float("inf")

    dfs(0, [])

    print(f"#{test_case}", result)