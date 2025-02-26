import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Feature Engineering", page_icon="📈")
st.sidebar.header("Feature Engineering")

st.title("Feature Engineering")

if "df_select" not in st.session_state:
    st.session_state["df_select"] = pd.DataFrame()

if "df_cat_columns" not in st.session_state:
    st.session_state["df_cat_columns"] = pd.DataFrame()

st.write("### Current DataFrame")
st.write(st.session_state["df_select"])

st.write(f"New shape:")
st.write(st.session_state["df_select"].shape)

st.write("---")
st.write("### Which categorical columns should be transformed with OneHotEncoder?")

categorical_columns = (
    st.session_state["df_select"]
    .select_dtypes(include=[pd.CategoricalDtype(), np.object_])
    .columns.tolist()
)

for elem in categorical_columns:
    checkbox_state = st.checkbox(label=f"{elem}", key=f"fe_{elem}")
    if checkbox_state:
        st.session_state["df_cat_columns"][elem] = st.session_state["df_select"][elem]
    else:
        if elem in st.session_state["df_cat_columns"]:
            st.session_state["df_cat_columns"].drop(columns=[elem], inplace=True)


st.write(st.session_state["df_cat_columns"])
st.write(f"New shape:")
st.write(st.session_state["df_select"].shape)

if st.button("Save DataFrame to CSV"):
    st.session_state["df_cat_columns"].to_csv("../../data/interim/ohe_marked.csv")
