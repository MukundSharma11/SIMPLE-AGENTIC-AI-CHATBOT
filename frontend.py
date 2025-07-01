import streamlit as st

st.set_page_config(page_title='Chatbot with tools', layout= 'centered')
st.title('Chatbot with tools')
st.write('Interact with chatbot')

prompt = st.text_area("Define your AI Agent: ",placeholder="Type your response here")
model_name = st.radio(label="Select the model you want to use", options=['gemma2-9b-it', 'qwen-qwq-32b'])
allow_web_search = st.checkbox(label = "Allow web search using Tavily")

query = st.text_area("Your query: ",placeholder="Type your response here")

API_URL = 'http://127.0.0.1:9999/chat'

if st.button("Ask Agent"):
    if query.strip():
        import requests
        
        payload = {
            "model_name": model_name,
            "prompt": prompt,
            "messages": [query],
            "allow_search": allow_web_search
        }

        response = requests.post(url=API_URL, json=payload)
        if response.status_code == 200:
            response_data = response.json()
            print(response_data)
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.header("Agent Response")
                st.markdown(f"Final Response Below:\n\n{response_data}")






