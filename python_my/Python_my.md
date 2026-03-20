# Python!
``` python
T = int(input())
for test_case in range(1, T + 1):
    # 황순철의 파이썬
    # 내가 파이썬을 배우는 방법
    break
```
- - -
## 기본 개념

&nbsp; 파이썬(python)은 1991년 귀도 반 로섬이 개발한 **오픈 소스, 고수준, 객체지향형, 인터프리터 방식의 다목적 프로그래밍 언어**이다.
**AI(머신러닝/딥러닝)**, 웹 개발, 데이터 분석 등 다양한 분야엣 활용된다.

## 학습개요

### 1. 학습 주제
  - Python 기본 문법
  - 객체 지향 프로그래밍 기초
  - 데이터 분석 라이브러리(NumPy, Pandas)

### 2. 학습 목표
  - Python의 다양한 자료형
  - 조건문과 반복문

### 3. 핵심 개념
  - 기본 자료형
  - 컬렉션 자료형
  - 제어문
  - **함수(function)**: 코드를 재사용 가능한 블럭으로 만들어 가독성과 유지 보수성을 높임
  - **클래스(class)**: 데이터와 기능을 하나의 구조로 묶어 재사용성과 구조화를 제공, 객체/인스턴스/메서드 개념을 포함

- - -
- - -
## PEP 8 – Style Guide for Python Code
&nbsp; 파이썬의 기본 스타일 가이드  
[pep 8](https://peps.python.org/pep-0008/) &nbsp;<공문> / &nbsp;[누군가의 위키독스](https://wikidocs.net/8926) &nbsp;
1. 가독성과 명시성이 중요
2. indentation - 들여쓰기  
   코드는 들여쓰기로 속해있는 관계를 표현한다.  
   수준당 4개의 공백 혹은 Tab으로 나눈다.  
3. 문자열의 인용문  
   파이썬에서 "" 혹은 ''으로 표현한다.
   둘중 하나가 필요할 경우  
    " ' ' " 으로 작은따옴표  
    ' " " ' 으로 큰 따옴표를 표현한다.
    ```python
    print("'Hello!'")   # -> 'Hello!'
    print('"Python!"')  # -> "Python!" 

    ```
4. 표현식과 명령문에서의 공백
5. 후행 쉼표를 사용하는 경우
6. 짧은 설명문(주석)  
   '''  
   '''  
   혹은,  
   \#  
   으로 표기한다.
   ```python
   '''
   This is comments
   under of function!
       함수의 밑에서는 해당 함수가 어떤 것 인지, 
       파라미터로는 어떠한 것을 받는지
       등등을 설명 할 수 있다.
   '''

   # This is comments
   # 해당 구문이 어떤 구문인지를 설명할때 자주 쓰인다.

   ```
7. 이름설정 협약  -> 해당 카테고리 공부가 더 필요할 것으로 보임
   - 재정의 원칙
   - 이름 설정 스타일
8. 프로그래밍 권장사항


## 기본 자료형

1. ### int/float
   숫자형!
   ```python
   a = -3.14159

   # 절대값 만들기
   a_abs = abs(a)
   print(a_abs)

   # 반올림
   a_rounded = round(a)
   print(a_rounded)

   # 제곱
   a_squared = a ** 2
   print(a_squared)

   ```
2. ### str
   문자열!
   ```python
   s = "Hello World!"

   s1 = "Python"
   
   # 소문자로 변환
   s_lower = s.lower()
   print(s_lower)

   # 대문자로 변환
   s_upper = s.upper()
   print(s_upper)

   # 문자열 결합
   s_str = s + s1
   print(s_str)

   # 끝나는 글자 확인
   ends_with_s = s.endswith("!")
   print(ends_with_s)  # True, False

   # int/float 로 변환 가능한지 확인
   is_isdigit_s = s.isdigit()
   print(is_isdigit_s)  # True, False

   ```

## 컬렉션 자료형

1. ### List
   ```python
   # 순서가 있는 가변의 컬렉션 자료형
   # 다양한 타입의 데이터를 저장 가능

   lst = list(1, 2, 3, 4)

   lst_1 = [5, 6, 7]

   lst_len = len(lst) # -> 길이를 int값으로 줌

   new_lst = lst + lst_1  # [1, 2, 3, 4, 5, 6, 7]

   slicing = lst[0:4:1]  # start 0, stop 3, step 1 -> -1 이면 역순

   slicing_lst_plus = lst[:2] + lst_1[1:]  # [1, 2] + [6, 7]

   has_4 = 4 in lst  # True

   max_val = max(lst)

   min_val = min(lst)

   # 원소 지우기
   lst.remove(3)

   # 원소 넣기
   lst.insurt(2, 3)  # 인덱스, 값

   # 원소 넣기
   lst.append(5)

   # 원소 빼기
   lst.pop()

   # l 뒤집기
   lst.reverse()

   # 정렬
   lst.sort()
   
   # 원소 모두 삭제
   lst.clear()

   ```
2. ### Tuple
   ```python
   # 순서가 있는 불변의 컬렉션 자료형
   # 리스트보다 메모리 효율이 좋음 안전한 데이터 저장 <변경 불가>

   t = tuple(1, 2, 3, 4)
   t = (1, 2, 3, 4)

   length = len(t)

   has_1 = 1 in t

   double_t = t + t

   slicing_t = t[1 : 3]

   max_val = max(t)

   min_val = min(t)

   ```
3. ### Set
   ```python
   # **순서가 없는** 불변의 컬렉션 자료형
   # 중복이 허용이 되지 않음
   # 인덱싱 불가, + 연산 불가

   s = {1, 2, 3, 4}

   length = len(s)

   has_1 = 1 in s

   max_val = max(s)

   min_val = min(s)

   # 원소 없애기
   s.remove(3)

   # 원소 추가
   s.add(3)

   s2 = {3, 4, 5, 6}
   
   # 합집합
   union = s.union(s2)
   union = s | s2

   # 차집합
   difference = s.difference(s2)
   difference = s - s2

   # 대칭차집합(교집합을 제외한 합집합)
   symmetric_diff = s.symmetric_difference(s2)
   symmetric_diff = s ^ s2
   
   ```
4. ### Dict
   ```python
   # 순서가 없는 불변의 키와 값이 있는 자료형
   # 키 중복 불가! 키로 벨류를 불러 올 수 있음

   d = {
      1: "apple",
      2: "banana",
      3: "cheese",
   }

   length = len(d)

   keys = list(d.keys())

   has_key_4 = 4 in d

   # key가 존재하면 value반환, 없으면 None
   val_4 = d.get(4)

   d2 = {
       4: "dragonfruit"
   }

   # d 랑 d2 랑 합치기
   marged = { **d, **d2 }

   ```

## 제어문과 반복문
1. ### 제어문
   ```python
   score = 85

   if score >= 90:
       print("학점: A")
      # 조건

   elif score >= 80:
       print("학점: B")
      # 2번째 조건

   if score >= 70:
       print("학점: C")
      # 새로운 고려 조건
   
   else:
       print("학점: D")
      # 이외의 모딘 조건

   # in라인 조건문
   result = a if a > score else b
      # a 가 score 보다 크면 a 를 result로 할당, 혹은 b를 할당

   ```
2. ### 반복문
   ```python
   for i in range(N):
      # 범위를 만들고 그동안 반복하는 반복문
      break

   while True:
      # 조건이 참일 동안 계속해서 반복
      break
   
   # list comprehension
   lst = [list(map(int, input().split())) for _ in range(N)]

   ```
## 함수 (function)
   ```python
   def function(parameterA, parameterB):  # P
      # 함수정의 후 연산
      # calculation
      # Application parameter

      global result
      # global을 해야 전역변수(global parameter)인 result를 함수 내에서 변경 가능

         # 재귀 호출 시 전위순회 구역 -> P, A, B
      function(parameterA + 1, parameterB + 1) # A
      # 재귀호출처럼 다시 호출도 가능
         # 재귀 호출 시 중위순회 구역 -> A, P, B
      function(parameterA + 1, parameterB) # B
         # 재귀 호출 시 후위 순회 구역 -> A, B, p

      return # function() end
      # return에 값을 넣어두면 변수에 할당할 수 있음

   
   # 함수 호출
   function(A, B)

   ```


## 클래스
따로정리 -> 응용해야 할 사항이 많음