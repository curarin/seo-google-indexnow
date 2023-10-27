# seo-google-indexnow
 Streamlit App for IndexNOW Ping to Google

 ## Why?
 In my Inhouse SEO Daily Business i often want to ping google after small updates to a specific url, in order to get the fresh content get recrawled and indexed as soon as possible. Especially after bulk updates I don't want to ping google using the web UI due to its slowness.

 After using the python script for quite some time I figured i transport it to streamlit for coworkers to use as well.

 ## How?
 Currently the project is behind a login wall due to the indexing API requiring OAUTH 2.0. You need to set up a service account on google cloud platform, obtain an credentials json and save the credentials as YAML to streamlit secrets.

 You can find more informations on how to setup the authentication part here: https://developers.google.com/search/apis/indexing-api/v3/prereqs

 ## Result
 

### Use Case 1: Ping google with bulk urls for crawling
<img width="783" alt="Screenshot 2023-10-27 at 11 30 57" src="https://github.com/curarin/seo-google-indexnow/assets/145868208/cc1fce2c-a02e-4121-aea9-7628318a8c9c">

### Use Case 2: Request current informations about indexing state
<img width="801" alt="Screenshot 2023-10-27 at 11 30 52" src="https://github.com/curarin/seo-google-indexnow/assets/145868208/c2194b92-33ac-4972-b34a-4ab0e05eb2fb">
