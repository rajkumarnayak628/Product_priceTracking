# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 11:51:36 2020

@author: user
"""

import requests
import bs4
from bs4 import BeautifulSoup
import smtplib




def check_price():

    URL= 'https://www.amazon.in/DEVICE-URBAN-INFOTECH-Professional-Broadcasting/dp/B08DRMQ4W2/ref=sr_1_52?dchild=1&keywords=singing+mic&qid=1607505823&sr=8-52'

    header={'user-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}

    page= requests.get(URL,headers=header)
 
    soup= BeautifulSoup(page.content, 'html.parser')

    title= soup.find(id="productTitle").get_text()
    print(title.strip())

    price=soup.find(id="priceblock_ourprice").get_text()
    converted_price=float(price[2]+price[4:7])
    print(converted_price)
    
    if (converted_price<2200):
        send_mail()


def send_mail():
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('rajkumarnayak628@gmail.com','kearlgmaskuiwdfk')
    subject="Yo boi Price fell down" 
    body="Check this fuckin link and order it now you lazy ass    https://www.amazon.in/DEVICE-URBAN-INFOTECH-Professional-Broadcasting/dp/B08DRMQ4W2/ref=sr_1_52?dchild=1&keywords=singing+mic&qid=1607505823&sr=8-52"
    
    msg= f"Subject: {subject}\n\n\n{body}"
    
    server.sendmail( 
        'rajkumarnayak628@gmail.com',
        'rajkumarnayak.dce.628@gmail.com',
        msg)
    print('Hey Its done bro')
    


check_price()