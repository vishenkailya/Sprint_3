import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from locators import LoginPageLocators as L


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get('https://stellarburgers.nomoreparties.site/')
    return browser


@pytest.fixture(scope="function")
def login(driver):
    driver.find_element(*L.BUTTON_MY_ACCOUNT).click()
    WebDriverWait(driver, 3). \
        until(expected_conditions.visibility_of_element_located(L.LOGIN_WINDOW))
    driver.find_element(*L.EMAIL_INPUT). \
        send_keys('ilya_vishnyakov_11@gmail.com')
    driver.find_element(*L.PASSWORD_INPUT). \
        send_keys('12345678')
    driver.find_element(*L.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3). \
        until(expected_conditions.visibility_of_element_located(L.BUTTON_MAKE_ORDER))
    yield driver


@pytest.fixture(scope="function")
def open_registration_form(driver):
    driver.find_element(*L.BUTTON_MY_ACCOUNT).click()
    WebDriverWait(driver, 3). \
        until(expected_conditions.visibility_of_element_located(L.LOGIN_WINDOW))
    driver.find_element(*L.REGISTRATION_BUTTON).click()
    WebDriverWait(driver, 3). \
        until(expected_conditions.visibility_of_element_located(L.REGISTRATION))
    yield driver
    driver.quit()
