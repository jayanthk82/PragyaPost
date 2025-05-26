import streamlit as st
from chatgpt import ChatGPT,generate_linkedin_post
from SLM import slm
import time
st.title("LinkedIn Post Generator")
st.write("")
st.write("")
col1,col2 = st.columns(2)
row = st.container()

if "response" not in st.session_state:
    st.session_state.response = False
if "summary" not in st.session_state:
    st.session_state.summary = False
if "summary_key" not in st.session_state:
    st.session_state.summary_key = False
if st.session_state.get('response'):
    row.header("Post")
    row.write(st.session_state.response)
    row.write("Click on the button below to generate summary for the post")
with col1:
    past_post = st.text_input("Upload past post's if you want to use them as a reference")
with col2:
    post_topic = st.text_input("Enter the topic of your Next LinkedIn post")
    generate_post = st.button("Generate LinkedIn Post", key="generate_post")

if generate_post:
      if post_topic:
        if past_post:
            prompt = f"Generate a LinkedIn post based on the following past post: {past_post}. And the topic for new linked post is {post_topic}. Extract persona and writing style from the past posts, if possible add some emojies to the response. Note: Response within 150-300 words"
        else:
            prompt = f"Generate a LinkedIn post on the topic: {post_topic}, if possible add emojies to the response.Note: Response within 150-300 words"
        with st.spinner("Generating post..."):      
            row.write("")
            try:
              st.session_state.response = generate_linkedin_post(prompt)
              row.success("Post generated successfully!")
              row.write(st.session_state.response) 
              time.sleep(2)  # Simulate some processing time
              st.session_state.summary = True
            except Exception as e:
              st.error(f"An error occurred while generating the post: {e}")

if st.session_state.get('summary'):
    if not st.session_state.get('summary_key'):
        st.session_state.summary_key = st.button("Generate summary for the post", key="generate_summary")
    
    if st.session_state.summary_key:
        with st.spinner("Generating summary.."):
            summary = slm(st.session_state.response)
            row.success("Summary of the post:")
            row.write(summary)
            st.session_state.summary_key = False
