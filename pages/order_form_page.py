import allure
from locators.order_form_page_locators import TestOrderFormPageLocators
from pages.base_page import BasePage


class OrderFormPage(BasePage):

    @allure.step('Заполнить поле "Имя"')
    def set_first_name(self, name):
        self.set_text_to_elm(TestOrderFormPageLocators.FIRST_NAME_FIELD, name)
        return self

    @allure.step('Проверка, что поле "Имя" содержит значение')
    def check_first_name_value(self, expected_value):
        field = self.find_element_with_wait(TestOrderFormPageLocators.FIRST_NAME_FIELD)
        assert field.get_attribute('value') == expected_value, "Значение в поле 'Имя' не совпадает с ожидаемым"

    @allure.step('Заполнить поле "Фамилия"')
    def set_last_name(self, last_name):
        self.set_text_to_elm(TestOrderFormPageLocators.LAST_NAME_FIELD, last_name)
        return self

    @allure.step('Заполнить поле "Адрес"')
    def set_address(self, address):
        self.set_text_to_elm(TestOrderFormPageLocators.ADDRESS_FIELD, address)
        return self

    @allure.step('Заполнить поле "Метро"')
    def set_metro(self, station):
        self.click_on_element(TestOrderFormPageLocators.METRO_STATION_FIELD)
        self.set_text_to_elm(TestOrderFormPageLocators.METRO_STATION_FIELD, station)
        self.click_on_element(TestOrderFormPageLocators.SELECTED_STATION)
        return self

    def check_metro_value(self, station):
        field = self.find_element_with_wait(TestOrderFormPageLocators.METRO_STATION_FIELD)
        expected_value = station
        assert field.get_attribute('value') == expected_value, "Значение в поле 'Метро' не совпадает с ожидаемым"

    @allure.step('Заполнить поле "Телефон"')
    def set_phone(self, number):
        self.set_text_to_elm(TestOrderFormPageLocators.PHONE_NUMBER_FIELD, number)
        return self

    @allure.step('Нажать кнопку "Далее"')
    def click_next_button(self):
        self.click_on_element(TestOrderFormPageLocators.CONTINUE_BUTTON)

    @allure.step('Проверка отображения заголовка второй формы')
    def check_the_title_of_second_form_displaying(self):
        self.check_displaying_of_element(TestOrderFormPageLocators.TITLE_ABOUT_RENT_FORM)

    @allure.step('Заполнить поле "Дата аренды"')
    def set_rental_date(self):
        self.click_on_element(TestOrderFormPageLocators.RENTAL_DATE_FIELD)
        self.find_element_with_wait(TestOrderFormPageLocators.CALENDAR)
        today = self.find_element_with_wait(TestOrderFormPageLocators.TODAY_DATE_CALENDAR)
        tomorrow = today.find_element(*TestOrderFormPageLocators.TOMORROW_DATE_CALENDAR)
        tomorrow.click()
        return self

    @allure.step('Заполнить поле "Срок аренды"')
    def set_rental_duration(self):
        self.click_on_element(TestOrderFormPageLocators.RENTAL_DURATION_FIELD)
        self.find_element_with_wait(TestOrderFormPageLocators.RENTAL_DURATION_LIST)
        self.click_on_element(TestOrderFormPageLocators.DROPDOWN_ITEM_RENTAL_PERIOD)


    def set_color_field(self):
        self.click_on_element(TestOrderFormPageLocators.CHECKBOX_GREY)
        return self

    def set_comment_field(self, comment):
        self.set_text_to_elm(TestOrderFormPageLocators.COMMENT_FIELD, comment)
        return self

    @allure.step('Нажать кнопку "Заказать"')
    def click_order_button(self):
        self.click_on_element(TestOrderFormPageLocators.ORDER_BUTTON)
        self.find_element_with_wait(TestOrderFormPageLocators.POP_UP_CONFIRM_ORDER)

    @allure.step('Проверка отображения окна подтверждения после нажатия кнопки Заказать')
    def check_displaying_of_confirm_window(self):
        self.check_displaying_of_element(TestOrderFormPageLocators.POP_UP_CONFIRM_ORDER)

    @allure.step('Нажать кнопку "Да" в окне подтверждения заказа')
    def click_yes_button_confirmation_pop_up(self):
        self.click_on_element(TestOrderFormPageLocators.YES_BUTTON_POP_UP_CONFIRM_ORDER)
        self.find_element_with_wait(TestOrderFormPageLocators.POP_UP_COMPLETE_ORDER)
        return self


    @allure.step('Заполнение первой части формы и нажатие кнопки "Далее"')
    def personal_information_input(self, name, last_name, address, station, number):
        self.set_first_name(name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.set_metro(station)
        self.check_metro_value(station)
        self.set_phone(number)
        self.click_next_button()
        self.check_the_title_of_second_form_displaying()

    @allure.step('Заполнение второй части формы и окно подтверждения')
    def rental_information_input(self, comment):
        self.set_rental_date()
        self.set_rental_duration()
        self.set_color_field()
        self.set_comment_field(comment)
        self.click_order_button()
        self.check_displaying_of_confirm_window()