import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import email, smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import socket
def execute(x):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options) #create webdriver object
    l1=list(x.split(' '))
    url="https://webapp4.asu.edu/catalog/classlist?t=2227&s=CSE&n=5**&k={0}%20{1}&hon=F&promod=F&c=TEMPE&e=all&ses=C&page=1".format(l1[0],l1[1])
    driver.get(url) #Navigating to the specified URL(Link)
    time.sleep(30) #Putting the thread to sleep for 30 seconds, in order to pause the script.
    driver.fullscreen_window() #Making Browser to be on fullscreen mode
    driver.set_page_load_timeout(20) #set the 20 seconds time to wait for a page load to complete before throwing an error.
    filename = str(x)+'.png'
    driver.save_screenshot( filename )
    #Server code starts
    socket.setdefaulttimeout(340)
    subject = "Seats availability for"+" "+str(x)+" course."
    body = "Please find the below attachment for seats availablity of "+str(x)+" course."
    receiver_email = "nuttaki111@gmail.com"
    sender_email = "seats.notfier@gmail.com"
    password = "frfhonnvlbzumivc"
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails
    # Add body to email
    message.attach(MIMEText(body, "plain"))
    #filename = str(x)+".png"  # In same directory as script
    # Open PNG file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)
    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()
    # Log in to server and send email
    ser=smtplib.SMTP('smtp.gmail.com',587) #Provide the host(smtp.gmail.com, since we are using gmail service) and also port number 587(for tls connection)
    ser.ehlo()
    ser.starttls()
    ser.login("seats.notfier@gmail.com","frfhonnvlbzumivc")
    ser.sendmail("seats.notfier@gmail.com","nuttaki111@gmail.com",text)
    print("Mail sent")
    ser.quit()
    #Server code ends here
    driver.close() #Closing the existing browser tab
    path1="/Users/chennupatiaashvik/Documents/"+str(filename)
    os.remove(path1) #deleting the file from where we stored earlier

SubjectList=["Data Mining", "Data Processing at scale" , "Data Visualization"]
for x in SubjectList:
    execute(x)
