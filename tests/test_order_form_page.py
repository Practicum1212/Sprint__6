import allure
import pytest

from data_tests import user_1, user_2
from pages.order_form_page import OrderFormPage
from locators.order_form_page_locators import TestOrderFormPageLocators
from pages.home_page import HomePageSamokat
from locators.home_page_locators import TestHomePageLocators

class TestOrderForm:
    @allure.title('Проверка флоу позитивного сценария оформления заказа посредством верхней кнопки "Заказать"')
    @allure.description('Проверка перехода в форму заказа через нажатие кнопки "Заказать" в хедере и успешного оформления заказа')
    @pytest.mark.parametrize('name, last_name, address, station, number, comment', [user_1])
    def test_complete_order_form_order_button_header(self, driver, name, last_name, address, station, number, comment):
        home_page = HomePageSamokat(driver)
        order_page = OrderFormPage(driver)

        home_page.scroll_to_element(TestHomePageLocators.ORDER_BUTTON_HEADER)
        home_page.click_on_element(TestHomePageLocators.ORDER_BUTTON_HEADER)
        order_page.personal_information_input(name, last_name, address, station, number)
        order_page.rental_information_input(comment)
        order_page.click_yes_button_confirmation_pop_up()
        assert order_page.check_displaying_of_element(TestOrderFormPageLocators.POP_UP_COMPLETE_ORDER)

    @allure.title('Проверка флоу позитивного сценария оформления заказа посредством нижней кнопки "Заказать"')
    @allure.description('Проверка перехода в форму заказа через нажатие кнопки "Заказать" в теле и успешного оформления заказа')
    @pytest.mark.parametrize('name, last_name, address, station, number, comment', [user_2])
    def test_complete_order_form_order_button_body(self, driver, name, last_name, address, station, number, comment):
        home_page = HomePageSamokat(driver)
        order_page = OrderFormPage(driver)

        home_page.scroll_to_element(TestHomePageLocators.ORDER_BUTTON_BODY)
        home_page.click_on_element(TestHomePageLocators.ORDER_BUTTON_BODY)
        order_page.personal_information_input(name, last_name, address, station, number)
        order_page.rental_information_input(comment)
        order_page.click_yes_button_confirmation_pop_up()
        assert order_page.check_displaying_of_element(TestOrderFormPageLocators.POP_UP_COMPLETE_ORDER)

































