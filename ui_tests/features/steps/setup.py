import selenium
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

URL = "https://www.saucedemo.com/v1/"

driver = webdriver.Chrome()

driver.get(URL)

