# file : ds22_recursion.py
# desc : 재귀호출 

import time

def open_box(): 
    global count
    print(f'{count}번째 상자를 엽니다')
    count -= 1
    if count == 0 :
        print('반지를 넣고 반환합니다')
        return

    time.sleep(0.5) # 0.5초 동안 딜레이
    open_box()  
    print('상자를 닫습니다')

count = 10 
open_box()