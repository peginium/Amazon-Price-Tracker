import requests
from bs4 import BeautifulSoup
import smtplib
import time

link = 'Amazon_item_link' #Amazon Link
headers = {"Your_User_Agent"} #Your User Agent

page = requests.get(link, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
def get_price():
    title = soup.find(id="productTitle").getText()
    price = soup.find(id="priceblock_ourprice").getText()
    price2 = float(price[1:6])

    if (price2 < Your_Price):  #Write your price if its more cheaper than your price its sends email
        send_mail()

    print(price2)
    print(title.strip())

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('sender-gmail-adress', 'sender-email-password')

    subject = 'XXXXXX' #Title
    body = 'XXXXXX' #Body
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'Sender-gmail-adress',
        'Reciever-gmail-adress',
        msg
    )
    server.quit()

while(True):
    get_price()
    time.sleep(3600)