import requests
from bs4 import BeautifulSoup
import smtplib

url = 'https://rb.gy/3bnrug'

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

    server.login('email', 'password')

    subject = 'Amazing !'
    body = f'''Hey, I just want to take a moment of yours to remind you.
            Last chance to grab this amazing product with discounted price 
            {url}'''

    msg = f"Subject: {subject}\n\n {body}"

    sender = 'email'
    recipients = ['email/s']

    server.sendmail(
        sender,
        recipients,
        msg
    )

    print('Successfully sent email')
    server.quit()


tracking_iphone()
