# seo-google-bing-indexnow
 Streamlit App for IndexNOW Ping to Google and Bing

 ## Why?
 In my Inhouse SEO Daily Business i often want to ping google and bing after small updates to a specific url, in order to get the fresh content get recrawled and indexed as soon as possible. Especially after bulk updates I don't want to ping google using the web UI due to its slowness.

 After using the python script for quite some time I figured i transport it to streamlit for coworkers to use as well.

 The second use case consists of inspect data from google. In the past I used to work with screaming frog for these informations but sometimes it's too much work to set it up for the needed use case. In these scenarios I prefer to get the inspect data directly from the inspection API.

 ## How?
 Currently the project is behind a login wall due to the indexing API requiring OAUTH 2.0. You need to set up a service account on google cloud platform, obtain an credentials json and save the credentials as YAML to streamlit secrets.

 You can find more informations on how to setup the authentication part here: https://developers.google.com/search/apis/indexing-api/v3/prereqs

 ## Result
 

### Use Case 1: Ping google and bing with bulk urls for crawling
<img width="724" alt="Screenshot 2023-10-27 at 20 44 19" src="https://github.com/curarin/seo-google-indexnow/assets/145868208/7ed3a852-9e2c-46f7-ae81-20d75efdc39f">

### Use Case 2: Request current informations about indexing state
<img width="732" alt="Screenshot 2023-10-27 at 20 44 54" src="https://github.com/curarin/seo-google-indexnow/assets/145868208/3d383f71-ed1e-4b1f-b750-2b4041ea6dff">
