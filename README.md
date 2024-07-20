# ILLUMINATI - Article Summarizer and Mindmap Creator
Discover the magic of easy learning with ILLUMINATI! Bid farewell to long articles – this tool converts them into quick summaries and captivating mind maps. Dive into knowledge effortlessly and make learning a joy! 🚀📚


## Table of Contents
1. [Demo](#demo)
2. [Motivation](#motivation)
3. [Pipeline](#pipeline)
4. [Technologies Used](#technologies-used)
5. [Team](#team)

## Demo Video
https://github.com/ritikagup/Illuminati/assets/99736341/63f435e3-b393-4bdb-abbb-135008a3503a

## Motivation
ILLUMINATI wants to make a big positive impact on education, especially for people with ADHD and those who learn better with visuals. We believe that everyone should have access to fun and effective learning, no matter how they learn best. In today's digital world, there is a lot of information, which can be overwhelming. People with ADHD often have trouble focusing on long, text-heavy materials, and visual learners might find traditional methods boring and hard to understand. ILLUMINATI uses advanced technology to solve these problems, making learning easy and enjoyable for everyone.

## Pipeline
How ILLUMINATI transforms articles into summarized content and visual mind maps:

1) Article Input:
Users provide an article URL as input to the application.

2) Text Scraping:
The application uses BeautifulSoup to scrape and extract text content from the provided article URL.
Various HTML structures are handled to ensure robust extraction of meaningful content.

3) Text Preprocessing:
Extracted text undergoes preprocessing to remove unwanted characters, URLs, and non-alphanumeric symbols using regular expressions (re).
This step ensures that the text is in a suitable format for further analysis.

4) Text Summarization:
The cleaned text is divided into paragraphs, and each paragraph is summarized using the Mistral 7b model through the ollama.Client() API.
The process is optimized to handle large volumes of text, ensuring concise and comprehensive summaries while eliminating extraneous details.

5) Mind Map Generation:
The cleaned text is converted into a markdown format suitable for creating visual mind maps using the Mistral model.
Key points and ideas are emphasized with headings and bullet points, ensuring clarity and focus in the mind map structure.
Mind maps are rendered using the streamlit_markmap library, providing an interactive visual representation of the summarized content.

6) User Interaction:
Users interact with the application through a frontend interface built with Streamlit.
They input article URLs, view generated summaries, and explore interactive mind maps directly within the Streamlit app.

## Technologies,Tools and Models

<img src="https://github.com/ritikagup/Illuminati/assets/99736341/3293c68c-23e5-4cdc-ae6a-0650de855793" alt="tools" width="350" height="300">

- Python: Primary programming language for backend development and scripting tasks.

- Streamlit: Web application framework used for building interactive and data-driven applications.

- Beautiful Soup: Python library for web scraping, used to extract text content from article URLs.

- Ollama: It is is an open-source project that serves as a powerful and user-friendly platform for running LLMs on your local machine. It acts as a bridge between the complexities of LLM technology and the desire for an accessible and customizable AI experience.

- Markdown: Lightweight markup language used for formatting text content and generating visual mind maps.

- Markmap: It is visualization tool that transforms hierarchical data, such as nested lists or mind maps, into interactive diagrams. It offers an intuitive way to organize and explore complex relationships, with customizable options for appearance and layout.

- Mistral: Mistral 7B is a 7-billion-parameter language model released by Mistral AI. Mistral 7B is a carefully designed language model that provides both efficiency and high performance to enable real-world applications. Due to its efficiency improvements, the model is suitable for real-time applications where quick responses are essential. At the time of its release, Mistral 7B outperformed the best open source 13B model (Llama 2) in all evaluated benchmarks.

## Team
- Ritika Gupta

