from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def translate(text):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-logging') 
    options.add_argument('--log-level=3')  
    driver = webdriver.Chrome(options=options) 
    driver.get("https://translate.google.com/?hl=ru&sl=en&tl=ru")
    sleep(4)
    textarea = driver.find_element('xpath', '//textarea')
    textarea.send_keys(text)
    sleep(3)
    translation = driver.find_element('xpath', '//div[@class="lRu31"]')
    return translation.text