# 자료구조와 알고리즘 2024 (ds-and-algorithm)
부경대학교 2024 IoT 개발자 과정 - 파이썬 자료구조와 알고리즘 학습 리포지토리

## 1일차
- 자료구조, 알고리즘 개요
- 파이썬 기초 복습, 함수까지

## 2일차 
- 파이썬 기초 복습

![자료구조](https://t1.daumcdn.net/cfile/tistory/23202B4C53FDC5600C)

- 파이썬 자료 구조
    - 선형 리스트 
    - 단순 연결 리스트 = 파이썬의 list와 동일
        ![연결리스트](https://upload.wikimedia.org/wikipedia/commons/9/9c/Single_linked_list.png)

## 3일차 
-  파이썬 자료 구조 
    - 단순 연결 리스트(선형리스트의 불편함을 개선하고자) 
    - 원형 연결 리스트 : 마지막 노드가 첫 노드와 연결 
    - 스택 : Last In First Out = LIPO 후입선출 - 교재 203p

        ![stack](https://bluegalaxy.info/codewalk/wp-content/uploads/2018/08/stack.jpg)

        - pop : list.pop()
        - push : list.append() 와 동일 
    - 큐 : First In First Out = FIFO 선입선출 - 교재 235p 

        ![Queue](https://raw.githubusercontent.com/hyeily0627/ds-and-algorithm/main/images/queue.png)


## 4일차
- 파이썬 자료구조
    - 큐(Sequential Queue_순차큐) 일반구현 - 교재 243p
        ```python
        def isQueueFull() :
        global SIZE, rear
        if rear == (SIZE - 1) : 
            return True
        else :
            return False 
        ```
        - ❗deQueue 사용시 큐의 앞쪽은 비워지지만 다시 사용하지 않는 문제 발생
            
        ![Queue2](https://raw.githubusercontent.com/hyeily0627/ds-and-algorithm/main/images/queue2.png)

        ```python
        def isQueueFull() :
        global SIZE, queue, front, rear
        if rear == (SIZE - 1) : # 큐가 아직 빈 상태 
            return False
        elif rear == (SIZE - 1) and front == -1 : # 큐가 꽉찬 상태 
            return True
        else : # 큐 앞쪽이 비어있는 상태, rear가 끝까지 간 상태
            while front != -1 : # 완전히 앞으로 당기기 -> front가 -1이 될 때까지
                for i in range(front + 1, SIZE) :
                    queue[i - 1] = queue[i] # front에다가 front + 1의 값 할당
                    queue[i] = None
                front -= 1 
                rear -= 1 
            return False
        ```
        ![Queue3](https://raw.githubusercontent.com/hyeily0627/ds-and-algorithm/main/images/queue3.png)

    - 원형 큐(circular Queue) - 교재 258p~
        - 원형 큐에서는 'rear|front + 1 % 큐 크기' 가 핵심
    - 트리(이진) - 교재 276p

        ![이진트리](https://kahee.github.io//assets/post_img/tree3.png)
        
        - 전위 순회(preorder traversal) : 루트 -> 왼쪽 -> 오른쪽 
        - 중위 순회(inorder traversal) :  왼쪽 -> 루트 -> 오른쪽 
        - 후위 순회(postorder traversal) :  왼쪽 -> 오른쪽 -> 루트 

## 5일차
- 파이썬 자료구조/알고리즘
    - 그래프
    
    ![graph](https://raw.githubusercontent.com/hyeily0627/ds-and-algorithm/main/images/graph2.png)

## 6일차(24.02.19)
- 파이썬 자료구조/ 알고리즘
    - 재귀호출 : 자신을 다시 호출 하는 것 

    ![Recursion기본예제](https://raw.githubusercontent.com/hyeily0627/ds-and-algorithm/main/images/recursion.gif)

    - 정렬
        1. 선택 정렬(Selection Sort) : 주어진 자료들 중에 현재 위치에 맞는 자료를 찾아 선택하여 위치를 교환하는 정렬 알고리즘
            - 첫 번째는 주어진 배열에서 최소값을 찾는다. 두 번째는 최소값을 맨 앞의 값과 바꾼다. 세 번째는 바꿔준 맨 앞 값을 제외한 나머지 원소를 동일한 방법으로 바꿔준다.
            - O(n²)의 시간복잡도를 가지고 있다.(성능이 좋지 않다.)

        ![선택정렬](https://raw.githubusercontent.com/hyeily0627/ds-and-algorithm/main/images/sort3.gif)  

        2. 삽입 정렬(Insertion Sort) : 주어진 자료의 모든 요소를 앞에서부터 차례대로 정렬된 자료 부분과 비교하여 자신의 위치를 찾아 삽입하는 정렬
            - O(n)의 시간복잡도를 가지지만, 최악의 경우 O(n²)시간복잡도를 가진다.

        ![삽입정렬](https://raw.githubusercontent.com/hyeily0627/ds-and-algorithm/main/images/sort2.gif)  

        3. 버블 정렬(Bubble Sort)
            - 0번째 원소와 1번째 원소를 비교 후 정렬
            - 1번째 원소와 2번째 원소를 비교 후 정렬 …
            - n-1번째 원소와 n번째 원소를 비교 후 정렬
            - 시간복잡도 : O(n²) 
            - 단, 정렬이 어느정도 되어 있는 데이터라면 연산수가 급격하게 줄어듦

        ![버블정렬](https://raw.githubusercontent.com/hyeily0627/ds-and-algorithm/main/images/sort1.gif)

        4. 퀵 정렬(Quick Sort)
            - 입력된 자료 리스트에서 하나의 원소를 고른다. 이 원소를 피벗이라고 부른다.
            - 피벗을 기준으로 리스트를 둘로 분할한다.
            - 피벗을 기준으로 피벗보다 작은 원소들은 모두 피벗의 왼쪽으로 옮긴다
            - 피벗을 기준으로 피벗보다 큰 원소들은 모두 피벗의 오른쪽으로 옮긴다
            - 시간복잡도 O(n×log n), 최악의 경우 O(n²)

        ![퀵정렬](https://raw.githubusercontent.com/hyeily0627/ds-and-algorithm/main/images/sort4.gif) 

        - 시간복잡도 정리 

        ![시간복잡도](https://raw.githubusercontent.com/hyeily0627/ds-and-algorithm/main/images/sort10.png)   

## 7일차
- 파이썬 자료구조/ 알고리즘
    - 검색
- 코딩테스트 