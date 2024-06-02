import requests
import ollama
from bs4 import BeautifulSoup
import re
import json


def scrape_text(url):
   headers = {
       "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
   }
   try:
       response = requests.get(url, headers=headers)
       response.raise_for_status()


       if 'text/html' not in response.headers['Content-Type']:
           return "Invalid content type"
      
       soup = BeautifulSoup(response.content, "html.parser")
       text = soup.get_text(separator=' ', strip=True)
       return text
   except requests.RequestException as e:
       return f"Request failed: {e}"


def preprocess_text(text):
   text = re.sub(r'http\S+|www.\S+', '', text)
   text = re.sub(r'\W', ' ', text)
   return text


def summarize_text(text):
   client = ollama.Client()
   paragraphs = text.split("\n\n")
   detailed_summary = ""


   for paragraph in paragraphs:
       prompt = (
           "Provide a detailed summary of the following text section. Include all main ideas and essential information, "
           "eliminating extraneous language but maintaining depth and detail. Ensure the summary covers all important aspects. Text: " + paragraph
       )
       request_data = {
           "model": "mistral",
           "prompt": prompt,
           "stream": False
       }


       try:
           response = requests.post(
               "http://localhost:11434/api/generate",
               headers={'Content-Type': 'application/json'},
               data=json.dumps(request_data)
           )


           if response.status_code == 200:
               response_data = response.json()
               summary = response_data.get("response", "")
               detailed_summary += summary + " "
           else:
               return f"Error: HTTP {response.status_code} - {response.text}"
       except requests.RequestException as e:
           return f"Request failed: {e}"


   return detailed_summary.strip()


def generate_markmap(text):
   client = ollama.Client()
   prompt = "Please convert the given article into a markdown file suitable for creating a detailed visual mindmap. Keep sentences short and focused, and emphasize key points with headings and bullet points. Text: " + text
  
   request_data = {
       "model": "mistral",
       "prompt": prompt,
       "stream": False
   }
  
   response = client.generate(model=request_data["model"], prompt=request_data["prompt"], stream=request_data["stream"])
  
   if isinstance(response, dict):
       markdown_output = response.get("response", "")
       return markdown_output
   else:
       print("Unexpected response format")
       return None


