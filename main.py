import streamlit as st # pip install streamlit - for creating web apps
from scrape import scrape_website, extract_body_content, clean_body_content, split_dom_content
from parse import parse_with_ollama

st.title('AI Web Scraper')
url = st.text_input('Enter a Website URL to scrape:')

if st.button('Scrape Site'):
    st.write('Scraping website...')
    result = scrape_website(url)
    #print(result)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)
    
    st.session_state.dom_content = cleaned_content

    with st.expander("View DOM content"):
        st.text_area("DOM Content", cleaned_content, height=300)
    st.success('Scraping completed!')

if 'dom_content' in st.session_state: # Session state is used to store data between interactions
    parse_description = st.text_area("Describe what you want to parse?")

    if st.button('Parse Content'):
        if parse_description:
         st.write('Parsing content...')

         dom_chunk = split_dom_content(st.session_state.dom_content)  # Taking only the first chunk for simplicity
            # Here you would integrate with your AI model to parse the content based on user description
         dom_chunks = split_dom_content(st.session_state.dom_content)
         result = parse_with_ollama(dom_chunks, parse_description)
         st.write(result)
         
