import streamlit as st
import streamlit.components.v1 as components

# Page settings
st.set_page_config(page_title="Student Performance Dashboard", layout="wide")

st.title("📊 Student Performance Dashboard")

# HTML file ka naam yahan daalo (agar file ka naam alag hai toh change kar dena)
HTML_FILE = "student_performance_dashboard.html"

with open(HTML_FILE, "r", encoding="utf-8") as f:
    html_content = f.read()

# Height adjust kar sakte ho apni screen ke hisab se
components.html(html_content, height=3500, scrolling=True)