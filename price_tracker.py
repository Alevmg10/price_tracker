import requests
from bs4 import BeautifulSoup
import smtplib
import time


URL = "https://www.overstock.com/Home-Garden/T-Shaped-Gaming-Desk-Computer-Office-Desk-with-Cup-Holder-and-Headphone-Hook/33095190/product.html?guid=627f96c4-9d49-4fc5-b7f0-8c15ae6514fa&kwds=&osp=true&refccid=QLUWWRJ7MGKZIDCN5DQSIXDZOA&rfmt=desk%20type%3AGaming%20Desks&searchidx=3"

headers = {
    "User-Agent": 'Mozilla...'
}  # search in google for "my user agent"


def check_item_price():

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    title = soup.find(class_="_3Bj68d3").get_text(strip=True)
    price = soup.find(id="product-price-price-container").get_text(strip=True)
    price_converted = float(price[1:6])

    if (price_converted < 135):
        send_email()

    print(title)
    print(price_converted)


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()  # encrypt our connection
    server.ehlo()

    # here put the email and the password that you will use
    server.login('example@mail.com', 'password')

    subject = 'Price is now low'

    msg = f"Subject: {subject}\n\n{URL}"

    server.sendmail(
        'example@mail.com',  # from email
        'example@mail.com',  # to email
        msg
    )
    print('The email has been sent')

    server.quit()


while True:
    check_item_price()
    time.sleep(3600)  # will check every hour
