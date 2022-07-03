import streamlit as st
import streamlit.components.v1 as components

def show_explore_page():
    st.header("Report")

    htmlfile = open("report.html","r",encoding="utf-8")
    source_code = htmlfile.read()

    return components.html(source_code,height=15000, scrolling=True)