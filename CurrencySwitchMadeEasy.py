
pip install -U pycoingecko

from selenium import webdriver
from selenium.webdriver.common.by import By
from pycoingecko import CoinGeckoAPI


cg = CoinGeckoAPI()

cg.ping()


cg.get_price(ids=['bitcoin', 'litecoin', 'ethereum'], vs_currencies='usd')



def change_currency():
    
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

    
    driver.get('https://www.coingecko.com/')

    
    button = driver.find_element(By.CSS_SELECTOR, '[data-action="click->analytics-tracker#trackEventFromTempProperties click->settings#changeCurrency"]')
    
    
    current_currency = button.get_attribute('data-iso-code')
    
    if current_currency == 'aud':
        
        button.set_attribute('data-analytics-event-properties', '{"target_currency":"usd"}')
        button.set_attribute('data-iso-code', 'usd')
    else:
       
        button.set_attribute('data-analytics-event-properties', '{"target_currency":"aud"}')
        button.set_attribute('data-iso-code', 'aud')
    
   
    button.click()


change_currency('bitcoin')

