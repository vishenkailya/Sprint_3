import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import login
from conftest import driver
from locators import LoginPageLocators as L


class TestGoToConstructor:

    def test_go_to_constructor_from_my_page_changed_url(self, login):
        WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located(L.BUTTON_MAKE_ORDER))
        login.find_element(*L.BUTTON_MY_ACCOUNT).click()
        WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located(L.PROFILE_MARK_LOGGED_IN))
        login.find_element(*L.BUTTON_CONSTRUCTOR).click()
        WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located(L.MAKE_BURGER_HEADER))
        assert login.current_url == 'https://stellarburgers.nomoreparties.site/' \
               and login.find_element(*L.MAKE_BURGER_HEADER).text == 'Соберите бургер'
