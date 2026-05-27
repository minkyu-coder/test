import streamlit as st
import google.generativeai as genai

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="공부 도우미 챗봇",
    page_icon="📚",
    layout="centered"
)

st.title("📚 공부 도우미 Gemini 챗봇")
st.caption("Gemini 2.5 Flash Lite 기반 AI 공부 챗봇")

# -----------------------------
# API KEY 불러오기
# -----------------------------
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    st.error("❌ secrets.toml에 GEMINI_API_KEY가 설정되지 않았습니다.")
    st.stop()

# -----------------------------
# Gemini 설정
# -----------------------------
genai.configure(api_key=api_key)

# 모델 생성
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash-lite"
)

# -----------------------------
# 세션 상태 초기화
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# 이전 채팅 출력
# -----------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# 사용자 입력
# -----------------------------
prompt = st.chat_input("공부 질문을 입력하세요!")

if prompt:

    # 사용자 메시지 저장
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # 사용자 메시지 출력
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI 응답 생성
    with st.chat_message("assistant"):

        with st.spinner("공부 중..."):

            try:
                # 대화 기록 구성
                chat_history = []

                for msg in st.session_state.messages:
                    role = "user" if msg["role"] == "user" else "model"

                    chat_history.append({
                        "role": role,
                        "parts": [msg["content"]]
                    })

                # 응답 생성
                response = model.generate_content(chat_history)

                reply = response.text

            except Exception as e:
                reply = f"❌ 오류가 발생했습니다.\n\n{str(e)}"

            st.markdown(reply)

    # AI 응답 저장
    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })

# -----------------------------
# 사이드바
# -----------------------------
with st.sidebar:
    st.header("⚙️ 설정")

    if st.button("채팅 기록 초기화"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.markdown("### 📌 사용 모델")
    st.code("gemini-2.5-flash-lite")
