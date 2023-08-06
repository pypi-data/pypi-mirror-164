# -*- coding: utf-8 -*-
import time

from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Helpers:
    def __init__(self, app):
        self.app = app

    # Проверка перехода на нудную ручку
    @staticmethod
    def pageEndpoint(self, host: str, endpoint: str, locator: str):
        wd = self.app.wd
        if wd.current_url == host + endpoint:
            pass
        else:
            self.click((By.XPATH, locator))
            time.sleep(0.1)
            assert str(wd.current_url) == str(host + endpoint), f" \nОшибка перехода на сраницу! " \
                                                                f"\nОжидаемый адрес:'{host + endpoint}'" \
                                                                f"\nФактический адрес:'{wd.current_url}'"

    # Метод проверки ввода вывода
    def assertEqual(self, input, expected, locator):
        self.Input_values_xpath(input, locator)
        self.Assert_values_xpath(expected, locator)

    # Ввод значений в поле
    def Input_values(self, value, locator):
        try:
            wd = self.app.wd
            element = WebDriverWait(wd, 10).until(
                EC.element_to_be_clickable((By.ID, ('%s' % locator))))
            element.clear()
            element.send_keys(value)
        except Exception as e:
            assert e == TimeoutException, f"Ошибка локатор поля ввода '{locator}' - не найден"

    # Ввод значений в поле xpath
    def Input_values_xpath(self, value, locator):
        try:
            wd = self.app.wd
            element = WebDriverWait(wd, 10).until(
                EC.element_to_be_clickable((By.XPATH, ('%s' % locator))))
            element.clear()
            element.send_keys(value)
            # element.click()
        except Exception as e:
            assert e == TimeoutException, f"Ошибка локатор поля ввода '{locator}' - не найден"

    # Проверка введенных значений в поле xpath
    def Assert_values_xpath(self, value, locator):
        try:
            wd = self.app.wd
            element = WebDriverWait(wd, 10).until(
                EC.element_to_be_clickable((By.XPATH, ('%s' % locator))))
            values = element.get_attribute('value')
            assert str(value) == str(
                values), f"\nОжидаемый результат ввода = '{value}'\nФактическое значение в поле = '{values}'"
        except TimeoutException:
            print(f"Ошибка при проверке локатор поля ввода '{locator}' - не найден")

    # Получить текст
    def get_text(self, locator):
        wd = self.app.wd
        return WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.XPATH, ('%s' % locator)))).text

    # Проверить текст на странице
    def assert_text_on_page(self, locator, list_text):
        info_element = self.get_text(locator)
        for x in list_text:
            assert x in info_element, \
                f"\n----------------------\n" \
                f"Ошибка!\nОжидаемый текст: ***{x}*** - отсутствует на странице!\n" \
                f"\n----------------------\n" \
                f"Фактический текст на странице:\n{info_element}" \
                f"\n----------------------"


    # Проверить отсутствие текста на странице
    def assert_not_text_on_page(self, locator, list_text):
        info_element = self.get_text(locator)
        for x in list_text:
            assert x not in info_element, \
                f"\n----------------------\n" \
                f"Ошибка!\nОжидаемый текст: ***{x}*** - отсутствует на странице!\n" \
                f"\n----------------------\n" \
                f"Фактический текст на странице:\n{info_element}" \
                f"\n----------------------"

    # Клик по элементу
    def click(self, locator):
        try:
            wd = self.app.wd
            element = WebDriverWait(wd, 10).until(
                EC.element_to_be_clickable((locator)))
            element.click()
        except Exception as e:
            assert e == TimeoutException, f"Ошибка! Нет возможности кликнуть по локатору: '{locator}'"


    # Получение длинны списка элементов
    def get_elements_len(self, locator):
        wd = self.app.wd
        return len(wd.find_elements(By.XPATH, locator))

    # Клик по элементу
    def click_clicable(self, locator):
        try:
            wd = self.app.wd
            element = WebDriverWait(wd, 20).until(
                EC.element_to_be_clickable((locator)))
            element.click()
        except Exception as e:
            assert e == TimeoutException, f"Ошибка! Нет возможности кликнуть по локатору: '{locator}'"

    # Проверка статуса кнопок в выходах
    def status_outs_button(self, locator):
        wd = self.app.wd
        element = WebDriverWait(wd, 20).until(
            EC.element_to_be_clickable((locator)))
        class_button = element.get_property("className")
        assert str(
            class_button) == "BTN-primary-text content-left block active", f"Ошибка активации кнопки!\nФактический класс кнопки: '{class_button}'\nОжидаемый: 'BTN-primary-text content-left block active'"

    # Клик по элементу
    def get_atr(self, locator):
        try:
            wd = self.app.wd
            element = WebDriverWait(wd, 10).until(
                EC.element_to_be_clickable((locator)))
            return element.get_property('checked')
        except Exception as e:
            assert e == TimeoutException, f"Ошибка! Нет возможности кликнуть по локатору: '{locator}'"

    # Выбор чекбокса
    def check_box(self, position, click, status):
        try:
            wd = self.app.wd
            element = WebDriverWait(wd, 10).until(
                EC.element_to_be_clickable((By.XPATH, click)))
            selected = wd.find_element(By.XPATH, status)
            if position == "ON":
                if selected.is_selected() == True:
                    pass
                else:
                    element.click()
            elif position == "OFF":
                if selected.is_selected() == False:
                    pass
                else:
                    element.click()
        except Exception as exc:
            assert exc == TimeoutException, f"Ошибка! локатор чекбокса: '{click}' не найден"

    # Проверка выбора чекбокса
    def assert_check_box(self, position, status):
        wd = self.app.wd
        selected = wd.find_element(By.XPATH, status)
        if position == "ON":
            status_check_box = True
        if position == "OFF":
            status_check_box = False
        if selected.is_selected() == False:
            result = 'Не включается'
        if selected.is_selected() == True:
            result = 'Не выключается'
        assert status_check_box == selected.is_selected(), f"Ошибка! Чекбокс: {result}"

    def status_button(self, locator):
        wd = self.app.wd
        selected = wd.find_element(By.XPATH, locator)
        return selected.get_attribute('disabled')

    # Выбор из выпадающего списка
    def Select_from_the_dropdown_list(self, button, position):
        try:
            self.app.method.click((By.XPATH, button))
            self.app.method.click((By.XPATH, position))
        except TimeoutException as exc:
            assert exc == TimeoutException, f"Ошибка!!! Локатор выпадающего списка не найден"

    # Выбор из выпадающего списка с чекбоксом
    def Select_from_the_dropdown_list_check_box(self, button, position, status):
        try:
            wd = self.app.wd
            self.app.method.click((By.XPATH, button))
            selected = wd.find_element(By.XPATH, status)
            if selected.is_selected() == False:
                self.app.method.click((By.XPATH, position))
        except TimeoutException as exc:
            assert exc == TimeoutException, f"Ошибка!!! Локатор выпадающего списка не найден"

    # Выбор из выпадающего списка для сохранения
    def Select_dropdown_list(self, button, name):
        try:
            self.app.method.click((By.XPATH, button))
            self.app.method.click((By.XPATH, f'/html/body//div[@class="option"][.="{name}"]'))
        except TimeoutException as exc:
            assert exc == TimeoutException, f"Ошибка!!! Локатор выпадающего списка не найден"

    # Проверка значения в выпадающем списке
    def assert_Selection_from_the_dropdown_list(self, values, identifier):
        try:
            wd = self.app.wd
            element = wd.find_element(By.XPATH, identifier).get_property("textContent")
            assert str(element) == str(
                values), f"\nОжидаемое значение в выпадающем списке: '{values}'\nФактическое: '{element}'"
        except TimeoutException as exc:
            assert exc == TimeoutException, f"Ошибка локатор выпадающего списка '{identifier}' - не найден"

    # Проверка значения в выпадающем списке
    def assert_Selection_from_the_dropdown_list_check_box(self, values, identifier):
        try:
            wd = self.app.wd
            element = wd.find_element(By.XPATH, identifier).get_property("outerText")
            assert str(values) in str(
                element), f"\nОжидаемое значение в выпадающем списке: '{values}'\nФактическое: '{element}'"
        except TimeoutException as exc:
            assert exc == TimeoutException, f"Ошибка локатор выпадающего списка '{identifier}' - не найден"

    # Виджет ползунок
    def slider_widget(self, volum, identifier):
        try:
            wd = self.app.wd
            slider = wd.find_element(By.XPATH, identifier)
            wd.execute_script("arguments[0].value = arguments[1]", slider, "%s" % volum)
        except Exception as exc:
            assert exc == TimeoutException, f"Ошибка локатор виджета {identifier} ползунка не найден"

    # Проверка виджета ползунка ID
    def assert_slider_widget(self, volum, identifier):
        wd = self.app.wd
        element = wd.find_element(By.XPATH, identifier).get_property("value")
        assert int(element) == int(
            volum), f"\n***Неверное положение виджета ползунка!***\nОжидаемое:'{volum}'\nФактическое:'{element}'"

    # Проверка текста всплывающей подсказки
    def assert_tooltip_text(self, text):
        locator = '//*[@class="b-tooltip-text"]'
        actual_text = self.get_text(locator)
        assert str(text) == str(
            actual_text), f"\nОшибка при проверке всплывающей подсказки!\nОжидаемый текст: '{text}'\nФактический текст: '{actual_text}'"

    # Выбор из выпадающего списка по названию
    def Select_from_the_dropdown_list_by_name(self, button, position):
        try:
            self.app.method.click((By.XPATH, button))
            time.sleep(0.5)
            self.app.method.click((By.XPATH, f'/html/body//div[@class="option"][.="{position}"]'))
        except TimeoutException as exc:
            assert exc == TimeoutException, f"Ошибка!!! Локатор выпадающего списка не найден"

    # Ввод значений в поле xpath
    def element_focus(self, locator):
        try:
            wd = self.app.wd
            element = WebDriverWait(wd, 10).until(
                EC.element_to_be_clickable((By.XPATH, ('%s' % locator))))
            action = ActionChains(wd)
            action.move_to_element(element).perform()
        except TimeoutException as exc:
            assert exc == TimeoutException, f"Ошибка!!! Локатор '{locator}' не найден"
