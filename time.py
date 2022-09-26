from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = r"C:\Users\Vimal\Desktop\Python\Applications\chromedriver.exe"
game_url = "http://orteil.dashnet.org/experiments/cookie/"

ser = Service(chrome_driver_path)
driver = webdriver.Chrome(service=ser)
driver.get(game_url)

#get cookie to click on

cookie = driver.find_element(by=By.ID, value="cookie")

#get upgrade items ids

items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5   # 5 seconds
five_min = time.time() + (60*3) #5 minutes

while True:
    cookie.click()

    #every 5 seconds
    if time.time() > timeout:

        #get all upgrade b tags
        all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
        item_prices=[]
        #convert b text in integer price
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost_item = int(element_text.split("-")[1].replace(",", ""))
                item_prices.append(cost_item)

        #create dictonary items for store id and prices

        cookie_upgrade = {}
        for n in range (len(item_prices)):
            cookie_upgrade[item_prices[n]] : item_ids[n]

        #get current cookie count
        money_element = driver.find_element(by=By.ID, value="money").text
        if "," in money_element:
            money_element = money_element.replace("," "")
        cookie_count = int(money_element)

        #find upgrade that we can currently afford
        affordable_upgrades = {}
        for cost, id_item in cookie_upgrade.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id_item

        #purchase the most expensive affortable items
        highest_price_affordable_upgrade = max(affordable_upgrades.items(),key = lambda x:x[0])
        print(highest_price_affordable_upgrade)

        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(by=By.ID, value=f"{to_purchase_id}").click()

        #add another 5 seconds
        timeout = time.time() + 5

    #after 5 minute stop the bot and check cookie per seconds
    if time.time() > five_min:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break
