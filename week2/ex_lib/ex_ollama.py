import ollama

# 모델 불러오기
models = ollama.list()  # 사용할 수 있는 모델 목록 가져오기
model_nm = "mistral"  # 사용할 모델 이름
ollama.pull(model_nm)  # 모델 다운로드

# 대화 기록(컨텍스트 유지)
messages = []
messages.append({"role": "system", "content": "너는 친절한 AI비서, 짧고 간결한 한글 답변을 제공해줘."})

print("exit 또는 종료 입력시 종료")

# 대화 시작
while True:
    user_input = input("You: ")

    # 종료 조건
    if user_input.lower() in ["exit", "종료"]:
        print("ollama 종료")
        break

    # 사용자 입력 추가
    messages.append({"role": "user", "content": user_input})

    print("ollama AI:", end="", flush=True)

    # 스트리밍 응답 받기
    res_stream = ollama.chat(model=model_nm, messages=messages, stream=True)
    ai_all_response = ""

    # 스트리밍된 응답을 실시간으로 출력
    for part in res_stream:
        text = part["message"]["content"]
        print(text, end="", flush=True)  # 응답 실시간 출력
        ai_all_response += text  # 전체 응답 저장

    print()  # 줄바꿈

    # 대화 컨텍스트에 AI 응답 추가 (중복 방지)
    messages.append({"role": "assistant", "content": ai_all_response})
