from bs4 import BeautifulSoup
from urllib.request import urlopen

def puslapis(addrLink):
	html 	= urlopen(addrLink)
	bsObj 	= BeautifulSoup(html.read(),"lxml")
	for skelbimas in bsObj.find_all('div',{"class":"desc_m_a_b"}):
		link 		= skelbimas.find('a',href=True)
		#print ("nuoroda:\t",link["href"],"\n")
		adresas 	= link.text.strip()
		try:
			miestas	= adresas.split()[3][:-1]
		except:
			miestas	= "nera"
		try:
			rajonas	= adresas.split()[4]
		except:
			rajonas	= "nera"
		if rajonas.endswith(','):
			rajonas	= rajonas[:-1]
			gatve	= str(adresas.split()[5:-1]).strip("[']")
			gatve	= gatve.replace(',','')
			gatve	= gatve.replace("'","")
		else:
			gatve	= "nera"

		price 		= skelbimas.find("span",{"class":"main_price"})
		delploto 	= skelbimas.find("div", {"class":"description"}).text
		try:
			plotas	= int(delploto.split()[10])
		except:
			plotas 	= "nera"

		data 		= skelbimas.find("time")
		print (miestas,"\t",rajonas,"\t",gatve,"\t",price.text.strip(),"\t",plotas,"\t",str(data["datetime"])[:-15],"\t",str(link["href"])[-15:-5],"\t",link["href"])
		#print ("adresas:\t",adresas,"\n") out
		#print ("miestas:\t",miestas,"\n")
		#print ("rajonas:\t",rajonas,"\n")
		#print ("gatve:\t\t",gatve,"\n")
		#print ("kaina:\t\t",price.text.strip(),"\n")
		#print ("plotas:\t\t",plotas,"m2\n")
		#print ("ikelimo data:\t",str(data["datetime"])[:-15],"\n")
		#print ("UID:\t\t",str(link["href"])[-15:-5],"\n")
		#print ("-"*200)

	try:
		nextPg	= bsObj.find("a",{"rel":"next"})
		nextPg	= nextPg["href"]
	except TypeError:
		nextPg	= "paskutinis"
	return nextPg

pradzia = "http://www.alio.lt/nekilnojamas-turtas/butai/nuomoja.html"
while pradzia != "paskutinis":
	#print (pradzia)
	pradzia = puslapis(pradzia)
