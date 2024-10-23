# Caltech Lab04 Step 1 

## Intro

This template is a simple Streamlit app that shows how to build a chatbot using OpenAI's GPT-3.5.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://chatbot-template.streamlit.app/)

### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```


## Steps for Tutorial

Now we will modify to run our LLM locally and the deploy in the cloud:

1. change the OpenAI functions to use VertexAI instead
2. store GOOGLE_APPLICATION_CREDENTIALS in secrets in console
3. write a docker file
4. deploy with gcloud commands to CloudRun
5. (optional) set up Cloudbuild or Github Actions to automate build process

If you get struck along the way take a look at [answers](./step1_streamlit-chatbot-answers)




