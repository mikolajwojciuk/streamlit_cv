import streamlit as st

st.set_page_config(page_title="About", page_icon="🙋🏻‍♂️")

st.sidebar.write(
    """<div style="width:100%;text-align:center;"><a href="https://www.linkedin.com/in/mikołaj-wojciuk-72956a20b" style="float:center"><img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" width="22px"></img></a></div>""",
    unsafe_allow_html=True,
)

st.header("About me")
st.write(
    """I have always been fascinated by the wonders of technology that surround us every day. From simple electronic circuits to complex algorithms that help locate me on the internet. Thanks to diligence, perseverance, and a constant questioning mindset, today I not only understand how they work but also actively participate in their creation.

Through various interests and passions, I have been able to earn the title of an engineer. Through experience, I have come to understand what it means to be an engineer. I am not afraid to challenge things I do not understand and get excited when the opportunity arises to learn something new.

Numerous experiences allow me to easily navigate previously unknown situations. I enjoy solving real-world problems, and thanks to the tools at my disposal, the range of problems I can address continues to expand. My lifelong curiosity about the world enables me to answer not only the question 'how?' but also 'why?.'


Technologies I am familiar with include: TensorFlow, PyTorch, Numpy, Pandas, Huggingface ecosystem, OpenCV"""
)
