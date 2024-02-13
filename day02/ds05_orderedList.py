# file : ds05_orderedList.py
# desc : 다항식 선형 리스트 표현과 계산 프로그램 

# px = [7, -4, 0, 5]
# print(px)
# # 전체 배열 길이가 4이므로 4-1인 3부터 카운트 해서 계산 

# x = 2 
# pxVal = 7*x**3 -4*x**2 + 0*x**1 + 5*x**0
# print(pxVal)

## 함수 선언 부분 
def printPoly(p_x):
    term = len(p_x) - 1
    polyStr = 'p(x) ='

    for i in range(len(px)) : 
        coef = p_x[i]

        if(coef >= 0) :
            polyStr += '+'
        polyStr += str(coef) +'x^'+ str(term) + ''
        term -= 1
    
    return polyStr

def calcPoly(xVal,p_x) : 
    retValue = 0 
    term = len(p_x) - 1 # 최고차항 숫자 = 배열길이 - 1

    for i in range(len(px)) : 
        coef = p_x[i]
        retValue += coef * xVal ** term
        term -= 1

    return retValue

## 전역변수 선언 부분
px =[7, -4, 0, 5]      # = 7x^3 -4x^2 +0x^1 +5x^0 

## 메인 코드 부분 
if __name__ == '__main__':
    
    pStr = printPoly(px)
    print(pStr)

    xValue = int(input('x값 -->'))

    pxValue = calcPoly(xValue, px)
    print(pxValue)