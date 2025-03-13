from tkinter import *
from tkinter import scrolledtext
import ollama

# 모델 불러오기
models = ollama.list()  # 사용할 수 있는 모델 목록 가져오기
model_nm = "mistral"  # 사용할 모델 이름
ollama.pull(model_nm)  # 모델 다운로드

# 대화 기록(컨텍스트 유지)
messages = []
messages.append({"role": "system", "content": "너는 친절한 AI비서, 짧고 간결한 한글 답변을 제공해줘."})

def send_message(event=None):
    message = entry.get()
    if message:
        chat_window.config(state=NORMAL)
        chat_window.insert(END, f"\nYou:{message}\n")
        chat_window.config(state=DISABLED)
        entry.delete(0, END)
        chat_window.yview(END) # 자동 스크롤 내려감
        # ollama 에게 요청
        # 사용자 입력 추가
        messages.append({"role": "user", "content": message})
        # 스트리밍 응답 받기
        res_stream = ollama.chat(model=model_nm, messages=messages, stream=True)
        ai_all_response = ""

        # 응답 내용을 출력
        # 스트리밍된 응답을 실시간으로 출력
        for part in res_stream:
            text = part["message"]["content"]
            print(text, end="", flush=True)  # 응답 실시간 출력
        # chat_window.insert(text, f"\nollama:{text}\n")  # 응답 실시간 출력
            ai_all_response += text  # 전체 응답 저장

        print()  # 줄바꿈
        # 대화 컨텍스트에 AI 응답 추가 (중복 방지)
        messages.append({"role": "assistant", "content": ai_all_response})

app = Tk()
app.title("Chat UI")
app.geometry("400x500")
# 채팅 창
chat_window = scrolledtext.ScrolledText(app, wrap=WORD, state=DISABLED, height=20, width=50)
chat_window.pack(pady=10, padx=10, expand=True, fill=BOTH)

# 입력프레임
input_frame = Frame(app)
input_frame.pack(pady=10, padx=10, fill=X)
# input
entry = Entry(input_frame)
entry.pack(side=LEFT, padx=5, pady=5, expand=True, fill=X)
# btn
btn = Button(input_frame, text="Send", command=send_message)
btn.pack(side=RIGHT, padx=5, pady=5)
app.mainloop()
