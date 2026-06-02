import streamlit as st

st.title("Download Project Report")

with open("SQL COMMANDS USED.docx", "rb") as file:
    st.download_button(
        label="📄 Download Report",
        data=file,
        file_name="Project_Report.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
