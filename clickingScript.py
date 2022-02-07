from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import easygui

print("Choose your desired web driver")
print("Chrome, Firefox or Edge")
print("!!Only .exe or .dmg files!!\n")
filename = easygui.fileopenbox()

url = input("Write in a URL: ")

print("A locator enables testers to select an HTML DOM element to act on.")
print("1 = Find element by id!")
print("2 = Find element by css selector!")
print("3 = Find element by class name!")
print("4 = Find element by name!")
print("5 = Find element by link text!")
print("6 = Find element by partial link text!")
print("7 = Find element by tag name!")
print("8 = Find element by xpath!\n")
inputLocator = int(input("Pick a locator by writing a number: "))
inputClickDetail = input("\nWrite in the name of the HTML element to click on: ")
inputLoopNumber = int(input("\nWrite in the number of clicks that will be performed: "))

if 'chromedriver.exe' in filename:
    driver = webdriver.Chrome(filename)
    driver.get("https://" + url)
    driver.maximize_window()
    time.sleep(30)
elif 'geckodriver.exe' in filename:
    driver = webdriver.Firefox(filename)
    driver.get("https://" + url)
    time.sleep(3)
    driver.maximize_window()
elif 'msedgedriver.exe' in filename:
    driver = webdriver.Edge(filename)
    driver.get("https://" + url)
    time.sleep(3)
    driver.maximize_window()
else:
    print("!!Wrong file!!")
    print("Download a compatible web driver")
    print("Chrome --> https://chromedriver.storage.googleapis.com/index.html")
    print("Firefox --> https://github.com/mozilla/geckodriver/releases")
    print("Edge --> https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/")


def clickingLoop(inputLocator, inputClickDetail, inputLoopNumber):

    if inputLocator == 1:
        for _ in range(inputLoopNumber):
            driver.find_element(By.ID, inputClickDetail).click()
    elif inputLocator == 2:
        for _ in range(inputLoopNumber):
            driver.find_element(By.CSS_SELECTOR, inputClickDetail).click()
    elif inputLocator == 3:
        for _ in range(inputLoopNumber):
            driver.find_element(By.CLASS_NAME, inputClickDetail).click()
    elif inputLocator == 4:
        for _ in range(inputLoopNumber):
            driver.find_element(By.NAME, inputClickDetail).click()
    elif inputLocator == 5:
        for _ in range(inputLoopNumber):
            driver.find_element(By.LINK_TEXT, inputClickDetail).click()
    elif inputLocator == 6:
        for _ in range(inputLoopNumber):
            driver.find_element(By.PARTIAL_LINK_TEXT, inputClickDetail).click()
    elif inputLocator == 7:
        for _ in range(inputLoopNumber):
            driver.find_element(By.TAG_NAME, inputClickDetail).click()
    elif inputLocator == 8:
        for _ in range(inputLoopNumber):
            driver.find_element(By.XPATH, inputClickDetail).click()
    else:
        print("Choose a number between 1 an 8!")

    print("The clicking is finished!")

clickingLoop(inputLocator, inputClickDetail, inputLoopNumber)
