# day3-4
from tkinter import *
from tkinter import messagebox
import random
# 터미널에서 실행 (공유하기)
# .py to .exe
# pip install pyinstaller
app = Tk()
app.title("로또 번호 생성기!")
app.geometry("250x50")
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
# app.grid_rowconfigure(0, weight=1)
# app.grid_rowconfigure(1, weight=1)

lab = Label(app, text='수량')
lab.grid(row=0, column=0)
txt = Entry(app)
txt.grid(row=0, column=1)

def fn_click():
    msg = txt.get()
    lotto = ""
    for _ in range(int(msg)):   # _ 의미없음. 문법상 무언가 있어야하기 때문에 씀
        lotto += f"{str(sorted(make_lotto()))} \n"
    # 수량을 입력받아서
    # 수량만큼 생성
    # 생성 번호를 출력!
    messagebox.showinfo("행운의 번호:" , lotto)

def make_lotto():
    lotto_num = set()
    while len(lotto_num) < 6:
        lotto_num.add(random.randint(1, 45))
    return lotto_num

btn = Button(app, text='생성!', command=fn_click) # 함수 이름만, ()넣지 말기
btn.grid(row=1, column=0, columnspan=2, sticky='ew')

app.mainloop()