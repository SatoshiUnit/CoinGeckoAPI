#!/usr/bin/env python
# coding: utf-8

# In[ ]:


The following demonstrates how to create 


# In[1]:


pip install -U pycoingecko


# In[2]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from pycoingecko import CoinGeckoAPI


# In[3]:


cg = CoinGeckoAPI()

cg.ping()


# In[4]:


cg.get_price(ids=['bitcoin', 'litecoin', 'ethereum'], vs_currencies='usd')


# In[8]:


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

    # Close the browser
    driver.quit()


# In[9]:


change_currency('bitcoin')

