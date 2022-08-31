import requests
from bs4 import BeautifulSoup
from datetime import datetime  
from datetime import timedelta 
import nepali_datetime
from userge import userge, Message


@userge.on_cmd("xutti", about={
    'header': "Tell if tomorrow is holiday in nepal or not"
    'usage': "!xutti"})
async def xutti(message:Message):
               todayDate = []
               activeDate = 0
               holiday = []
               dayOf = []
               engDay = []
               URL = f"https://www.hamropatro.com/widgets/calender-medium.php"
               page = requests.get(URL)
               soup = BeautifulSoup(page.content, "html.parser")
               date = soup.find("ul", class_= "dates")
               for current in date:
                   todayDate.append(date.find("li", class_="active"))
               activeDate = todayDate[0].find("span", class_="eng").text.strip()

               for ho in date:
                    holiday.append(date.find_all("li", class_="holiday"))
               holiDate = holiday[0]
               for d in holiDate:
                       ok = d.find("span", class_="nep").text
                       no = d.find("span", class_="eng").text
                       engDay.append({"eng": no, "nep": ok})
               for a in engDay:
                    if(activeDate < a["eng"]):
                      dayOf.append(a["nep"])
               xutti = dayOf[0]
               urldate='{d.year}-{d.month}-{d.day}'.format(d=nepali_datetime.datetime.now()+ timedelta(days=int(1)))
               nepdate=(nepali_datetime.datetime.now() + timedelta(days=int(1))).strftime("%D %N %K, %G")
               rws=requests.get('https://www.hamropatro.com/date/'+urldate).text
               rawtit=rws[rws.find('<title>') + 7 : rws.find('</title>')]
               titis=rawtit.split(' | ')[0]+' | '+rawtit.split(' | ')[1]
               if(nepdate.split(" ")[0] == xutti):
                  await message.edit(f"Aww bholi xutti ho. {titis} haru xa bholi aba aafai jana baki")
               elif (nepdate.split(" ")[3] == "शनिबार"):
                  await message.edit("saturday ko xutti ho bholi enjoy gara")
               else:
                  await message.edit(f"k ko xutti huni hora. haina school jau khuru khuru. {xutti} gatey xa bida aba sed sanibar bayek")
