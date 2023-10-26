import streamlit as st
import json
from googleapiclient.discovery import build
from google.oauth2 import service_account

def inspect_api_call():
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
    scopes = [
    'https://www.googleapis.com/auth/webmasters',
    'https://www.googleapis.com/auth/webmasters.readonly'
    ]
 
    credentials = service_account.Credentials.from_service_account_info(KEY_FILE, scopes = scopes)
    #
    inspect_api = build('searchconsole', 'v1', credentials=credentials)

    # Input field
    st.header("Request current indexing informations")
    st.write("Choose the correct google search console domain for your use case, put in the urls you want crawling informations and press the button 'Get inspect data'")
    domain_choosen = st.selectbox("Select Search Console Domain", ["sc-domain:urlaubsguru.de", "sc-domain:urlaubsguru.at", "sc-domain:holidayguru.ch", "sc-domain:holidayguru.nl", "sc-domain:holidayguru.es"])
    urls_crawling_data_needed = st.text_area("Put URLs in here", key = "urls crawling data needed")
    urls_crawling_data_needed = [urls_crawling_data_needed.strip() for urls_crawling_data_needed in urls_crawling_data_needed.split("\n")]
    st.divider()
    # check for coverage state to print warnings in case of indexing problems
    url_is_on_google = ["Submitted and indexed"]
    url_is_not_on_google = ["Excluded by 'noindex' tag", "URL is unknown to Google", "Page with redirect", "Crawled - currently not indexed", "Not found (404)", "Alternate page with proper canonical tag", "Duplicate without user-selected canonical"]
    url_is_on_google_with_issues = ["Indexed, though blocked by robots.txt", "Blocked by robots.txt"]
    # Send URL notifications
    if st.button("Get Inspect Data"):
        for url in urls_crawling_data_needed:
            try:
                response = inspect_api.urlInspection().index().inspect(
                    body={
                        'inspectionUrl': url,
                        'siteUrl': domain_choosen
                    }).execute()
                inspectionResult = response['inspectionResult']
                coverageState = response["inspectionResult"]["indexStatusResult"]["coverageState"]
                robotsTxtState = response["inspectionResult"]["indexStatusResult"]["robotsTxtState"]
                indexingState = response["inspectionResult"]["indexStatusResult"]["indexingState"]
                lastCrawlTime = response["inspectionResult"]["indexStatusResult"]["lastCrawlTime"]
                pageFetchState = response["inspectionResult"]["indexStatusResult"]["pageFetchState"]
                googleCanonical = response["inspectionResult"]["indexStatusResult"]["googleCanonical"]
                userCanonical = response["inspectionResult"]["indexStatusResult"]["userCanonical"]
                crawledAs = response["inspectionResult"]["indexStatusResult"]["crawledAs"]
                st.subheader(url)
                if coverageState in url_is_on_google:
                    st.success(f"{coverageState}")
                elif coverageState in url_is_on_google_with_issues:
                    st.warning(f"{coverageState}")
                elif coverageState in url_is_not_on_google:
                    st.error(f"{coverageState}")
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"**Robots.txt Status**")
                    st.write(robotsTxtState)
                    st.markdown("**Indexing Status**")
                    st.write(indexingState)
                    st.markdown("**Last Crawl Time**")
                    st.write(lastCrawlTime)
                    st.markdown("**Page Fetch State**")
                    st.write(pageFetchState)
                with col2:
                    st.markdown("**Canonical Tag selected by Google**")
                    st.write(googleCanonical)
                    st.markdown("**Canonical Tag declared by user**")
                    st.write(userCanonical)
                    st.markdown("**Google Bot used for crawling**")
                    st.write(crawledAs)
                st.divider()
            except Exception as e:
                st.error(f"Error sending notification for URL {url}: {e}")
