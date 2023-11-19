import streamlit as st
import openai

# OpenAI APIキーの設定
openai.api_key = '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'

def get_chatgpt_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4.0-chat",
            messages=[
                {"role": "system", "content": "あなたはフレンドリーなAIアシスタントです。"},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content']
    except Exception as e:
        return str(e)

# Streamlitアプリのレイアウト
st.title('ChatGPTを使ったシンプルなチャットボット')

# ユーザー入力フィールド
user_input = st.text_input('質問を入力してください：')

# 送信ボタン
if st.button('送信'):
    # ChatGPTへのリクエストとレスポンスの取得
    chatgpt_response = get_chatgpt_response(user_input)
    # 応答を表示
    st.text_area('ChatGPTの応答：', chatgpt_response, height=150)

# Streamlitアプリを実行するには、このスクリプトをPythonファイルとして保存し、
# コマンドラインから `streamlit run [ファイル名].py` を実行します。
