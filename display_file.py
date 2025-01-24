import streamlit as st
import pandas as pd

st.title("スクリーニング結果")

uploaded_file = st.file_uploader("スクリーニング結果のCSVをアップロード", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
    st.success("CSVファイルの内容を表示しました！")
else:
    st.info("CSVファイルをアップロードしてください。")
