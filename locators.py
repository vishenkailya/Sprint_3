from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_SCREEN = (By.XPATH, '//h2') #Экран авторизации
    BUTTON_MY_ACCOUNT = (By.XPATH, '//p[text()="Личный Кабинет"]') #Кнопка "Личный кабинет"
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']") #Поле для ввода почты при входе
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']") #Поле для ввода пароля при входе
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти"]') #Кнопка "Вход" при входе в аккаунт
    LOGIN_WINDOW = (By.XPATH, '//h2') #Надпись Вход при авторизации
    BUTTON_SIGN_IN = (By.XPATH, '//button[text()="Войти в аккаунт"]') #Кнопка войти в аккаунт на главном окне
    BUTTON_MAKE_ORDER = (By.XPATH, '//button[text()="Оформить заказ"]') #Кнопка Оформить заказ после авторизации
    REGISTRATION_BUTTON = (By.XPATH, "//a[contains(text(), 'Зарегистрироваться')]") #Кнопка "Зарегестрироваться"
    REGISTRATION_NAME_INPUT = (By.XPATH, "//input[@name='name']") #Поле для ввода имени при регистрации
    #Этот локатор никак не исправить
    REGISTRATION_EMAIL_INPUT = (By.XPATH, "//fieldset[2]/div/div/input[@name='name']") #Поле для ввода почты при регистрации
    REGISTRATION_PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']") #Поле для ввода пароля при регистрации
    BUTTON_REGISTER = (By.XPATH, '//button[text()="Зарегистрироваться"]') #Кнопка "Зарегистрироваться"
    PROFILE_MARK_LOGGED_IN = (By.XPATH, '//a[text()="Профиль"]') #Подтверждение, что пользователь авторизировался
    BUTTON_PROFILE_LOGGED_IN_EXIT = (By.XPATH, '//button[text()="Выход"]') #Кнопка для выхода
    BUTTON_CONSTRUCTOR = (By.XPATH, '//p[text()="Конструктор"]') #Кнопка перехода к конструктору
    MAKE_BURGER_HEADER = (By.XPATH, '//section[1]/h1') #Хэдер конструктора бургеров
    BOOKMARK_BUNS = (By.XPATH, '//span[text() = "Булки"]') #Вкладка булочек
    BUNS_SECTION = (By.XPATH, '//h2[text() = "Булки"]') #Раздел булочек
    BOOKMARK_SAUCE = (By.XPATH, '//span[text() = "Соусы"]') #Вкладка соусов
    SAUCE_SECTION = (By.XPATH, '//h2[text() = "Соусы"]') #Раздел соусов
    BOOKMARK_TOPPING = (By.XPATH, '//span[text() = "Начинки"]') #Вкладка начинок
    TOPPING_SECTION = (By.XPATH, '//h2[text() = "Начинки"]') #Раздел начинок
    REGISTRATION = (By.XPATH, "//h2") #Страница регистрации
    LOGIN_FROM_REGISTRATION = (By.XPATH, '//a[text()="Войти"]') #Кнопка авторизации на странице регистрации
    LOST_PASSWORD = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]") #Кнопка "Забыл пароль"
    LOST_PASSWORD_PAGE = (By.XPATH, '//h2') #Страница восстановления пароля
    LOGIN_FROM_RECOVERY = (By.XPATH, "//a[contains(text(), 'Войти')]") #Кнопка авторизации на странице восстановления пароля
    MESSAGE_INCORRECT_PASSWORD = (By.XPATH, '//fieldset[2]/div/p[text()="Некорректный пароль"]') #Сообщение о неправильно пароле
    MESSAGE_INCORRECT_REGISTRATION = (By.XPATH, '//p[text()="Некорректный пароль"]')#Сообщение о неверной регистрации



