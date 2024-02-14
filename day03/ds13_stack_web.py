# file : ds13_stack_web.py
# desc : 스택 구현 _ 웹

import webbrowser
import time

# 1. 스택 상태 확인 함수 : isStackFull( )
def isStackFull():
    global SIZE, stack, top
    if top == (SIZE - 1) :
        return True # 스택이 꽉 참 
    else : 
        return False  

# 2. Push 함수
def push(data) : 
    global SIZE, stack, top
    if isStackFull() == True : 
        print('stack is Full')
        return
    else : 
        top += 1 
        stack[top] = data 

# 3. isStackEmpty( ) 함수
def isStackEmpty() :
    global SIZE, stack, top
    if top <= -1 :
        return True # 스택이 비었음
    else : 
        return False

# 4. pop 함수 
def pop() : 
    global SIZE, stack, top
    if isStackEmpty() == True : 
        return None
    else : 
        data = stack[top]
        stack[top] = None
        top -= 1
        return data    

# 5. peek 함수 
def peek():
    global stack, top 
    if isStackEmpty() == True : 
        print('스택이 비어있습니다')
        return None
    else: 
        return stack[top]
    
# 전역 변수 선언
SIZE = 10
stack = [None for _ in range(SIZE)]
top = - 1 
    
# 메인코드 
if __name__== '__main__' : 
    urls = ['naver.com', 'daum.net', 'nate.com','bing.com', 'github.com']

    for url in urls : 
        push(url)
        webbrowser.open('http://www.{url}')
        print(url, end='--->')
        time.sleep(1)
    
    print('방문종료')
    time.sleep(5) # 5초동안 아무것도 하지 않고 대기

    print(stack)

    while True : 
        url = pop() # 위의 url과 다른 지역 변수 
        if url == None : break 

        webbrowser.open(f'http://www.{url}')
        print(url, end='--->')
        time.sleep(1)
    
    print('방문종료')