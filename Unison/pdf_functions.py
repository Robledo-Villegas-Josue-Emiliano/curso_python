from bs4 import BeautifulSoup
import os
from markitdown import MarkItDown
import requests

def get_webpage(url):
    try:
        response = requests.get(url, timeout=10)  # Set a timeout for the request
        response.raise_for_status()  # Check if the request was successful
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return None
        
def extract_pdf_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    pdf_links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.lower().endswith('.pdf'):
            pdf_links.append(href)
    return pdf_links
    
def download_pdf(url, filename):
    try:
        response = requests.get(url, stream=True, timeout=10)  # Set a timeout for the request
        response.raise_for_status()  # Check if the request was successful
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Downloaded: {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading the PDF: {e}")

def get_pdfs(url = "https://fi-ing.unison.mx/acuerdos-de-sesiones-del-h-colegio-de-la-facultad-interdisciplinaria-de-ingenieria-2026/"):
        download_path = "pdfs"
        if not os.path.exists(download_path):
            os.makedirs(download_path, exist_ok=True)  # Create the directory if it doesn't exist
        html = get_webpage(url)
        if not html:
            print(f"Failed to retrieve the webpage: {url}")
            exit(1)
        pdf_links = extract_pdf_links(html)
        for link in pdf_links:
            print(link)
            filename = link.split('/')[-1]  # Extract the filename from the URL
            downloaded_file = os.path.join(download_path, filename)
            download_pdf(link, downloaded_file)
            print(f"Downloaded: {filename}")



def convert_pdf_to_markdown(pdf_path, markdown_path):
    try:
        converter = MarkItDown()
        result = converter.convert(pdf_path)
        markwdown_content = result.markdown or result.text_content
        with open(markdown_path, 'w', encoding='utf-8') as f:
            f.write(markwdown_content)
    except Exception as e:
        print(f"Error converting PDF to Markdown: {e}")

def main():
    if not os.path.exists("markdown_files"):
        os.makedirs("markdown_files", exist_ok=True)  # Create the directory if it doesn't exist
    for filename in os.listdir("pdfs"):
        if filename.lower().endswith('.pdf'):
            pdf_path = os.path.join("pdfs", filename)
            markdown_path = os.path.join("markdown_files", f"{os.path.splitext(filename)[0]}.md")
            convert_pdf_to_markdown(pdf_path, markdown_path)
            print(f"Converted {filename} to Markdown.")
            
if __name__ == "__main__":
    main()

