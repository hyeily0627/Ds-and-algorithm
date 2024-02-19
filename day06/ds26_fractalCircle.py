# file : ds26_fractalCircle.py
# desc : 프랙탈 원 그리기

from tkinter import * 
import random

def drawCircle(x, y, r) : 
    # global count, radius
    # count += 1 
    Canvas.create_oval(x-r, y-r, x+r, y+r, width=2, outline=random.choice(colors))
    # Canvas.create_text(x, y-r, text=str(count), font=('굴림', 30))

    if r >= radius/2 : 
        drawCircle(x-r//2, y, r//2)
        drawCircle(x+r//2, y, r//2)

# count = 0
radius = 400 
wSize = 1000
colors = ['red', 'green', 'indigo', 'crimson', 'deep pink', 'gray', 'blue', 'yellow', 'orange']

# 메인코드
window = Tk()
window.title('프랙탈 원 그리기')
Canvas = Canvas(window, height = wSize, width = wSize, bg='black')

# cx-r, cy-r(좌측 상단 x, y) / cx+r, cy+r(우측 하단 x, y)
# Canvas.create_oval(cx-r, cy-r, cx+r, cy+r, width= 20, outline= 'deep pink')

drawCircle(wSize//2, wSize//2, radius)

Canvas.pack()
window.mainloop()