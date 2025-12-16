import streamlit as st
import pandas as pd
import plotly.express as px
from data_manager import add_expense, load_data
import datetime

# 網頁基礎設置
st.set_page_config(layout="wide")
st.title("Expense Tracking Tool")
col1, col2 = st.columns(2)

# Load data
expenses = load_data()

# 左側欄位
with col1:
    st.header("Add an Expense")
    with st.form("expense_form", clear_on_submit=True):
        date = st.date_input("Date", datetime.date.today())
        amount = st.number_input("Amount", min_value=0.0, format="%.2f")
        category = st.selectbox("Category", ["Food", "Transport", "Entertainment", "Housing", "Other"])
        notes = st.text_input("Notes (Optional)")
        submitted = st.form_submit_button("Add Expense")  # 按鈕偵測

        if submitted:
            add_expense(date.strftime("%Y-%m-%d"), amount, category, notes)
            st.success("Expense added successfully!")
            expenses = load_data()  # 新增完成, 更新資料表

# 右側圓餅圖
with col2:
    st.header("Expense Visualization")
    if not expenses.empty:
        fig = px.pie(expenses, names='Category', values='Amount', title='Expenses by Category')
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("No expenses to display. Add an expense to see the chart.")

st.header("Recent Expenses")
st.dataframe(expenses.tail(10))
