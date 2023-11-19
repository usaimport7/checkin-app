import streamlit as st
import pandas as pd
import random

# サンプルデータの作成
company_names = ['Company ' + chr(i) for i in range(65, 165)] # Company AからCompany Tまで100社
regions = ['US', 'JP', 'FR', 'ID', 'NW', 'SW', 'VT', 'GE', 'IT']
categories = ['IT', 'アウトドア', 'ホーム', '家電', '車', '食品']
sources = ['Etsy', 'Amazon', 'eBay', 'ヤフオク', '楽天', 'shopify', '展示会']

data = {
    '会社名': company_names,
    'URL': ['http://{}.com'.format(name.lower()) for name in company_names],
    '地域': random.choices(regions, k=100),
    'カテゴリ': [', '.join(random.sample(categories, random.randint(1, 3))) for _ in range(100)],
    'ソース': random.choices(sources, k=100),
    'EMAIL': ['contact@{}.com'.format(name.lower()) for name in company_names]
}
df = pd.DataFrame(data)

# Streamlitアプリケーションのレイアウト
st.title('企業データフィルタリング')

# カテゴリの選択
st.write('カテゴリを選択:')
category_cols = st.columns(len(categories))
selected_categories = [category for category, col in zip(categories, category_cols) if col.checkbox(category, key='cat_' + category)]

# 地域の選択
st.write('地域を選択:')
region_cols = st.columns(len(regions))
selected_regions = [region for region, col in zip(regions, region_cols) if col.checkbox(region, key='reg_' + region)]

# データソースの選択
st.write('ソースを選択:')
source_cols = st.columns(len(sources))
selected_sources = [source for source, col in zip(sources, source_cols) if col.checkbox(source, key='source_' + source)]

# フィルタリングされたデータの表示
filtered_df = df[df['カテゴリ'].apply(lambda x: any(cat in x.split(', ') for cat in selected_categories)) &
                 df['地域'].isin(selected_regions) &
                 df['ソース'].isin(selected_sources)]
if not filtered_df.empty:
    st.write(filtered_df)

    # CSVファイルとして出力（UTF-8 with BOM）
    st.download_button(
        label="Download data as CSV",
        data=filtered_df.to_csv(index=False, encoding='utf-8-sig').encode('utf-8-sig'),
        file_name='filtered_companies.csv',
        mime='text/csv',
    )
