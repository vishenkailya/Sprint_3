import random
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers import random_email
from helpers import random_password
from helpers import random_name
from conftest import driver
from conftest import open_registration_form
from locators import LoginPageLocators as L


class TestRegistration:

    def test_correct_registration_opens_login_screen(self, open_registration_form):
        open_registration_form.find_element(*L.REGISTRATION_NAME_INPUT).send_keys(random_name(random.randint(3, 8)))
        open_registration_form.find_element(*L.REGISTRATION_EMAIL_INPUT).send_keys(random_email())
        open_registration_form.find_element(*L.REGISTRATION_PASSWORD_INPUT).send_keys(random_password(random.randint(6, 12)))
        open_registration_form.find_element(*L.BUTTON_REGISTER).click()
        WebDriverWait(open_registration_form, 3). \
            until(expected_conditions.url_contains('login'))
        assert open_registration_form.current_url == 'https://stellarburgers.nomoreparties.site/login'
        open_registration_form.quit()

    def test_short_password_registration_denied_warning_message(self, open_registration_form):
        open_registration_form.find_element(*L.REGISTRATION_NAME_INPUT).send_keys(random_name(random.randint(3, 8)))
        open_registration_form.find_element(*L.REGISTRATION_EMAIL_INPUT).send_keys(random_email())
        open_registration_form.find_element(*L.REGISTRATION_PASSWORD_INPUT).send_keys(random_password(random.randint(0,5)))
        open_registration_form.find_element(*L.BUTTON_REGISTER).click()
        WebDriverWait(open_registration_form, 3). \
            until(expected_conditions.url_contains('register'))
        WebDriverWait(open_registration_form, 3). \
            until(expected_conditions.
                  visibility_of_element_located(L.MESSAGE_INCORRECT_REGISTRATION))
        assert open_registration_form.find_element(*L.MESSAGE_INCORRECT_REGISTRATION). \
                   text == 'Некорректный пароль'
        open_registration_form.quit()


