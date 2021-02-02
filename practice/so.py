import requests
from bs4 import BeautifulSoup

#&pg=2
URL = "https://stackoverflow.com/jobs?q=python"

def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")

def get_jobs():
    last_page = get_last_page()
    return []