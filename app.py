
import streamlit as st
import hmac

import tabs.sidebar as sidebar
import tabs.indexnow as indexnow
import tabs.inspect_api as inspect_api

st.set_page_config(
    layout="centered",
    page_title="Google & Bing API Tool | Paul Herzog",
    initial_sidebar_state="expanded", #collapsed
    page_icon="🤖"
)

with st.sidebar:
    sidebar.sidebar()

########################################################################

# Main Streamlit app starts here
tab1, tab2 = st.tabs([
    "Google & Bing IndexNOW |",
    "Google Indexing Status"
    ])


with tab1:
    indexnow.indexnow_api_call()

with tab2:
    inspect_api.inspect_api_call()