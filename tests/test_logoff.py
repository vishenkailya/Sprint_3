import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import login
from conftest import driver
from locators import LoginPageLocators as L

class TestLogOff:

    def test_logging_out_logged_off(self, login):
        WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located(L.BUTTON_MAKE_ORDER))
        login.find_element(*L.BUTTON_MY_ACCOUNT).click()
        WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located(L.PROFILE_MARK_LOGGED_IN))
        login.find_element(*L.BUTTON_PROFILE_LOGGED_IN_EXIT).click()
        WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located(L.LOGIN_WINDOW))
        assert login.current_url == 'https://stellarburgers.nomoreparties.site/login'