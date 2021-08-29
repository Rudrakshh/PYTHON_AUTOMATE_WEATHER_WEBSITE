from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyperclip
import pyautogui
import time
print("ENTER CITY OR POSTAL CODE")
city=input()
chrome_options = Options()
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)
driver.maximize_window()
driver.get("https://weather.com/en-IN/?Goto=Redirected")
time.sleep(10)
driver.find_element_by_id("LocationSearch_input").click()
pyperclip.copy(city)
pyautogui.hotkey('ctrl','v')
time.sleep(2)
pyautogui.press('enter')
time.sleep(120)
driver.quit()