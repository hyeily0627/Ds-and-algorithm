# file : ds23_recursion_sum.py
# desc : 재귀호출 합산 함수

def addNumber(num):
    if num <= 1 :
        return 1
    
    return num + addNumber(num-1)
# 5 + addNumber(4)[4 + addNumber(3)[3 + addNumber(2)[2 + addNumber(1)]]]

print(addNumber(5))
