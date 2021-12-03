from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import numpy as np


GG = webdriver.Chrome()
GG.minimize_window()

################# BTC/EUR ####################

GG.get("https://www.google.com/search?q=btc%2Feur&oq=btc%2Feur&aqs=chrome.0.69i59j0i512l5j69i58j69i61.3397j1j7&sourceid=chrome&ie=UTF-8")

BTCEURcookies = WebDriverWait(GG, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="L2AGLb"]'))
)
BTCEURcookies.click()
time.sleep(1)
BTCEUR_price = GG.find_element_by_xpath('//*[@id="crypto-updatable_29"]/div/div[2]/span[1]').text
BTCEUR_price_fl = BTCEUR_price.replace('.','').replace(',','.')

##################### EUROSTOXX SELECT DIVIDEND 30 ##############################

GG.get("https://www.borsaitaliana.it/borsa/etf/scheda/IE00B0M62S72.html?lang=it")
EUROSTOXXSELECTDIVIDEND30price = GG.find_element_by_xpath('//*[@id="fullcontainer"]/main/section/div[4]/div[1]/article/div/div/div[2]/div/span[1]/strong').text
EUROSTOXXSELECTDIVIDEND30price_fl = EUROSTOXXSELECTDIVIDEND30price.replace(',','.')

######################## VANECK ESPORT ETF ######################################

GG.get("https://www.borsaitaliana.it/borsa/etf/scheda/IE00BYWQWR46.html?lang=it")
ESPOprice = GG.find_element_by_xpath('//*[@id="fullcontainer"]/main/section/div[4]/div[1]/article/div/div/div[2]/div/span[1]/strong').text
ESPOprice_fl = ESPOprice.replace(',','.')

################# AcomeA Eurobbligazionario #####################################

#GG.get("https://www.borsaitaliana.it/borsa/fondi/dettaglio/1FADB106004.html?lang=it")
GG.get("https://www.morningstar.it/it/funds/snapshot/snapshot.aspx?id=F00000MJ5X")
ACOMEAEUROBBprice = GG.find_element_by_xpath('//*[@id="overviewQuickstatsDiv"]/table/tbody/tr[2]/td[3]').text
ACOMEAEUROBBprice_onlynumber = ACOMEAEUROBBprice[4:]
ACOMEAEUROBBprice_fl = ACOMEAEUROBBprice_onlynumber.replace(',','.')
#TRIM THE FIRST 4 CHARACTERS

################# S&P500 iShares (acc) #############################################

GG.get("https://www.borsaitaliana.it/borsa/etf/scheda/IE00B5BMR087.html?lang=en")
STANDARD_AND_POORS_ACC_price = GG.find_element_by_xpath('//*[@id="fullcontainer"]/main/section/div[3]/div[1]/article/div/div/div[2]/div/span[1]/strong').text
STANDARD_AND_POORS_ACC_price_fl = STANDARD_AND_POORS_ACC_price.replace(',','.')

################## DATAFRAME #################

asset = ['BTC/EUR', 'Eurostoxx select dividend 30', 'ESPO', 'AcomeA Eurobbligazionario', 'S&P500 (acc)']
prezzo = np.array([BTCEUR_price_fl, EUROSTOXXSELECTDIVIDEND30price_fl, ESPOprice_fl, ACOMEAEUROBBprice_fl, STANDARD_AND_POORS_ACC_price_fl]).astype(np.float64)
quantità = np.array([0.00585535, 48, 28, 10.161, 1], dtype=np.float64)
investimento = np.array([296.4, 1002.24, 986.16, 225, 390.47], dtype=np.float64)
profit_loss_perc = ((quantità*prezzo-investimento)/investimento)*100
profit_loss_abs = (quantità*prezzo-investimento)
indici = [" ", " ", " ", " "," "]

pd.set_option("display.precision", 8)
df = pd.DataFrame({'asset': asset, 'prezzo': prezzo, 'quantità': quantità, 'investimento': investimento, 'p/l (%)': profit_loss_perc, 'p/l (€)': profit_loss_abs}, indici)

Total = df['p/l (€)'].sum()
df.at['Total','p/l (€)'] = df['p/l (€)'].sum()
df.replace(np.NaN, "")

def profit_loss(val): 
   color = 'red' if val < 0 else 'green' 
   return 'color: %s' % color

df.style.applymap(profit_loss).format({'p/l (€)':'${0:,.2f}'})

print(df)





