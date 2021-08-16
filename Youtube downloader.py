from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import youtube_dl

print('Canzone?')
song=input()

browser = webdriver.Edge(executable_path= "msedgedriver.exe")

browser.get("https://www.youtube.com/")
#accetta
accetta1 = ActionChains(browser)
accetta1.send_keys(Keys.TAB*4).send_keys(Keys.ENTER).perform()
##accetta2
#accetta2 = ActionChains(browser)
#accetta2.send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()

#ricerca
searchbox = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, "search"))
)

clicca_barra = ActionChains(browser) 
clicca_barra.click(searchbox).send_keys(song).send_keys(Keys.ENTER).perform()

time.sleep(2)
video = ActionChains(browser)
video.send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()

#DOWNLOADER
ydl_opts = {
    'outtmpl': 'C:\\Users\\leoac\\OneDrive\\Desktop\\Coding\\Python apps\\Youtube downloader\\Canzoni\\%(title)s.%(ext)s',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}

def dwl_vid():
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([zxt])

another_one = 'y'
while (another_one == 'y'):
    link = browser.current_url
    zxt = link.strip()

    dwl_vid()
    print('another one? (y=yes other=no)')
    another_one = input()