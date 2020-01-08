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

class create_promotion(unittest.TestCase):


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
            "superadmin@mail.ru")

        time.sleep(2)
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='password']"))).send_keys("password")

        time.sleep(2)

        WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//button[@type='button']")))[
            1].click()

        time.sleep(5)


    def poisk(self, driver):# поиск по названию акции

        # поле по названию
        search_field = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Поиск по названию']")))

        # список названий акций
        list_names_of_promotions = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//div[@class='name']")))



        for i in range(0, 6):
            search_field.send_keys(
                list_names_of_promotions[randint(0, len(list_names_of_promotions) - 1)].text)  # берем любой  hall и иполучаем его название
            time.sleep(2)

            driver.refresh()# перезагружаем страницу









    def setUp(self):
        self.driver = webdriver.Chrome()

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



    def test_create_promotion_method_(self):  # главный метод, надо чтобы он начинался  с test_

        driver = self.driver
        self.authorizatuion(driver) # меода автризвация


        #жмем  в меню на Акцию:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//a[@href='/superadmin/promotions']"))).click()

        time.sleep(2)

        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,"//button[@class='header-action-button mat-flat-button mat-primary ng-star-inserted']"))).click() # копка Добавить
        time.sleep(2)


        file_dicitionary = {0: "/Users/rufina/Desktop/dishs/BjJ6inaYiWam0GGViLFHLQ-double.jpg",
                            1: "/Users/rufina/Desktop/dishs/4Rve51WmWfk.jpg", 2: "/Users/rufina/Desktop/dishs/2531.jpg",
                            3: "/Users/rufina/Desktop/dishs/salat_kinoa.jpg__1499258543__50030.jpg",
                            4: "/Users/rufina/Desktop/dishs/4703.jpg", 5: "/Users/rufina/Desktop/dishs/caption (1).jpg"}

        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys(file_dicitionary[randint(0, len(file_dicitionary) - 1)])
        time.sleep(2)

        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Название акции']"))).send_keys(self.my_metho_randem_stroka(randint(4, 7), 3))
        time.sleep(2)

        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//div[@data-placeholder ='Текст акции...']"))).send_keys(self.my_metho_randem_stroka(randint(5,10), randint(3, 5)))
        time.sleep(2)

        # выбиоаем дату начала действия акции:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@placeholder='От']"))).click()
        time.sleep(2)

        # спсиок дат начала
        list_dates_from = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//td[@class='mat-calendar-body-cell ng-star-inserted']")))

        list_dates_from[randint(0, len(list_dates_from )-1)].click()

        time.sleep(2)

        # выбиоаем дату конца действия акции:
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@placeholder='До']"))).click()
        time.sleep(2)

        # спсиок дат конца
        list_dates_to = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//td[@class='mat-calendar-body-cell ng-star-inserted']")))

        list_dates_to[randint(0, len(list_dates_to) - 1)].click()

        time.sleep(2)

        # кнопка Добаить
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='mat-button mat-flat-button']"))).click()

        time.sleep(2)

        # стрелка Назад
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='back-btn mat-icon-button ng-star-inserted']"))).click()

        time.sleep(2)
        self.poisk(driver)# вызов метода поиска



        time.sleep(5)



    def tear_down(self):
        time.sleep(5)
        self.driver.quit()
        #self.driver.close() #  закрываем браузер
        # pass


if __name__ == "__main__":
    unittest.main()