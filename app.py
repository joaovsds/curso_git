import streamlit as st
from src.extraction import load_data

st.st_page_config(layout='wide')

def main():
    df = load_data

    st.dataframe(df)

if __name__ == '__main__':
    main()