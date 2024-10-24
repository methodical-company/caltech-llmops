# 💬 Chatbot template

A simple Streamlit app that shows how to build a chatbot using VertxAI.

### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```

### How to deploy on VertexAI

```
gcloud builds submit --tag gcr.io/<PROJECT_ID>/<SOME_PROJECT_NAME> --timeout=2h
```