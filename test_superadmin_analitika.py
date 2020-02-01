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
from selenium.webdriver.common.action_chains import ActionChains # lля сколинга к нужному элементу импортируем класс ActionChains
from random import randint
import string

class Analitika_superadmin(unittest.TestCase):


    def my_metho_with_predlojenie(self, kolvo_bukv_v_slove, count_slov, count_predlojeniy):

        list_predloj = []

        for k in range(count_predlojeniy):  # цикл по колву предло;ений
            list_slov = []
            # kolvo_bukv_v_slove = randint(3,5) # генерим ково букв в i-ом  слове

            for i in range(count_slov):  # цикл по колву слов, будет 5 слов  строке

                list_bukv = []
                for j in range(kolvo_bukv_v_slove):  # цикл по буквам в i-ом слове

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


    def authorizatuion(self, driver):

        driver.get("https://admin.preorder.technaxis.com/external/login")

        time.sleep(2)  # чтобы сразу окно не закрывалось
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='login']"))).send_keys(
            "admin@ujezakazal.ru")

        time.sleep(2)
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='password']"))).send_keys("password")

        time.sleep(2)

        WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//button[@type='button']")))[
            1].click()

        time.sleep(5)


    def sortirovka(self, driver):

        # WebDriverWait(driver, 10).until(
        #     ec.presence_of_element_located((By.XPATH, "//button[@aria-label='Change sorting for id']"))).click()

        for i in range(0, 6):

            WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//mat-header-cell[@role='columnheader']")))[i].click()
            time.sleep(3)
            WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//mat-header-cell[@role='columnheader']")))[i].click()# еще раз жмем на этот же столбец

            time.sleep(3)






    def setUp(self):
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver')#Firefox()

        self.driver.set_window_position(0, 0)  # устанавливает позицию левого верзнего угла окна браузера
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



    def test_analitika_superadmin_method_(self):  # главный метод, надо чтобы он начинался  с test_

        driver = self.driver
        self.authorizatuion(driver) # меода автризвация


        #жмем  в меню на Аналитика:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//a[@href='/superadmin/analytics']"))).click()

        time.sleep(2)



        for i in range(0, 5):

            if i == 4: # если итерация последняя то жмет на Все

                # жмем на выбор города(маленький треугольничек)
                WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located((By.XPATH, "//mat-select[@role='listbox']")))[0].click()
                time.sleep(2)
                # список городов
                list_towns = WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located(
                        (By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']")))


                time.sleep(2)
                list_towns[0].click() # жмет на Все

            else:
                # жмем на выбор города(маленький треугольничек)
                WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located((By.XPATH, "//mat-select[@role='listbox']")))[0].click()
                time.sleep(2)
                # список городов
                list_towns = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']")))
                list_towns[randint(0, len(list_towns)-1)].click() # выбирете любой индекс из спсика

                time.sleep(2)


        #driver.refresh() # перезагужае  страницу


        time.sleep(3)


        for i in range(0, 7):

            if i == 6: # если итерация последняя
                # жмем на выбор заведения(маленький треугольничек)
                WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located((By.XPATH, "//mat-select[@role='listbox']")))[1].click()
                time.sleep(2)
                # список заведений
                list_companies = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
                    (By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']")))
                list_companies[0].click()  # жмем на Все

            else:
                # жмем на выбор заведения(маленький треугольничек)
                WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located((By.XPATH, "//mat-select[@role='listbox']")))[1].click()
                time.sleep(2)
                # список заведений
                list_companies = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']")))
                list_companies[randint(0,len(list_companies)-1)].click() # выбирете любой индекс из спсика

                time.sleep(2)
        #
        # #driver.refresh()  # перезагужае  страницу
        #
        # time.sleep(2)
        # for i in range(0, 3):
        #     # жмем на выбор города
        #     WebDriverWait(driver, 10).until(
        #         ec.presence_of_all_elements_located((By.XPATH, "//mat-select[@role='listbox']")))[0].click()
        #     time.sleep(2)
        #     # список городов
        #     list_towns = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']")))
        #     list_towns[randint(0,len(list_towns)-1)].click() # выбирете любой индекс из спсика
        #
        #     time.sleep(2)
        #
        #     for j in range(0, 4):
        #         # жмем на выбор заведения
        #         WebDriverWait(driver, 10).until(
        #             ec.presence_of_all_elements_located((By.XPATH, "//mat-select[@role='listbox']")))[1].click()
        #         time.sleep(2)
        #         # список заведений
        #         list_companies = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
        #             (By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']")))
        #         list_companies[randint(0, len(list_companies) - 1)].click()  # выбирете любой индекс из спсика
        #
        #         time.sleep(2)
        #
        # driver.refresh()  # перезагужае  страницу
        #
        # self.sortirovka(driver)# вызов метода сортировки

        # for i in range(0, 3):
        #         time.sleep(2)
        #         # Жмем на первую дату
        #         WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,  "//input[@placeholder='От']"))).click()
        #         time.sleep(2)
        #
        #         list_from_date = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
        #                      (By.XPATH,  "//td[@class='mat-calendar-body-cell ng-star-inserted']")))# спсиок дат От
        #
        #         list_from_date[randint(0, len(list_from_date)-1)].click() # бере рандомный индекс даты(начала)
        #         time.sleep(2)
        #
        #
        #
        #
        #         # Жмем на вторую дату
        #         WebDriverWait(driver, 10).until(
        #             ec.presence_of_element_located((By.XPATH, "//input[@placeholder='До']"))).click()
        #         time.sleep(2)
        #
        #         list_to_date = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
        #             (By.XPATH, "//td[@class='mat-calendar-body-cell ng-star-inserted']")))# список дат До
        #
        #
        #         list_to_date[randint(0, len(list_to_date) - 1)].click()  # бере рандомный индекс даты(конца)
        #
        # time.sleep(5)



    def tear_down(self):
        time.sleep(5)
        #self.driver.quit()
        self.driver.close() #  закрываем браузер
        # pass


if __name__ == "__main__":
    unittest.main()