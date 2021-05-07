import requests
from bs4 import BeautifulSoup
import time, os, datetime
import json


# Subasheta
page = requests.get("https://www.prajavani.net")
soup = BeautifulSoup(page.content,'html.parser')

x = soup.find_all('div', class_ = 'heading-center')

if (len(x) == 0):
	print ("Not Present")
	subasheta = "ಇಡೀ ಪತ್ರಿಕೆ ಹುಡುಕಿದೆ ಆದರೆ ಸುಭಾಷಿತ ಕಂಡುಬಂದಿಲ್ಲ, ಕ್ಷಮಿಸಿ."
else:
	y = soup.find_all('div', style = 'font-size:14px !important;')
	z = soup.find_all('span', class_='pj-header__source')
	subasheta = str(datetime.datetime.now())+"%0A%0A"+x[0].get_text()+".%0A%0A%09"+y[0].get_text() + ".%0A%0A" +z[0].get_text()

ur = 'https://chandrashekarcn.000webhostapp.com/telegram/updatepost.php'
mydata = {'subasheta':subasheta}
rr = requests.post(ur,data=mydata)
print("subasheta")

# Horoscope
page = requests.get("https://www.prajavani.net/amp/daily-horoscope.html")
soup = BeautifulSoup(page.content,'html.parser')

x = soup.find_all('div', class_= 'field-label')
y = soup.find_all('div', class_= 'field-items')
z = soup.find_all('h1')
z = z[0].text.split(":")
z = z[1]

horoscope =  str(datetime.datetime.now()) + "%0A%0A" + z + "%0A%0A"
for i in range(len(x)):
        horoscope = horoscope + x[i].get_text() + "%0A" + y[i].get_text() + "%0A%0A"

ur = 'https://chandrashekarcn.000webhostapp.com/telegram/updatepost.php'
mydata = {'horoscope':horoscope}
rr = requests.post(ur,data=mydata)
print("Horoscope")

# Panchanga
x = datetime.datetime.now()
xx = x.strftime("%Y") + "-" + x.strftime("%m") + "-" + x.strftime("%d")

page = requests.get("https://kannada.panchangam.org/dailypanchangam.php?date="+xx)
soup = BeautifulSoup(page.content,'html.parser')

x = soup.find_all('td')

pan = {
	"cn":"cnc",
	"Sunrise & Sunset":"ಸೂರ್ಯೋದಯ ಮತ್ತು ಸೂರ್ಯಾಸ್ತ",
	"Month & Paksham":"ತಿಂಗಳು ಮತ್ತು ಪಕ್ಷ",
	"Tithi*":"ತಿಥಿ",
	"Nakshatram*":"ನಕ್ಷತ್ರ",
	"Yogam*":"ಯೋಗ",
	"Karanam*":"ಕರಣ",
	"Rahukalam*":"ರಾಹುಕಾಲ",
	"Yamagandam*":"ಯಮಗಂಡ ಕಾಲ",
	"Varjyam*":"ವರ್ಜಯಂ",
	"Gulika*":"ಗುಳಿಕಕಾಲ",
	"Amritakalam*":"ಅಮೃತಕಾಲ",
	"Abhijit Muhurtham*":"ಅಭಿಜಿತ್ ಮುಹೂರ್ತ"
}

p = "[ " + x[0].text + " ]%0A"
p = p + "[ " + pan[x[3].text] + " ]%0A[ " + x[4].text + " ]%0A" #sunrice and sunset
p = p + "[ " + pan[x[5].text] + " ] [ " + x[6].text + " ]%0A" #month and paksham
p = p + "[ " + pan[x[8].text] + " ] [ " + x[9].text + " ]%0A" #tithi
p = p + "[ " + pan[x[10].text] + " ] [ " + x[11].text + " ]%0A" #nakshatrm
p = p + "[ " + pan[x[12].text] + " ] [ " + x[13].text + " ]%0A" #yogam
p = p + "[ " + pan[x[14].text] + " ] [ " + x[15].text + " ]%0A" #karanam
p = p + "[ ಕೆಟ್ಟಕಾಲ / Bad Time ]%0A"
p = p + "[ " + pan[x[17].text] + " ] [ " + x[18].text + " ]%0A" #Rahukala
p = p + "[ " + pan[x[19].text] + " ] [ " + x[20].text + " ]%0A" #yamaganda kalm
p = p + "[ " + pan[x[21].text] + " ] [ " + x[22].text + " ]%0A" #varjyam
p = p + "[ " + pan[x[23].text] + " ] [ " + x[24].text + " ]%0A" #gulika
p = p + "[ ಒಳ್ಳೆ ಸಮಯ / Good Time ]%0A"
p = p + "[ " + pan[x[26].text] + " ] [ " + x[27].text + " ]%0A" #amritakala
p = p + "[ " + pan[x[28].text] + " ]%0A[ " + x[29].text + " ]%0A" #abijit
p = p.replace("&","-")

ur = 'https://chandrashekarcn.000webhostapp.com/telegram/updatepost.php'
mydata = {'panchanga':p}
rr = requests.post(ur,data=mydata)
print("panchanga")


# chinakurali
page = requests.get("https://www.prajavani.net/cartoons")
soup = BeautifulSoup(page.content,'html.parser')

x = soup.find_all('a',itemprop = 'url')

page = requests.get("https://www.prajavani.net"+x[0]['href'])
soup = BeautifulSoup(page.content,'html.parser')
y = soup.find_all('script', type = 'application/ld+json')
data = json.loads(y[1].string)

p = data['image']['contentUrl'] + "&caption=" + data['headline']
ur = 'https://chandrashekarcn.000webhostapp.com/telegram/updatepost.php'
mydata = {'chinakurali':p}
rr = requests.post(ur,data=mydata)
print("chinakurali")


# churumuri

page = requests.get("https://www.prajavani.net/churumuri")
soup = BeautifulSoup(page.content,'html.parser')

x = soup.find_all('a', itemprop = 'url')
url = "http://www.prajavani.net" + x[0].get('href')

page1 = requests.get(url)
soup1 = BeautifulSoup(page1.content,'html.parser')

y = soup1.find_all('script', type = 'application/ld+json')
data = json.loads(y[1].string)
soup2 = BeautifulSoup(data['articleBody'],'html.parser')
z = soup2.find_all('p')

p_img = data['image']['contentUrl'] + "&caption=" + data['datePublished'] +"%0A" + data['headline'] + "%0A%0A"
p=""
for i in range(len(z)):
	p = p + z[i].get_text() +"%0A%0A"

p = p + "ಬರೆದವರು," + data['author'] + ".%0A%0A"

ur = 'https://chandrashekarcn.000webhostapp.com/telegram/updatepost.php'
mydata = {'churumuri1':p_img}
rr = requests.post(ur,data=mydata)
mydata = {'churumuri2':p}
rr = requests.post(ur,data=mydata)
print("churumuri")
exit(0)

