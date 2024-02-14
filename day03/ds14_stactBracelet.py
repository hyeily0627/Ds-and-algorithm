# file : ds14_stactBracelet.py
# desc : 스택 전체 구현 - 괄호 매칭 검사

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

# 수식 괄호 판단 함수
def checkBracket(expr) : # '(a+b)'과 같은 문자열이 들어올 것
    for ch in expr : # '(' / 'a'/ 'b'/ ')'
        if ch in '({[<' : # 여는 괄호가 있으면 
            push(ch)
        elif ch in ')}]>' : # 닫는 괄호가 있으면 
            out = pop()
            if ch == ')' and out == '(' :
                pass #(continue)
            elif ch == '}' and out == '{' :
                pass #(continue)
            elif ch == ']' and out == '[' :
                pass #(continue)
            elif ch == '>' and out == '<' :
                pass
            else : 
                return False 
        else : 
            continue 

    if isStackEmpty() == True : 
        return True
    else : 
        return False

# 전역 변수 선언
SIZE = 50
stack = [None for _ in range(SIZE)]
top = - 1 
    
# 메인코드 
if __name__== '__main__' : 
    arr = ['(a+b)',')a*b(','((a+b)-c)]','(<a+{b+c}/[c*d]>)'] 

    for expr in arr : 
        top = -1
        print(f'{expr} ==> {checkBracket(expr)}')