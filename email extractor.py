import requests
from bs4 import BeautifulSoup
import re

def extract_emails(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'html.parser')
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, soup.get_text())
    return emails

# Iterate over your list of links
link_list=["http://mailchi.mp/4bd5002a15e1/february2018", "http://mailchi.mp/comnetwork/16may2018","https://admissions.ptu.ac.in/"]
for link in link_list:
    emails = extract_emails(link)
    print(emails)






