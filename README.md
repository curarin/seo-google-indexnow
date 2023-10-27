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
<img width="853" alt="Screenshot 2023-10-26 at 21 41 25" src="https://github.com/curarin/seo-google-indexnow/assets/145868208/121b6618-054e-4cbf-931e-e29a0cec40ff">

### Use Case 2: Request current informations about indexing state
<img width="816" alt="Screenshot 2023-10-26 at 21 41 37" src="https://github.com/curarin/seo-google-indexnow/assets/145868208/6e3d677c-91a7-4f79-87c0-256ab2d9c294">
