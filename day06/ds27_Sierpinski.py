# file : ds27_Sierpinski.py
# desc : 시에르핀스키 삼각형 그리기 

from tkinter import * 

## 클래스 함수 선언
def drawTriangle(x, y, size) : 
    if size >= 30 :
        drawTriangle(x, y, size/2) # 왼쪽 아래 작은 삼각형
        drawTriangle(x+size/2, y, size/2) # 오른쪽 아래 작은 삼각형 
        drawTriangle(x+size/4, int(y-size*(3**0.5)/4), size/2) # 위쪽 작은 삼각형
    else :
        Canvas.create_polygon(x, y, x+size, y, x +size/2, y-size*(3**0.5/2), fill ='pink', outline= "black")

## 전역변수 선언 
wSize = 1000
radius = 400

## 메인코드부분
window = Tk()
window.title('삼각형 모양의 프랙탈')
Canvas = Canvas(window, height=wSize, width=wSize, bg='white')

drawTriangle(wSize/5, wSize/5*4, wSize*2/3)

Canvas.pack()
window.mainloop()