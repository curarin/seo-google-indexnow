import streamlit as st
import json
from googleapiclient.discovery import build
from google.oauth2 import service_account
import requests
import time

def indexnow_api_call():
    # Input field
    st.header("Ping Google & Bing for Crawling")
    st.write("Paste urls in the following text area (1 URL in each line) and request crawling by pressing the 'Index Now' button.")
    st.subheader("Copy Paste URLs in here")
    domain_name_for_bing = "https://www.urlaubsguru.de"
    domain_name_for_bing = st.selectbox("Select Domain", ["https://www.urlaubsguru.de", "https://www.urlaubsguru.at", "https://www.holidayguru.ch", "https://www.holidayguru.es", "https://www.holidayguru.nl"])
    urls_to_be_pinged = st.text_area("1 URL in each line...",  key = "urls pinged for crawling", height=300)
    urls_to_be_pinged = [urls_to_be_pinged.strip() for urls_to_be_pinged in urls_to_be_pinged.split("\n")]
    st.divider()

    ### GOOGLE PING DATA
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
    KEY_FILE = service_account_info
    credentials = service_account.Credentials.from_service_account_info(KEY_FILE)
    indexing_api = build('indexing', 'v3', credentials=credentials)

    ### BING PING DATA
    endpoint_bing = "https://ssl.bing.com/webmaster/api.svc/json/SubmitUrl"
    bing_api_key = st.secrets["bing"]["api_key"]
    bing_endpoint_apiquota = f"https://ssl.bing.com/webmaster/api.svc/json/GetUrlSubmissionQuota?apikey={bing_api_key}&siteUrl={domain_name_for_bing}"
    headers_bing = {
        "Content-Type": "application/json",
        "charset": "utf-8"
    }
    params_bing = {
        "apikey": bing_api_key
    }

    # Send URL notifications to google and bing
    if st.button("Index Now"):
        with st.status("Search Engine Ping in process...", expanded=True) as status:
            for url in urls_to_be_pinged:
                try:
                    # here comes google
                    indexing_api.urlNotifications().publish(
                        body={
                            'url': url,
                            'type': 'URL_UPDATED'
                        }).execute()
                    st.write(f"Successfully pinged Google for {url}")
                    #st.success(f"Google successfully pinged for URL: {url}")
                    data_bing = {
                                "siteUrl": domain_name_for_bing,
                                "url": url
                            }
                    response_bing = requests.post(endpoint_bing, json=data_bing, headers=headers_bing, params=params_bing)
                    if response_bing.status_code == 200:
                        st.write(f"Successfully pinged Bing for {url}")
                    else:
                        st.warning(f"Error {response_bing.status_code}: {response_bing.text}")
                    time.sleep(2)
                except Exception as e:
                    st.error(f"Error sending notification for URL {url}: {e}")
            ###here comes bing
            
        status.update(label="URLs sent to search engines.", state="complete", expanded=False)          
        response_bing_apiquota = requests.get(bing_endpoint_apiquota)
        if response_bing_apiquota.status_code == 200:
            data = response_bing_apiquota.json()
            if 'd' in data and '__type' in data['d'] and data['d']['__type'] == "UrlSubmissionQuota:#Microsoft.Bing.Webmaster.Api":
                daily_quota = data['d']['DailyQuota']
                monthly_quota = data['d']['MonthlyQuota']
                st.warning(f"Daily Quota left for Bing API: {daily_quota}")            
                st.warning(f"Monthly Quota left for Bing API: {monthly_quota}")     
