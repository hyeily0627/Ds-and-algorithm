# 자료구조와 알고리즘 2024 (ds-and-algorithm)
부경대학교 2024 IoT 개발자 과정 - 파이썬 자료구조와 알고리즘 학습 리포지토리

## 1일차
- 자료구조, 알고리즘 개요
- 파이썬 기초 복습, 함수까지

## 2일차 
- 파이썬 기초 복습
- 파이썬 자료 구조
    - 선형 리스트 

## 3일차 
-  파이썬 자료 구조 
    - 단순 연결 리스트(선형리스트의 불편함을 개선하고자) 
    - 원형 연결 리스트 : 마지막 노드가 첫 노드와 연결 
    - 스택 : Last In First Out = LIPO 후입선출

        ![stack](https://bluegalaxy.info/codewalk/wp-content/uploads/2018/08/stack.jpg)

        - pop : list.pop()
        - push : list.append() 와 동일 
    - 큐 : First In First Out = FIFO 선입선출

        ![Queue](https://raw.githubusercontent.com/hyeily0627/ds-and-algorithm/main/images/queue.png)



## 4일차
- 큐 일반구현
    ```python
    def isQueueFull() :
    global SIZE, rear
    if rear == (SIZE - 1) : 
        return True
    else :
        return False 
    ```
    - ❗deQueue 사용시 큐의 앞쪽은 비워지지만 다시 사용하지 않는 문제 발생
        
    ![Queue](https://raw.githubusercontent.com/hyeily0627/ds-and-algorithm/main/images/queue2.png)

- 트리(이진)
- 그래프 

## 5일차

