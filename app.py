
import streamlit as st
import hmac

import tabs.sidebar as sidebar
import tabs.indexnow as indexnow
import tabs.inspect_api as inspect_api

st.set_page_config(
    layout="wide",
    page_title="Google Ping Tool | Paul Herzog",
    initial_sidebar_state="expanded", #collapsed
    page_icon="🤖"
)

with st.sidebar:
    sidebar.sidebar()

########################################################################
########################################################################
########################################################################
def check_password():
    """Returns `True` if the user had a correct password."""

    def login_form():
        """Form with widgets to collect user information"""
        with st.form("Credentials"):
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.form_submit_button("Log in", on_click=password_entered)

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["username"] in st.secrets[
            "passwords"
        ] and hmac.compare_digest(
            st.session_state["password"],
            st.secrets.passwords[st.session_state["username"]],
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the username or password.
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    # Return True if the username + password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show inputs for username + password.
    login_form()
    if "password_correct" in st.session_state:
        st.error("😕 User not known or password incorrect")
    return False
if not check_password():
    st.stop()
########################################################################
########################################################################
########################################################################
# Main Streamlit app starts here
tab1, tab2 = st.tabs([
    "Google IndexNOW",
    "Google Indexing Status"
    ])


with tab1:
    indexnow.indexnow_api_call()

with tab2:
    inspect_api.inspect_api_call()