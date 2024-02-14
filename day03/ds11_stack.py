# file : ds11_stack.py
# desc : 스택 전체 구현 

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
SIZE = 5
stack = [None for _ in range(SIZE)]
top = - 1 
    
# 메인코드 
if __name__== '__main__' : 
    while True : 
        select = input('PUSH(p),POP(o),PEEK(e),EXIT(x)>' )

        if select.lower() == 'p': 
            data = input('입력데이터 >> ')
            push(data)
            print(f'스택상태 : {stack}')
        elif select.lower() == 'o': 
            data = pop()
            print(f'추출데이터 : {data}')
            print(f'스택상태 : {stack}')
        elif select.lower() == 'e': 
            data = peek()
            print(f'확인데이터 : {data}')
            print(f'스택상태 : {data}')
        elif select.lower() == 'x' : 
            exit(0)
        else : 
            continue