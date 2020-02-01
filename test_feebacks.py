# -*- coding: utf-8 -*-
import time
import unittest
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # ожидания различных событий
from selenium.webdriver.support.ui import Select  # работа со списками
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains # lля сколддинга к нужному элементу импортируем класс ActionChains
from random import randint
import string

class feedbacks_zavadenie(unittest.TestCase):


    def my_metho_with_predlojenie(self, kolvo_bukv_v_slove, count_slov, count_predlojeniy):

        list_predloj = []

        for k in range(count_predlojeniy):  # цикл по колву предло;ений
            list_slov = []
            # kolvo_bukv_v_slove = randint(3,5) # генерим ково букв в i-ом  слове

            for i in range(count_slov):  # цикл по колву слов, будет 5 слов  строке

                list_bukv = []
                for j in range(kolvo_bukv_v_slove):  # цикл по бкувам в i-ом слове

                    list_bukv.append(' '.join([self.list_characters[randint(0, len(self.list_characters) - 1)]]))

                list_slov.append(''.join(list_bukv))

            list_predloj.append(' '.join(list_slov) + '.')

        return str(' '.join(list_predloj))


    def my_metho_randem_stroka(self, kolvo_bukv_v_slove, count_slov): # генерит предложение

        list_slov = []
        # kolvo_bukv_v_slove = randint(3,5) # генерим ково букв в i-ом  слове

        for i in range(count_slov):  # цикл по колву слов, будет 5 слов  строке

            list_bukv = []
            for j in range(kolvo_bukv_v_slove):  # цикл по бкувам в i-ом слове

                list_bukv.append(' '.join([self.list_characters[randint(0, len(self.list_characters) - 1)]]))

            list_slov.append(''.join(list_bukv))

        return str(' '.join(list_slov))




    def generation_tel_phone(self):  # генерит номер телфона

        list_digits = []
        for i in range(0, 11):
            if i != 0:
                # print(string.digits[randint(0,9)]) # 0123456789
                list_digits.append(string.digits[randint(1, 9)])

        # print(list_digits)

        return str(str(8) + ''.join(list_digits))



    def my_metho_randem_stroka_for_email(self, kolvo_bukv_v_slove, count_slov):

        list_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                           'S', 'T', 'U', 'W', 'X', 'Y', 'Z',
                           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'k', 'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't', 'u', 'w', 'x', 'y', 'z',
                           '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_',  '.'] # добавить символы !,  ? , *, %, #, $, ~

        list_slov = []
        # kolvo_bukv_v_slove = randint(3,5) # генерим ково букв в i-ом  слове

        for i in range(count_slov):  # цикл по колву слов, будет 5 слов  строке

            list_slov = []
            # kolvo_bukv_v_slove = randint(3,5) # генерим ково букв в i-ом  слове

            for i in range(count_slov):  # цикл по колву слов, будет 5 слов  строке

                list_bukv = []
                for j in range(kolvo_bukv_v_slove):  # цикл по бкувам в i-ом слове

                    list_bukv.append(' '.join([list_characters[randint(0, len(list_characters) - 1)]]))

                list_slov.append(''.join(list_bukv))

        for_email = {0: "@yandex.ru", 1: "@mail.ru", 2: "@gmail.com",
                     3:"@yahoo.com", 4:"@felisadipiscing.edu", 5:"@aarcu.net", 6:"@sempereratin.edu", 7:"@estMauriseu.net", 8:"@pharetra.co.uk", 9:"@ut.ca", 10: "@felisDonectempor.org"}

        return str(' '.join(list_slov)) + for_email[randint(0, len(for_email)-1)]


    def authorization(self, driver):

        driver.get("https://admin.preorder.technaxis.com/external/login")

        time.sleep(2)  # чтобы сразу окно не закрывалось

        # авторизация
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='login']"))).send_keys(
            "123@mail.ru")

        time.sleep(2)
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='password']"))).send_keys("password")

        time.sleep(2)

        WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//button[@type='button']")))[
            1].click()


    def filter_on_page_zavadeniy(self, driver): # фильтрация

        # фильтрация по статусу заказа
        # жме мна списко Статус заказа
        WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//mat-select[@role='listbox']")))[0].click()
        time.sleep(2)


        for i in range(0, 4):

            # список пунктов из списка
            list_of_statuses = WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']"))) # жмет на галочку

            list_of_statuses[randint(0, len(list_of_statuses)-1)].click()# выбирает рандомый индекс и кликает
            time.sleep(2)

            WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//mat-select[@role='listbox']")))[0].click()
            time.sleep(2)

        # жмем пункт Все
        WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']")))[0].click()

        time.sleep(3)

        # фильрация по способу оплаты:
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//mat-select[@role='listbox']")))[1].click() # жмет на галочку
        time.sleep(2)

        for i in range(0, 4):
            # список пунктов из списка способов оплаты:
            list_of_paymet_types = WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']")))

            list_of_paymet_types[randint(0, len(list_of_paymet_types) - 1)].click()  # выбирает рандомый индекс и кликает
            time.sleep(2)

            WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//mat-select[@role='listbox']")))[1].click()# жмет на галочку
            time.sleep(2)

         # жмем пункт Все
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']")))[0].click()

        time.sleep(2)

        # Поиск по имени:
        for i in range(0, 4):
            list_of_names = WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located((By.XPATH, "//mat-cell[@class='mat-cell cdk-column-userName mat-column-userName ng-star-inserted']"))) # список id-шников

            rand_index_of_name = randint(0, len(list_of_names)-1) # берем рандомный индекс из спсика

            search_field = WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Поиск']")))

            search_field.send_keys(list_of_names[rand_index_of_name].text) # поле поиска

            time.sleep(2)

            search_field.clear() # очищает поле поиска



    def filter_by_dates(self, driver): # филтрация по датам

          WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located((By.XPATH, "//input[@placeholder='От']"))).click() # Жмем на поле От

          time.sleep(2)

          list_of_dates_from = WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located((By.XPATH, "//div[@class='mat-calendar-body-cell-content']")))# Список дат От

          rand_index_of_from_date = randint(0, len(list_of_dates_from)) # выбираем рандо индекс даты
          list_of_dates_from[rand_index_of_from_date].click()
          time.sleep(2)

          WebDriverWait(driver, 10).until(
              ec.presence_of_element_located((By.XPATH, "//input[@placeholder='До']"))).click()# Жмем на поле До

          time.sleep(2)

          list_of_dates_to = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
                  (By.XPATH, "//div[@class='mat-calendar-body-cell-content']")))  # Список дат До

          rand_index_of_from_to = randint(0, len(list_of_dates_to))  # выбираем рандо индекс даты До
          list_of_dates_to[rand_index_of_from_to].click()
          time.sleep(2)



    def setUp(self):
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver')

        self.driver.set_window_position(0, 0)  # устанавливает позицию левого вурзнего угла окна браузера
        self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна


        #self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()

        self.list_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                                'R', 'S',
                                'T', 'U', 'W', 'X', 'Y', 'Z',
                                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'k', 'm', 'n', 'o', 'p', 'q',
                                'r', 's',
                                't', 'u', 'w', 'x', 'y', 'z', 'A'
                                ' ']  # поле









    def test_feedback_zavedenie_method_(self):  # главный метод, надо чтобы он начинался  с test_

        driver = self.driver

        self.authorization(driver)

        time.sleep(2)

        # жмем на  разедл Заказы  в меню
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH,  "//a[@href='/place/orders']"))).click()

        time.sleep(6)

        #self.filter_on_page_zavadeniy(driver)# вызов метода


        time.sleep(2)
        self.filter_by_dates(driver)# выбор дат в каледнаре



    def tear_down(self):
        time.sleep(5)
        self.driver.quit()
        # pass


if __name__ == "__main__":
    unittest.main()