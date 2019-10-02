print("Importing Libraries..")
from lxml import html
import requests
import datetime
print("Libraries Imported..")
print("Getting the page..")
page = requests.get('https://www.whatmobile.com.pk/Oppo_F11-Pro')
print("Converting")
tree = html.fromstring(page.content)
print("Finding Price..")
price = tree.xpath('//*[@id="centerContainer"]/div/div[2]/div/div[2]/span[2]/text()[1]')
                    # //*[@id="centerContainer"]/div/div[2]/div/div[5]/table[2]/tbody/tr[1]/td/strong[1]
					# //*[@id="centerContainer"]/div/div[2]/div/div[2]/span[2]/text()[1]
					# //*[@id="centerContainer"]/div/div[2]/div/div[2]/span[2]/text()[1]
					
price = str(price)
price = price.strip("['\n    ")
price = price.rstrip(' ]\'')
price = price.lstrip(" ''\\'n'    Rs. ")
price = price.replace(',','')
print(price)

if price < "50000":
	print("You are good to go")
else:
	print("You are NOT good to go")

date = datetime.datetime.now()

datentime = date.strftime("%d") +"-"+ date.strftime("%B") +"-"+ date.strftime("%Y") +" "+ date.strftime("%X")



print("Writing to file..")
with open("Oppo F11 Pro.txt","a+") as f:
	data = "Current price of Oppo F11 Pro is Rs. " + price + " at " + str(datentime) + "\n"
	f.write(data)

