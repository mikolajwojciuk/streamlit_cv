import streamlit as st

st.set_page_config(page_title="About", page_icon="🙋🏻‍♂️")

st.sidebar.write(
    """<div style="width:100%;text-align:center;"><a href="www.linkedin.com/in/mikołaj-wojciuk-72956a20b" style="float:center"><img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" width="22px"></img></a></div>""",
    unsafe_allow_html=True,
)

st.header("About me")
