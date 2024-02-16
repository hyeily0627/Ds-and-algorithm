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
    - 재귀호출
    - 정렬

## 7일차
- 파이썬 자료구조/ 알고리즘
    - 검색
- 코딩테스트 