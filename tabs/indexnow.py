import streamlit as st
import json
from googleapiclient.discovery import build
from google.oauth2 import service_account

def indexnow_api_call():
    data = {
        "type": "service_account",
        "project_id": st.secrets["service_account"]["project_id"],
        "private_key_id": st.secrets["service_account"]["private_key_id"],
        "private_key": st.secrets["service_account"]["private_key"],
        "client_email": st.secrets["service_account"]["client_email"],
        "client_id": st.secrets["service_account"]["client_id"],
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": st.secrets["service_account"]["client_x509_cert_url"]
        }

    service_account_json = json.dumps(data, indent=4)
    service_account_info = json.loads(service_account_json)
    # Path to your service account JSON key file
    KEY_FILE = service_account_info
    credentials = service_account.Credentials.from_service_account_info(KEY_FILE)
    #
    indexing_api = build('indexing', 'v3', credentials=credentials)

    # Input field
    st.header("Ping Google for Crawling")
    st.write("Paste urls in the following text area (1 URL in each line) and request crawling by pressing the 'Index Now' button.")
    st.subheader("Copy Paste URLs in here")
    urls_to_be_pinged = st.text_area("1 URL in each line...",  key = "urls pinged for crawling")
    urls_to_be_pinged = [urls_to_be_pinged.strip() for urls_to_be_pinged in urls_to_be_pinged.split("\n")]
    st.divider()
    # Send URL notifications
    if st.button("Index Now"):
        for url in urls_to_be_pinged:
            try:
                indexing_api.urlNotifications().publish(
                    body={
                        'url': url,
                        'type': 'URL_UPDATED'
                    }).execute()
                st.success(f"Notification sent for URL: {url}")
            except Exception as e:
                st.error(f"Error sending notification for URL {url}: {e}")
