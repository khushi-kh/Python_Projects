import time

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

CHROME_OPTIONS = webdriver.ChromeOptions()
CHROME_OPTIONS.add_experimental_option("detach", True)

FORM_URL = "https://forms.gle/79V6M7Xo3uaAMUiK6"

ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"


response = requests.get(ZILLOW_URL)
content = response.text

soup = BeautifulSoup(content, "html.parser")
# print(soup.prettify())

all_link_elements = soup.select(".StyledPropertyCardDataWrapper a")

links = [link.get("href") for link in all_link_elements]

all_price_elements = soup.select(".PropertyCardWrapper span")

prices = [price.text.split("+")[0].replace("/mo", "") for price in all_price_elements]

all_addr_elements = soup.select(".StyledPropertyCardDataWrapper address")

addresses = [address.text.strip().replace("|", "") for address in all_addr_elements]

# filling google form
driver = webdriver.Chrome(CHROME_OPTIONS)
driver.get(FORM_URL)
time.sleep(2)

for address, price, link in zip(addresses, prices, links):
    address_element = driver.find_element(By.XPATH,
                                          value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')

    price_element = driver.find_element(By.XPATH,
                                        value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')

    link_element = driver.find_element(By.XPATH,
                                       value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    address_element.send_keys(address)

    price_element.send_keys(price)

    link_element.send_keys(link)

    submit = driver.find_element(By.XPATH,
                                 value='/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()

    time.sleep(2)
    another_response = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_response.click()
    time.sleep(2)

