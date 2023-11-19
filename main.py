import streamlit as st

st.title('商品LP生成器')

product = st.text_input('どんな商品を売りたい？')

if product:
    st.write(f'ここには「{product}」に関する素晴らしいLPが表示されます。')
