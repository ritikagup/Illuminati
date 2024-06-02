import streamlit as st
from utils import scrape_text, summarize_text, generate_markmap
from streamlit_markmap import markmap


st.title("Illuminati")
st.write("Welcome to Illuminati - Your AI Article Summarizer and Mindmap Creator")


st.header("Submit Article URL")
article_url = st.text_input("Enter the URL of the article")


if st.button("Submit"):
   if article_url:
       text = scrape_text(article_url)
       if text and not text.startswith("Request failed"):
           summary = summarize_text(text)
          
           # Display Summary
           st.header("Summary")
           st.write(summary)
          
           # Generate and Display Mindmap
           st.header("Mindmap")
           data = generate_markmap(text)
           markmap(data, height=400)
       else:
           st.warning("Failed to retrieve the website.")
   else:
       st.warning("Please enter the URL of the article.")


