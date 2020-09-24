import requests
from bs4 import BeautifulSoup
import smtplib

url = 'https://www.amazon.de/Neu-Apple-iPhone-SE-64-GB/dp/B0875Q8CD9/ref=sr_1_1_sspa?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=iphone+se&qid=1600896020&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFMSDY0RFRWUDNUTjQmZW5jcnlwdGVkSWQ9QTAxNDQyMDA4SFFWMUgxREwwUlYmZW5jcnlwdGVkQWRJZD1BMTAwNDU1MzNLVEEwT0hYU1dHSEkmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}


def tracking_iphone():

    page = requests.get(url, headers=headers)
    print(page.status_code)

    soup = BeautifulSoup(page.content, 'html.parser')

    # print(soup.prettify())

    productName = soup.find(id='productTitle').get_text()
    productPrice = soup.find(id='priceblock_ourprice').get_text()

    numProductPrice = float(productPrice[0:3])

    if(numProductPrice > 400):
        send_email()

    print(productName.strip())
    print(numProductPrice)


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('email goes here', 'password will be here)

    subject = 'Product price has not been decreased :(!'
    body = 'Check the amazon link https://www.amazon.de/Neu-Apple-iPhone-SE-64-GB/dp/B0875Q8CD9/ref=sr_1_1_sspa?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=iphone+se&qid=1600896020&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFMSDY0RFRWUDNUTjQmZW5jcnlwdGVkSWQ9QTAxNDQyMDA4SFFWMUgxREwwUlYmZW5jcnlwdGVkQWRJZD1BMTAwNDU1MzNLVEEwT0hYU1dHSEkmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl'

    msg = f"Subject: {subject}\n\n {body}"

    sender = 'email'
    recipients = ['email/s']

    server.sendmail(
        sender,
        recipients,
        msg
    )

    print('Successfull sent email')
    server.quit()


tracking_iphone()
