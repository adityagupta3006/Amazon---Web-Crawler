# Library calls.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup
import urllib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from urllib2 import Request, urlopen, URLError

url = raw_input("Paste the link here: ")
dprice = raw_input("Enter the desired price here: ")
req = Request(url)
try:
    response = urlopen(req)
except URLError, e:
    if hasattr(e, 'reason'):
        print 'Invalid link, please enter the correct link.'
        print 'Reason: ', e.reason
    elif hasattr(e, 'code'):
        print 'The server couldn\'t fulfill the request.'
        print 'Error code: ', e.code
else:
    driver = webdriver.Chrome("C:/Users/agupta/Downloads/chromedriver.exe")
    driver.get(url)
    price = driver.find_element_by_id('priceblock_ourprice').text.replace("$","")
    print price

# for mailing
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os

gmail_user = ""
gmail_pwd = ""

def mail(to, subject, text):
   msg = MIMEMultipart()

   msg['From'] = gmail_user
   msg['To'] = to
   msg['Subject'] = subject

   msg.attach(MIMEText(text))

   part = MIMEBase('application', 'octet-stream')
   #part.set_payload(open(attach, 'rb').read())
   Encoders.encode_base64(part)
   #part.add_header('Content-Disposition','attachment; filename="%s"' % os.path.basename(attach))
   #msg.attach(part)

   mailServer = smtplib.SMTP("smtp.gmail.com", 587)
   mailServer.ehlo()
   mailServer.starttls()
   mailServer.ehlo()
   mailServer.login(gmail_user, gmail_pwd)
   mailServer.sendmail(gmail_user, to, msg.as_string())
   # Should be mailServer.quit(), but that crashes...
   mailServer.close()
 
content = "The item "+ subject +" current price is "

if dprice<price:
    mail("", "Price changes observed", content)
    driver.find_element_by_xpath("//input[@value='']").click();
    driver.find_element_by_xpath("//input[@value='']").click();
    sleep(1.0)
    break