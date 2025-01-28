import streamlit as st
import pandas as pd
import os
import glob

# ディレクトリとファイルの形式
RESULT_DIR = "data"
FILE_PATTERN = "screened_stocks_*.csv"  # ワイルドカードでマッチするファイル形式

st.title("スクリーニング結果")

def get_latest_file(directory, pattern):
    """指定したディレクトリ内で、パターンに一致する最新ファイルを取得"""
    files = glob.glob(os.path.join(directory, pattern))
    if not files:
        return None
    latest_file = max(files, key=os.path.getctime)
    return latest_file

# 最新のスクリーニング結果ファイルを取得
latest_file = get_latest_file(RESULT_DIR, FILE_PATTERN)

if latest_file:
    st.subheader("最新のスクリーニング結果")
    df = pd.read_csv(latest_file)

    # Symbolカラムを文字列型に変換
    if 'Symbol' in df.columns:
        df['Symbol'] = df['Symbol'].astype(str)
    
    # インデックスをリセットして表示
    df = df.reset_index(drop=True)

    st.dataframe(df)
    st.success(f"表示中のファイル: {os.path.basename(latest_file)}")
else:
    st.warning("スクリーニング結果がまだ生成されていません。")
