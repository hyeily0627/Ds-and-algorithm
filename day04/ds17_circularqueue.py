# file : ds17_circularqueue.py
# desc : circular Queue 일반 구현 
## 원형 큐에서는 rear|front + 1 % 큐 크기

# QueueFull 함수 
def isQueueFull() :
    global SIZE, queue, front, rear
    if (rear + 1) % SIZE == front :
        return True
    else : 
        return False
 
# QueueEmpty 함수
def isQueueEmpty() : 
    global SIZE, queue, front, rear
    if front == rear :
        return True
    else :
        return False 

# Queue 데이터 삽입 함수
def enQueue(data) : 
    global SIZE, queue, front, rear
    if isQueueFull() == True : # 큐가 꽉차서 입력불가 
        print('Queue is Full')
        return # 함수 빠져나오기 
    else : 
        rear = (rear + 1) % SIZE # 원형 큐에서 데이터 입력 공간 확보 
        queue[rear] = data

# Queue 데이터 추출 함수 
def deQueue() :
    global SIZE, queue, front, rear
    if isQueueEmpty() : 
        print('Queue is Empty')
        return
    else : 
        front += (front + 1) % SIZE
        data = queue[front]
        queue[front] = None
        return data

# Queue 추출 데이터 확인 함수 
def peek() : 
    global SIZE, queue, front, rear
    if isQueueEmpty() == True : 
        print('큐가 비었습니다!')
        return
    else : 
        return queue[(front + 1) % SIZE ] 
    # 연산자 우선처리!! (front + 1) % SIZE != front + 1 % SIZE  

# 전역변수 
SIZE = int(input('큐 크기를 입력하세요(정수) > ')) # 대문자로 쓰는 건 상수(constant)로 사용하는 것 - 변수를 상수로 사용
queue = [None for _ in range(SIZE)] 
front = rear = 0 

if __name__ == '__main__': # 메인 시작
    # queue = [None, None, '마늘', '숙주', '고추']
    # front = 1 
    # rear = 4 

    # print(isQueueFull())
    # print(queue)

    while True :
        select = input('삽입(e), 추출(d), 확인(p), 종료(x) > ')
        
        if select.lower() == 'e' :
            data = input('입력 데이터 > ')
            enQueue(data)
            print(f'큐 상태 : {queue}')

        elif select.lower() == 'd' :
            data = deQueue()
            print(f'추출데이터 > {data}')
            print(f'큐 상태 : {queue}')

        elif select.lower() == 'p' :
            data = peek()
            print(f'확인데이터 > {data}')
            print(f'큐 상태 : {queue}')

        elif select.lower() == 'x' : 
            break
        
        else : 
            continue