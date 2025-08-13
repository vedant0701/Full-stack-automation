from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

@when(u"user add '{product}' into the cart")
def step_impl(context, product):
    wait = WebDriverWait(context.driver, 10)

    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))

    xpath = f"//div[normalize-space(text())='{product}']/ancestor::div[@class='inventory_item']//button"

    cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    cart_button.click()
    logging.info(f"Item '{product}' added to the cart")
    
@then("the user goes to the cart")
def stepimpl(context):
    carts = context.driver.find_element(By.XPATH, "//div[contains(@class,'shopping_cart_container')]")
    carts.click()
    logging.info("user navigated to cart")
    time.sleep(1)

@then(u"Click on button with '{button}' label")
def cart(context, button):
    in_cart = context.driver.find_element(By.XPATH, f"//div[@class='cart_footer']/a[text()='{button}']")
    in_cart.click()
    time.sleep(1)