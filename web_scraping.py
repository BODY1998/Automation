from bs4 import BeautifulSoup #web scraping
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests #http requests
import smtplib #send mail
import datetime

now = datetime.datetime.now()
