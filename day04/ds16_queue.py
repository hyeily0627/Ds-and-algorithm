# file : ds16_queue.py
# desc : Queue 일반 구현 

# QueueFull 함수 
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

# QueueEmpty 함수
def isQueueEmpty() : 
    global front, rear
    if front == rear :
        return True
    else :
        return False 

# Queue 데이터 삽입 함수
def enQueue(data) : 
    global queue, rear
    if isQueueFull() == True : # 큐가 꽉차서 입력불가 
        print('Queue is Full')
        return # 함수 빠져나오기 
    else : 
        rear += 1 
        queue[rear] = data

# Queue 데이터 추출 함수 
def deQueue() :
    global queue, front
    if isQueueEmpty() : 
        print('Queue is Empty')
        return
    else : 
        front += 1 
        data = queue[front]
        queue[front] = None
        return data

# Queue 추출 데이터 확인 함수 
def peek() : 
    global queue, front
    if isQueueEmpty() == True : 
        print('큐가 비었습니다!')
        return
    else : 
        return queue[front +1]

# 전역변수 
SIZE = int(input('큐 크기를 입력하세요(정수) > ')) # 대문자로 쓰는 건 상수(constant)로 사용하는 것 - 변수를 상수로 사용
queue = [None for _ in range(SIZE)] 
front = rear = -1 

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