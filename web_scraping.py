from bs4 import BeautifulSoup  # web scraping
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests  # http requests
import smtplib  # send mail
import datetime

now = datetime.datetime.now()
content = ''  # email content placeholder


def extract_news(url):
    print('Extracting somethings ...')
    cnt = ''
    cnt += ('Top News:\n'+'_'*50+'\n')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    for i, tag in enumerate(soup.find_all('td', attrs={'class': 'title', 'valign': ''})):
        cnt += ((str(i+1)+' >> '+tag.text+'\n')
                if tag.text != 'More' else '')
    return (cnt)


print(extract_news('https://news.ycombinator.com/'))
