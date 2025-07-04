import allure
import pytest
from locators.order_form_page_locators import TestOrderFormPageLocators
from data_tests import user_1, user_2


class TestOrderForm:

    @allure.title('Проверка флоу позитивного сценария оформления заказа посредством верхней кнопки "Заказать')
    @allure.description('Проверка перехода в форму заказа через нажатие кнопки "Заказать" в хедере и успешного оформления заказа')
    @pytest.mark.parametrize('name, last_name, address, station, number, comment', [user_1])
    def test_complete_order_form_order_button_header(self, driver, home_page, order_page, name, last_name, address, station, number, comment):
        home_page.click_order_button_header()
        order_page.personal_information_input(name, last_name, address, station, number)
        order_page.rental_information_input(comment)
        order_page.click_yes_button_confirmation_pop_up()
        assert driver.find_element(*TestOrderFormPageLocators.POP_UP_COMPLETE_ORDER).is_displayed()

    @allure.title('Проверка флоу позитивного сценария оформления заказа посредством нижней кнопки "Заказать')
    @allure.description('Проверка перехода в форму заказа через нажатие кнопки "Заказать" в теле и успешного оформления заказа')
    @pytest.mark.parametrize('name, last_name, address, station, number, comment', [user_2])
    def test_complete_order_form_order_button_body(self, driver, home_page, order_page, name, last_name, address, station, number, comment):
        home_page.click_order_button_body()
        order_page.personal_information_input(name, last_name, address, station, number)
        order_page.rental_information_input(comment)
        order_page.click_yes_button_confirmation_pop_up()
        assert driver.find_element(*TestOrderFormPageLocators.POP_UP_COMPLETE_ORDER).is_displayed()