from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import login
from conftest import driver
from locators import LoginPageLocators as L
from helpers import random_password


class TestLogin:

    def test_open_login_window_from_main_page_correct_page(self, driver):
        driver.find_element(*L.BUTTON_SIGN_IN).click()
        WebDriverWait(driver, 3). \
            until(expected_conditions.visibility_of_element_located(L.LOGIN_SCREEN))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()

    def test_open_login_window_from_my_account_correct_page(self, driver):
        driver.find_element(*L.BUTTON_MY_ACCOUNT).click()
        WebDriverWait(driver, 3). \
            until(expected_conditions.visibility_of_element_located(L.LOGIN_SCREEN))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()

    def test_input_login_in_logged_in(self, login):
        assert login.find_element(*L.BUTTON_MAKE_ORDER).text == 'Оформить заказ'
        login.quit()

    def test_wrong_input_password_warning(self, driver):
        driver.find_element(*L.BUTTON_MY_ACCOUNT).click()
        WebDriverWait(driver, 3). \
            until(expected_conditions.visibility_of_element_located(L.LOGIN_SCREEN))
        driver.find_element(*L.EMAIL_INPUT). \
            send_keys('ilya_vishnyakov_11@gmail.com')
        driver.find_element(*L.PASSWORD_INPUT). \
            send_keys(random_password(3))
        driver.find_element(*L.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3). \
            until(expected_conditions.
                  visibility_of_element_located(L.MESSAGE_INCORRECT_PASSWORD))
        assert driver.find_element(*L.MESSAGE_INCORRECT_PASSWORD). \
                   text == 'Некорректный пароль'
        driver.quit()

    def test_logging_in_from_registration_page_main_page_logged_in(self, driver):
        driver.find_element(*L.BUTTON_SIGN_IN).click()
        WebDriverWait(driver, 3). \
            until(expected_conditions.visibility_of_element_located(L.LOGIN_WINDOW))
        driver.find_element(*L.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3). \
            until(expected_conditions.visibility_of_element_located(L.REGISTRATION))
        driver.find_element(*L.LOGIN_FROM_REGISTRATION).click()
        WebDriverWait(driver, 3). \
            until(expected_conditions.visibility_of_element_located(L.LOGIN_WINDOW))
        driver.find_element(*L.EMAIL_INPUT).send_keys('ilya_vishnyakov_11@gmail.com')
        driver.find_element(*L.PASSWORD_INPUT).send_keys('12345678')
        driver.find_element(*L.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3). \
            until(expected_conditions.visibility_of_element_located(L.BUTTON_MAKE_ORDER))
        assert driver.find_element(*L.BUTTON_MAKE_ORDER).text == 'Оформить заказ'
        driver.quit()

    def test_logging_in_from_password_recovery_page_main_page_logged_in(self, driver):
        driver.find_element(*L.BUTTON_MY_ACCOUNT).click()
        WebDriverWait(driver, 3). \
            until(expected_conditions.visibility_of_element_located(L.LOGIN_WINDOW))
        driver.find_element(*L.LOST_PASSWORD).click()
        WebDriverWait(driver, 3). \
            until(expected_conditions.visibility_of_element_located(L.LOST_PASSWORD_PAGE))
        driver.find_element(*L.LOGIN_FROM_RECOVERY).click()
        WebDriverWait(driver, 3). \
            until(expected_conditions.visibility_of_element_located(L.LOGIN_WINDOW))
        driver.find_element(*L.EMAIL_INPUT).send_keys('ilya_vishnyakov_11@gmail.com')
        driver.find_element(*L.PASSWORD_INPUT).send_keys('12345678')
        driver.find_element(*L.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3). \
            until(expected_conditions.visibility_of_element_located(L.BUTTON_MAKE_ORDER))
        assert driver.find_element(*L.BUTTON_MAKE_ORDER).text == 'Оформить заказ'
        driver.quit()
