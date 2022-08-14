"""Amazon price updater. Couldn't get get_text() to work."""


from bs4 import BeautifulSoup
import smtplib
import requests
import time

URL = "https://www.amazon.com/eufy-BoostIQ-Super-Thin-Self-Charging-Medium-Pile/dp/B079QYYGF1/ref=sr_1_1?crid=I7X29WPFVVAF&keywords=automatic+vacuum&qid=1659889467&sprefix=automatic+vacuum%2Caps%2C94&sr=8-1"

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:5])

    if(converted_price < 100):
        send_mail()
    
    print(converted_price)
    print(title.strip())

    if(converted_price > 100):
        send_mail()


def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("mxgoetz03@gmail.com", 'Lillie_3274')

    subject = "Price fell down!"
    body = "Check the amazon link https://www.amazon.com/eufy-BoostIQ-Super-Thin-Self-Charging-Medium-Pile/dp/B079QYYGF1/ref=sr_1_1?crid=I7X29WPFVVAF&keywords=automatic+vacuum&qid=1659889467&sprefix=automatic+vacuum%2Caps%2C94&sr=8-1"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail("mxgoetz03@gmail.com", 'mxgoetz03@gmail.com', msg)

    print("Email has been sent.")

    server.quit()


while(True):
    check_price()
    time.sleep(86400)