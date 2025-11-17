from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

def scrape_website(url):
    print("Launching Chrome browser...")

    options = Options()
    options.add_argument("--headless")  # Optional: remove if you want UI
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Automatically download / manage ChromeDriver
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    try:
        driver.get(url)
        print("Page Loaded!")

        # time.sleep(10)  # Wait for content to load
        html = driver.page_source
        return html

    finally:
        driver.quit()
        print("Browser closed.")

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser") # BS will identify the html code and parse the content in the body tag
    body_content = soup.body
    
    if body_content: # making sure the body content is not empty, error handling
        return str(body_content)
    return ""
def clean_body_content(body_content): 
    soup = BeautifulSoup(body_content, 'html.parser') # cleaning the body content using BS

    for script_or_style in soup(['script', 'style']): # Remove scripts and styles
         script_or_style.extract()

    cleaned_content = soup.get_text(separator='\n') # Get text with new lines as separators
    cleaned_content = "\n".join( line.strip() for line in cleaned_content.splitlines() if line.strip()) # Remove extra whitespace and empty lines
  
    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i:i+max_length] for i in range(0, len(dom_content), max_length)
        ] # starting point, ending point, step size (6000 characters)
    


        