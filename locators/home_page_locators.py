from selenium.webdriver.common.by import By


class TestHomePageLocators:

    # Кнопка Заказать в хедере
    ORDER_BUTTON_HEADER = By.CLASS_NAME, 'Button_Button__ra12g'
    # Кнопка Заказать в теле страницы
    ORDER_BUTTON_BODY = By.CLASS_NAME, 'Button_Middle__1CSJM'
    # Блок "Как это работает"
    HOW_IT_WORKS_BLOCK = By.XPATH, '//div[text()="Как это работает"]'
    # Кнопка Принять куки
    ACCEPT_COOKIE_BUTTON = By.ID, 'rcc-confirm-button'

    # Блок FAQ
    # Первый вопрос
    ACCORDION_BUTTON_FAQ_1 = By.ID, 'accordion__heading-0'
    # Первый ответ
    ANSWER_FAQ_1 = By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-0"]:not([hidden]) p'
    # Второй вопрос
    ACCORDION_BUTTON_FAQ_2 = By.ID, 'accordion__heading-1'
    # Второй ответ
    ANSWER_FAQ_2 = By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-1"]:not([hidden]) p'
    # Третий вопрос
    ACCORDION_BUTTON_FAQ_3 = By.ID, 'accordion__heading-2'
    # Третий ответ
    ANSWER_FAQ_3 = By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-2"]:not([hidden]) p'
    # Четвертый вопрос
    ACCORDION_BUTTON_FAQ_4 = By.ID, 'accordion__heading-3'
    # Четвертый ответ
    ANSWER_FAQ_4 = By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-3"]:not([hidden]) p'
    # Пятый вопрос
    ACCORDION_BUTTON_FAQ_5 = By.ID, 'accordion__heading-4'
    # Пятый ответ
    ANSWER_FAQ_5 = By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-4"]:not([hidden]) p'
    # Шестой вопрос
    ACCORDION_BUTTON_FAQ_6 = By.ID, 'accordion__heading-5'
    # Шестой ответ
    ANSWER_FAQ_6 = By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-5"]:not([hidden]) p'
    # Седьмой вопрос
    ACCORDION_BUTTON_FAQ_7 = By.ID, 'accordion__heading-6'
    # Седьмой ответ
    ANSWER_FAQ_7 = By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-6"]:not([hidden]) p'
    # Восьмой вопрос
    ACCORDION_BUTTON_FAQ_8 = By.ID, 'accordion__heading-7'
    # Восьмой ответ
    ANSWER_FAQ_8 = By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-7"]:not([hidden]) p'
    # Логотип Яндекс
    LOGO_YANDEX = By.CLASS_NAME, "Header_LogoYandex__3TSOI"
    # Логотип Самокат
    LOGO_SAMOKAT = By.CLASS_NAME, "Header_LogoScooter__3lsAR"