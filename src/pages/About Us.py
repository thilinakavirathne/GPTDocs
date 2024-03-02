import streamlit as st



#pageConfig
st.set_page_config(layout="wide", page_title="DOC.AssistantGPT")



#Title
st.markdown(
    """
    <h2 style='text-align: center;'>Bluechip Asia Technologies</h1>
    """,
    unsafe_allow_html=True,)

st.markdown("---")


#Description
st.markdown(
    """ 
    <h5 style='text-align:center;'>Welcome to DOC.AssistantGPT, your intelligent chatbot designed to enhance your data exploration experience</h5>
    """,
    unsafe_allow_html=True)
st.markdown("---")


#AI_Assistant's Pages
st.subheader("How it work")
st.write("""
- Supports a Variety of Formats: PDF, TXT, CSV.
- Enter your OpenAI API key.
- Your OpenAI API key is securely stored in the app and never shared with anyone.
- The assistant can generate summaries or extract relevant information from documents.

""")
st.markdown("---")



