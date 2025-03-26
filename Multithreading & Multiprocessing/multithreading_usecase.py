
import threading
import requests
from bs4 import BeautifulSoup

urls = ['https://python.langchain.com/docs/tutorials/',
'https://python.langchain.com/docs/introduction/',
'https://docs.smith.langchain.com/']

def fetch_contents(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f'Fetched {len(soup.text)} characters from {url}')


threads = []

for url in urls:
    thread = threading.Thread(target=fetch_contents, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All web pages fetched")
