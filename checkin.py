import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Googleスプレッドシートの設定
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('autogptapril25-3a40ce8e89e4.json', scope)
client = gspread.authorize(creds)
sheet = client.open('checkin-airbnb').sheet1

# アプリのタイトル
st.title('チェックインフォーム')

# フォームの作成
with st.form(key='checkin_form'):
    room_number = st.text_input('部屋番号 / Room Number')
    name = st.text_input('名前 / Name')
    checkin_date = st.date_input('チェックイン日 / Check-in Date', min_value=datetime.today())
    checkout_date = st.date_input('チェックアウト日 / Check-out Date', min_value=datetime.today())
    country = st.selectbox('国 / Country', [
        'Japan 日本', 'USA 米国', 'China 中国', 'France フランス', 
        'Germany ドイツ', 'Australia オーストラリア', 'Korea 韓国', 
        'United Kingdom イギリス', 'Canada カナダ', 'Brazil ブラジル'
    ])
    if country != 'Japan 日本':
        st.write("If you are not a Japanese national, a passport is required. 日本人以外の場合はパスポートが必要です。")
        passport_number = st.text_input('パスポート番号 / Passport Number')
    else:
        passport_number = ""
    occupation = st.selectbox('職業 / Occupation', [
        'Office Worker 会社員', 'Freelance フリーランス', 
        'Unemployed 無職', 'Student 学生', 'Other その他'
    ])
    submit_button = st.form_submit_button(label='送信')

# フォーム送信時の処理
if submit_button:
    # 日付を文字列に変換
    checkin_date_str = checkin_date.strftime('%Y-%m-%d')
    checkout_date_str = checkout_date.strftime('%Y-%m-%d')

    # スプレッドシートにデータを追加
    sheet.append_row([room_number, name, checkin_date_str, checkout_date_str, country, passport_number, occupation])
    st.success('Sent Successfully. データを送信しました。')
