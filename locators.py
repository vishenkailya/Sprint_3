from typing import Tuple

from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_SCREEN = (By.XPATH, '//*[@id="root"]/div/main/div') #Экран авторизации
    BUTTON_MY_ACCOUNT = (By.XPATH, '//p[text()="Личный Кабинет"]') #Кнопка "Личный кабинет"
    EMAIL_INPUT = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input') #Поле для ввода почты при входе
    PASSWORD_INPUT = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input') #Поле для ввода пароля при входе
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти"]') #Кнопка "Вход" при входе в аккаунт
    LOGIN_WINDOW = (By.XPATH, '//*[@id="root"]/div/main/div/h2') #Надпись Вход при авторизации
    BUTTON_SIGN_IN = (By.XPATH, '//button[text()="Войти в аккаунт"]') #Кнопка войти в аккаунт на главном окне
    BUTTON_MAKE_ORDER = (By.XPATH, '//button[text()="Оформить заказ"]') #Кнопка Оформить заказ после авторизации
    REGISTRATION_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a') #Кнопка "Зарегестрироваться"
    REGISTRATION_NAME_INPUT = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input') #Поле для ввода имени при регистрации
    REGISTRATION_EMAIL_INPUT = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input') #Поле для ввода почты при регистрации
    REGISTRATION_PASSWORD_INPUT = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input') #Поле для ввода пароля при регистрации
    BUTTON_REGISTER = (By.XPATH, '//button[text()="Зарегистрироваться"]') #Кнопка "Зарегистрироваться"
    PROFILE_MARK_LOGGED_IN = (By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[1]/a') #Подтверждение, что пользователь авторизировался
    BUTTON_PROFILE_LOGGED_IN_EXIT = (By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button') #Кнопка для выхода
    BUTTON_CONSTRUCTOR = (By.XPATH, '/html/body/div/div/header/nav/ul/li[1]/a/p') #Кнопка перехода к конструктору
    MAKE_BURGER_HEADER = (By.XPATH, '/html/body/div/div/main/section[1]/h1') #Хэдер конструктора бургеров
    BOOKMARK_BUNS = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]') #Вкладка булочек
    BUNS_SECTION = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[1]') #Раздел булочек
    BOOKMARK_SAUCE = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]') #Вкладка соусов
    SAUCE_SECTION = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[2]') #Раздел соусов
    BOOKMARK_TOPPING = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]') #Вкладка начинок
    TOPPING_SECTION = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[3]') #Раздел начинок
    REGISTRATION = (By.CSS_SELECTOR, '#root > div > main > div > h2') #Страница регистрации
    LOGIN_FROM_REGISTRATION = (By.XPATH, '//*[@id="root"]/div/main/div/div/p/a') #Кнопка авторизации на странице регистрации
    LOST_PASSWORD = (By.XPATH, '//*[@id="root"]/div/main/div/div/p[2]/a') #Кнопка "Забыл пароль"
    LOST_PASSWORD_PAGE = (By.XPATH, '//*[@id="root"]/div/main/div/h2') #Страница восстановления пароля
    LOGIN_FROM_RECOVERY = (By.CSS_SELECTOR, '#root > div > main > div > div > p > a') #Кнопка авторизации на странице восстановления пароля
    MESSAGE_INCORRECT_PASSWORD = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/p') #Сообщение о неправильно пароле
    MESSAGE_INCORRECT_REGISTRATION = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/p')#Сообщение о неверной регистрации



