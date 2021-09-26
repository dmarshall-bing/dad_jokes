# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 18:36:14 2019

@author: entir
"""

#%%
#import requests

#headers={'User-Agent':'entirity','Accept':'application/json'}

#joke=requests.get("https://icanhazdadjoke.com/",headers=headers)

#print(joke.content)

#print(joke.content.decode('utf-8'))
#%% runs the program and sends joke every day at noon

#%% Retrieve joke from API

def joke_retrieve():
    
    import requests
    
    headers={'User-Agent':'entirity','Accept':'text/plain'}

    joke=requests.get("https://icanhazdadjoke.com/",headers=headers)

    return joke.content.decode('utf-8')

    print(joke.content.decode('utf-8'))

#%% Package joke and send it as a text to email
    
def joke_send(joke):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    
    email=""
    pas=""
    
    smtp='smtp.gmail.com'
    port=587
    server=smtplib.SMTP(smtp,port)
    server.starttls()
    server.login(email,pas)
    
    sms_gateway=[]
    for recipient in sms_gateway:
    
        msg=MIMEMultipart()
        msg['From']=email
        msg['To']=recipient
        
        from datetime import date
        
        msg['Subject']="Dannymarsh's Dad Joke emporium. Date:"+str(date.today())
        body=joke
    
    
        msg.attach(MIMEText(body, 'plain'))
        sms=msg.as_string()

        server.sendmail(email,recipient,sms)
    
    server.quit()
    
#%%
# joke_send(joke_retrieve())

while True:
    from datetime import datetime
    t=datetime.now()
    print("running...time is "+str(datetime.now()))
    import time
    if t.hour==12:
        joke_send(joke_retrieve())
        print("joke sent")
        time.sleep(3600)
    else:
        time.sleep(3600)
      
#%%
