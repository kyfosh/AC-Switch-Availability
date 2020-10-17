import requests
import time
import datetime
import math
import random
from playsound import playsound
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0"}
r = requests.get('https://www.bestbuy.com/site/nintendo-switch-animal-crossing-new-horizons-edition-32gb-console-multi/6401728.p?skuId=6401728', headers=headers)


soup = BeautifulSoup(r.content, features="html.parser")
line = str(soup.find_all("div", "fulfillment-add-to-cart-button")[0])

if(line.find("Add to Cart")):
    print("AVAILABLE")
    playsound('me-too.mp3')
elif(line.find("Coming Soon") or line.find("Sold Out")):
    while(True):
        r = requests.get('https://www.bestbuy.com/site/nintendo-switch-animal-crossing-new-horizons-edition-32gb-console-multi/6401728.p?skuId=6401728', headers=headers)
        line = str(soup.find_all("div", "fulfillment-add-to-cart-button")[0])
        if(line.find("Add to Cart")):
            print("AVAILABLE")
            playsound('me-too.mp3')'''change to noise you want to use to be alerted when its in stock'''
            break
        else:
            temp_stop = random.randint(600, 1800) '''change number values for longer/shorter random time for sleep'''
            print("SLEEPING FOR: " + str(math.floor(temp_stop/60.0)) + "mins " + str(temp_stop%60) + " seconds, cur time: ")
            print(datetime.datetime.now())
            time.sleep(temp_stop)
    


