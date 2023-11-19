import streamlit as st
import pandas as pd

# 仮のデータフレーム（実際にはデータベースからデータを読み込む）
data = {
    '会社名': ['Company A', 'Company B', 'Company C', 'Company D', 'Company E', 'Company F', 'Company G'],
    'URL': ['http://a.com', 'http://b.com', 'http://c.com', 'http://d.com', 'http://e.com', 'http://f.com', 'http://g.com'],
    '地域': ['Tokyo', 'Osaka', 'Nagoya', 'Hokkaido', 'Kyoto', 'Fukuoka', 'Hiroshima'],
    'カテゴリ': ['IT,家電', 'アウトドア,食品', 'ホーム', '家電', '車', '食品', 'IT'],
    'EMAIL': ['contact@a.com', 'contact@b.com', 'contact@c.com', 'contact@d.com', 'contact@e.com', 'contact@f.com', 'contact@g.com']
}
df = pd.DataFrame(data)

# Streamlitアプリケーションのレイアウト
st.title('企業データフィルタリング')

# カテゴリの選択
selected_categories = st.multiselect('カテゴリを選択', ['IT', 'アウトドア', 'ホーム', '家電', '車', '食品'])

# フィルタリングされたデータの表示
if selected_categories:
    # カテゴリ列をカンマで分割し、フィルタリング
    filtered_df = df[df['カテゴリ'].apply(lambda x: any(cat in x.split(',') for cat in selected_categories))]
    st.write(filtered_df)

    # CSVファイルとして出力（UTF-8 with BOM）
    st.download_button(
        label="Download data as CSV",
        data=filtered_df.to_csv(index=False, encoding='utf-8-sig').encode('utf-8-sig'),
        file_name='filtered_companies.csv',
        mime='text/csv',
    )
