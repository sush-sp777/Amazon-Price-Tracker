from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv


load_dotenv()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

# my_email="sushantsp433@gmail.com"
# password="vidy oigs gdnm xpus"
smtp_address = os.getenv("smtp_addrs")
email_address= os.getenv("Your_email_Address")
email_password = os.getenv("pass")

response=requests.get("https://appbrewery.github.io/instant_pot/")
actual_page=response.text
soup=BeautifulSoup(actual_page,"html.parser")
price=soup.find(name="span",class_="a-offscreen")
actual_price=float(price.getText().split("$")[1])

response1=requests.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1",headers=headers)
page=response1.text
soup1=BeautifulSoup(page,"html.parser")
L_price=soup1.find(name="span",class_="a-offscreen")
live_price=float(L_price.getText().split("$")[1])

if actual_price>live_price:
     with smtplib.SMTP(os.environ["smtp_address"],port=587) as connection:  #smtp object is created
        connection.starttls()   #securing your email connection (makes connection secure) tls=transfer layer protocol
        result=connection.login(os.environ["email_address"],os.environ["email_password"])
        connection.sendmail(
             from_addr=os.environ["email_address"],
             to_addrs=os.environ["itsadi369@gmail.com"],
             msg=f"Subject: Amazon Price Alert!\n\nInstant Pot Duo Plus 9-in-1 Electric Pressure Cooker, Slow Cooker is now ${live_price} shop now".encode("utf-8")

        )
