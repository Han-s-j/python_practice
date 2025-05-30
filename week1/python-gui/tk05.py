import tkinter as tk
from tkinter import ttk     #향산된 tkinter

import requests
api_url ="https://open.er-api.com/v6/latest/USD"
data = api_url.json()
print(data)
# exchange_rate = re_data['rates']['KRW'] # 현재환율
ex_rates = data['rates']

def convert_currency():
    print('달러',entry_usd.get())
    print('콤보박스 선택', currency.get())
    user_usd = entry_usd.get() / ex_rates
    result.config(text= entry_usd.get()+' USD'+'='+str(user_usd))
app = tk.Tk()
app.title("환율 변환기")
app.geometry("300x200")
# USD 입력
tk.Label(app, text='USD 금액:').pack(pady=5)
entry_usd = tk.Entry(app)
entry_usd.pack()
# 통화 선택(콤보)
tk.Label(app, text='변환할 통화 선택').pack(pady=5)
currency = ttk.Combobox(app, values=list(ex_rates.keys()))
currency.pack()
#currency.set("KRW")
currency.current(0) # 0번째로 디폴트 선택
# 반환 버튼
btn = tk.Button(app, text='변환!', command=convert_currency)
btn.pack(pady=5)
# 결과 출력
result = tk.Label(app, text='결과가 여기에 표시 됨.')
result.pack(pady=10)
app.mainloop()