# ILLUMINATI - Article Summarizer and Mindmap Creator
Discover the magic of easy learning with ILLUMINATI! Bid farewell to long articles – this tool converts them into quick summaries and captivating mind maps. Dive into knowledge effortlessly and make learning a joy! 🚀📚


## Table of Contents
1. [Demo](#demo)
3. [Motivation](#motivation)
4. [Technical Aspect](#technical-aspect)
5. [Pipeline](#pipeline)
6. [Installation](#installation)
7. [Run](#run)
8. [Directory Tree](#directory-tree)
9. [To Do](#to-do)
10. [Technologies Used](#technologies-used)
11. [Team](#team)

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

4.Text Summarization:
The cleaned text is divided into paragraphs, and each paragraph is summarized using advanced AI models.
ollama.Client() API is utilized to generate detailed summaries that retain essential information while eliminating extraneous details.
Summarization process handles large volumes of text, providing concise and comprehensive summaries.

5.Mind Map Generation:
Text is converted into a markdown format suitable for creating visual mind maps.
Key points and ideas are emphasized with headings and bullet points, ensuring clarity and focus in the mind map structure.
Mind maps are rendered using the streamlit_markmap library, providing an interactive visual representation of the summarized content.

6.User Interaction:
Users interact with the application through a frontend interface built with Streamlit.
They input article URLs, view generated summaries, and explore interactive mind maps directly within the Streamlit app.
