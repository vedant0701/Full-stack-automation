from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

@given(f"the user is on the login page")
def step(context):
    context.driver.get(context.base_url)

@when(u"The user logins with username '{username}' and password '{password}'")
def step_impl(context, username, password):
    user_name = context.driver.find_element(By.ID, "user-name")
    user_name.send_keys(username)
    time.sleep(1)
    password_field = context.driver.find_element(By.ID, "password")
    password_field.send_keys(password)
    time.sleep(1)
    login_button = context.driver.find_element(By.ID, "login-button")
    login_button.click()

@then("the user logins and is on the homepage")
def stepimpl(self):
    logging.info("Logged in successfully")
    time.sleep(2)