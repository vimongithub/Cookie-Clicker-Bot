from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = r"C:\Users\Vimal\Desktop\Python\Applications\chromedriver.exe"
game_url = "http://orteil.dashnet.org/experiments/cookie/"

ser = Service(chrome_driver_path)
driver = webdriver.Chrome(service=ser)
driver.get(game_url)

def money_box():
    money_element = driver.find_element(by=By.ID, value="money")
    money = (money_element.text)
    return int(money.replace(",", ""))
def buy_cursor():
    cursor = driver.find_element(by=By.ID, value="buyCursor")
    cursor.click()
def buy_grandma():
    grandma = driver.find_element(by=By.ID, value="buyGrandma")
    grandma.click()
def buy_factory():
    factory = driver.find_element(By.ID, value="buyFactory")
    factory.click()
def buy_mine():
    mine = driver.find_element(By.ID, value="BuyMine")
    mine.click()

coockie_click = driver.find_element(by=By.XPATH, value='//*[@id="cookie"]')
timeout= time.time()  + 5
five_minute = time.time() + 120   # 5 minutes from now

def time_out():
    global timeout
    timeout = time.time() +5
while True:
    coockie_click.click()
    if time.time() > timeout:
        if money_box() == 2000:
            buy_mine()
            time_out()
        elif money_box() == 550:
            buy_factory()
            time_out()
        elif money_box() == 100:
            buy_grandma()
            time_out()
        elif money_box() == 15:
            buy_cursor()
            time_out()

    if time.time() > five_minute:
        print(money_box())
        break