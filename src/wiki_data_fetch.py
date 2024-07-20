import os
import requests
from bs4 import BeautifulSoup

raw_data_dir = os.path.join(os.path.dirname(__file__), 'raw')
if not os.path.exists(raw_data_dir):
    os.makedirs(raw_data_dir)

def fetch_wiki_content(url):
    '''
    fetch content from a give wiki_URL
    '''
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        content = soup.find('div', id='mw-content-text').get_text()
        if content:
            main_content = content.find('div', {'class':'mw-parser-output'})
            if content:
                text = content.get_text(separator='\n', strip=True)
                return text
            else:
                print(f"Could not find 'mw-parser-output' in {url}")
                return None
        else:
            print(f"Could not find 'mw-content-text' in {url}")
            return None
    else:
        print(f"Failed to retrieve page: {url}")
        return None

def save_content(title, content):
    """
    save the content fetched into /raw
    """
    filename = f"{title}.txt"
    filepath = os.path.join(raw_data_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    content = fetch_wiki_content('http://127.0.0.1:8000/villagers')
    if content:
        save_content(villagers, content)
        print(f"Saved content for {villagers}")
    else:
        print(f"Failed to save content for {villagers}")

if __name__ == "__main__":
    main()