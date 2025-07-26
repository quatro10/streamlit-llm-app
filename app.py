from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

# ストリームリットページ設定
st.set_page_config(page_title="専門家AIチャット", page_icon="🤖")

# タイトルと説明
st.title("💬 専門家AIチャット")
st.write("""
このアプリでは、選択した分野の専門家AIがあなたの質問に答えます。  
以下の手順でご利用ください：

1. 専門家の種類を選択してください  
2. 質問を入力してください  
3. 「送信」ボタンを押すと、AIが回答を返します
""")

# 専門家の種類を定義
expert_types = {
    "心理学者": "あなたは経験豊富な心理学者です。相手の感情や心の動きを理解し、思いやりのある回答をしてください。",
    "経営コンサルタント": "あなたは優れた経営コンサルタントです。ビジネスやマネジメントに関する質問に的確かつ実用的な助言をしてください。",
    "医師": "あなたは信頼できる内科医です。健康や医学に関する質問に対して、明確で冷静な回答をしてください。"
}

# 入力フォーム（ラジオボタンとテキスト）
selected_expert = st.radio("専門家を選んでください：", list(expert_types.keys()))
user_input = st.text_input("質問を入力してください：", placeholder="例）ストレスとの付き合い方を教えてください")

# LLM呼び出し用関数
def get_expert_response(question: str, expert_role: str) -> str:
    # モデルの初期化
    llm = ChatOpenAI(model="gpt-4o", temperature=0.7)

    # プロンプト作成
    messages = [
        SystemMessage(content=expert_types[expert_role]),
        HumanMessage(content=question)
    ]

    # LLM呼び出し
    response = llm.invoke(messages)
    return response.content

# 送信ボタンと回答表示
if st.button("送信") and user_input:
    with st.spinner("AIが回答中..."):
        response = get_expert_response(user_input, selected_expert)
        st.markdown("### 🧠 AIの回答:")
        st.write(response)
