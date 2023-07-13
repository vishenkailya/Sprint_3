import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import login
from conftest import driver
from locators import LoginPageLocators as L


class TestConstructor:

    def test_constructor_bookmarks_buns_logged_in_changed_bookmarks(self, login):
        WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located(L.MAKE_BURGER_HEADER))
        login.find_element(*L.BOOKMARK_TOPPING).click()
        login.find_element(*L.BOOKMARK_BUNS).click()
        WebDriverWait(login, 4).until(expected_conditions.visibility_of_element_located(L.BUNS_SECTION))
        assert WebDriverWait(login, 4).until(expected_conditions.visibility_of_element_located(L.BUNS_SECTION))

    def test_constructor_bookmarks_sauce_logged_in_changed_bookmarks(self, login):
        WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located(L.MAKE_BURGER_HEADER))
        login.find_element(*L.BOOKMARK_SAUCE).click()
        assert WebDriverWait(login, 4).until(expected_conditions.visibility_of_element_located(L.SAUCE_SECTION))

    def test_constructor_bookmarks_toppings_logged_in_changed_bookmarks(self, login):
        WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located(L.MAKE_BURGER_HEADER))
        login.find_element(*L.BOOKMARK_TOPPING).click()
        assert WebDriverWait(login, 4).until(expected_conditions.visibility_of_element_located(L.TOPPING_SECTION))
