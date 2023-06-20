import requests
from discord_webhook import DiscordWebhook
from bs4 import BeautifulSoup
import smtplib
id = os.environ['APP_USERNAME']
password = os.environ['APP_PASSWORD']

def sendToDiscord(toSend):
    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1116620119645360209/Gs3Xj7EhFfl4_NNAR0VQsiKkhT8SGjVwGhY55G4_G1ctba-keATUorwaP3OADM7BwL3W', content=toSend)
    webhook.execute()

page = requests.get('https://www.tuiost.edu.np/result')
soup = BeautifulSoup(page.text, 'html.parser')
body=soup.find(id='notices')
lists=body.find_all('div', class_='mt-3')
allLists=""
for c in lists[:5]:
    allLists+=c.get_text().strip().replace("\n"," ")+"\n"
    if  'csit' in c.get_text().lower() and 'result' in c.get_text().lower() and 'vii' in c.get_text().lower():
        link =c.find('a')
        final_link=link.get("href")
        sendToDiscord("@everyone "+c.text+"\n"+final_link)
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(id, password)
        message=c.text+"\n"+final_link
        s.sendmail("Result alert", id, message)
        s.quit()
sendToDiscord(allLists)



