import requests
from bs4 import BeautifulSoup
from gtts import  gTTS
import  playsound
from art import *

def headline(title):
    print(text2art(title))


def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def url_maker(item, search_type):
    key = 12
    if search_type == 1:
        key = 12
    elif search_type == 2:
        key = 1
    elif search_type == 3:
        key = 10
    elif search_type == 4:
        key = 15
    elif search_type == 5:
        key = 7
    else:
        print('Number out of scope')
        
    
    url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=' + item + '&_sacat=0&LH_TitleDesc=0&_ipg=200&_sop=' + str(key)
    return url


def find_prices(fill, url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    for test in soup.find_all('span'):
        if test.get('class'):
            if test.get('class')[0] == 's-item__price':
                fill.append(test.get_text())

def maxamize_listings(fill, max_price, final):
    for i in range(len(fill)):
        if float(fill[i]) <= float(max_price):
            final.append(float(fill[i]))

if __name__ == "__main__":
    headline('Ebay Hunter')
    speak('Welcome to the money saver')
    speak('Enter the item your searching for')
    item = input('Enter the item your searching for:')
    search_type = int(input('Enter 1 for best match, 2 Time ending soonest, 3 time newly listed, 4 for price + shipping lowest first, 5 Distance nearest first: '))
    url = url_maker(item, search_type)


    fill = []
    find_prices(fill, url)
    max_price = int(input('Enter the max price your willing to pay'))
    final = []
    
    for i in range(len(fill)):
        fill[i] = fill[i][1:]
    
    maxamize_listings(fill, max_price, final)
    print(f'Min price found under asking was: {min(final)}')
    print("==================================================")
    print("All values under price")
    print(final)
    
    
    