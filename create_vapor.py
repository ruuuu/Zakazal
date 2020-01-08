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

# не долно быть паров  вобще у  завдения
class create_vapor(unittest.TestCase):


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






    def setUp(self):
        self.driver = webdriver.Chrome()

        #self.driver.set_window_position(0, 0)  # устанавливает позицию левого верзнего угла окна браузера
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



    def authorization(self, driver):

        driver.get("https://admin.preorder.technaxis.com/external/login")

        time.sleep(2)  # чтобы сразу окно не закрывалось
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='login']"))).send_keys(
            "istambul@gmail.com")

        time.sleep(2)
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='password']"))).send_keys("password")

        time.sleep(2)

        # кнопка Войти
        WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//button[@type='button']")))[
            1].click()




    def edit_vapor(self, driver): # меод редактирвоания

        # жмем на кнпоку редактирвоания
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located(
                (By.XPATH, "//button[@class='mat-icon-button mat-accent ng-star-inserted']")))[
            0].click()

        time.sleep(2)

        # поле Навзание:
        name = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH,
                                            "//input[@formcontrolname='name']")))

        name.clear()  # очищвем поле

        name.send_keys(self.my_metho_randem_stroka(randint(4, 7), randint(2, 5)))  # заполеняем поле

        time.sleep(2)

        description = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH,
                                            "//input[@formcontrolname='description']")))

        description.clear()  # очищвем поле

        description.send_keys(self.my_metho_randem_stroka(randint(4, 7), randint(2, 5)))  # заполеняем поле

        time.sleep(2)

        price = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH,
                                            "//input[@formcontrolname='price']")))

        price.clear()  # очищвем поле

        price.send_keys(self.my_metho_randem_stroka(randint(1, 9000)))  # заполеняем поле

        time.sleep(2)

        discountPrice = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH,
                                            "//input[@formcontrolname='discountPrice']")))

        discountPrice.clear()  # очищвем поле

        discountPrice.send_keys(self.my_metho_randem_stroka(randint(1, 9000)))  # заполеняем поле

        time.sleep(2)



    def test_create_vapor_method_(self):  # главный метод, надо чтобы он начинался  с test_

        driver = self.driver
        self.authorization(driver) # вызов метода авторизации
        time.sleep(2)


        #  в  меню выбираем ПАр
        try: # попытаемся нажаить на пунк меню Пар если он есть
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,  "//a[@href='/place/hookah']"))).click()


        except: # если его нет, то в профил поставит чекбокс на пар

            WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//mat-expansion-panel-header[@role='button']")))[2].click()
            time.sleep(2)
            WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//mat-checkbox[@color='primary']")))[0].click() # жмем Чек бокс Пар
            time.sleep(2)
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='mat-button mat-flat-button']"))).click() # кнопка Сохранить
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='mat-button mat-primary fullWidth mat-flat-button']"))).click() #  в поппапе нажимем Сохранить

            time.sleep(2)

            WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//a[@href='/place/hookah']"))).click() # жмем на пункт пар

            time.sleep(2)

        # жмем на галочку верхнюю Часы для скидок меню
        #WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//button[@class='arrow-btn mat-icon-button mat-accent']")))[0].click()

        #time.sleep(2)




        #
        # for i in range(0, 2):  #   # цикл по дням
        #
        #     WebDriverWait(driver, 10).until(
        #         ec.presence_of_all_elements_located((By.XPATH, "//div[@class='uz-form-field']")))[i].click()#переключаем тогглер
        #     time.sleep(2)
        #
        #
        #
        #
        #     # заоплняем Начало
        #     WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//mat-select[@formcontrolname='startTime']")))[i].click()
        #
        #     time.sleep(2)
        #
        #     # выбирам рандомный тайминг:
        #     # список таймингов Начала
        #     list_timings1 = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']")))
        #
        #
        #     list_timings1[randint(0, len(list_timings1)-1)].click()#  кликаем рандомный тайминг начала
        #
        #
        #     # заполняем Конец:
        #     WebDriverWait(driver, 10).until(
        #         ec.presence_of_all_elements_located((By.XPATH, "//mat-select[@formcontrolname='endTime']")))[i].click()
        #     time.sleep(2)
        #
        #     # спсиок таймингов конца
        #     list_timings2 = WebDriverWait(driver, 10).until(
        #         ec.presence_of_all_elements_located((By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']")))
        #
        #     list_timings2[randint(0, len(list_timings2) - 1)].click()  # кликаем раномный тайминг конца
        #     time.sleep(2)
        #
        #
        #
        # WebDriverWait(driver, 10).until(
        #                 ec.presence_of_element_located((By.XPATH,
        #     "//button[@class='mat-button mat-primary fullWidth mat-flat-button']"))).click() # кнопка Сохранить
        #
        time.sleep(7)

        # жмем кнопку Доавить паровой коктель
        WebDriverWait(driver, 10).until(
                 ec.presence_of_element_located((By.XPATH,
                "//*[@id='portal-classic-content']/app-hookah/div/div/mat-card/mat-card-content/app-hookah-menu/div/div[2]/button"))).click()

        #WebDriverWait(driver, 10).until(
                #ec.presence_of_element_located((By.XPATH, "//button[@class='mat-button mat-primary']"))).click() # жмем кнопку Доавить паровой коктель


        time.sleep(2)
        # # поле Навзание:
        # name = WebDriverWait(driver, 10).until(
        #        ec.presence_of_element_located((By.XPATH,
        #                                        "//input[@formcontrolname='name']")))
        #
        #
        #
        # name.send_keys(self.my_metho_randem_stroka(randint(4, 7), randint(2, 5)))  # заполеняем поле
        #
        # time.sleep(2)
        #
        # description = WebDriverWait(driver, 10).until(
        #        ec.presence_of_element_located((By.XPATH,
        #                                        "//input[@formcontrolname='description']")))
        #
        #
        #
        # description.send_keys(self.my_metho_randem_stroka(randint(4, 7), randint(2, 5)))  # заполеняем поле
        #
        # time.sleep(2)
        #
        # price = WebDriverWait(driver, 10).until(
        #        ec.presence_of_element_located((By.XPATH,
        #                                        "//input[@formcontrolname='price']")))
        #
        #
        #
        # price.send_keys(randint(1, 9000))  # заполеняем поле
        #
        # time.sleep(2)
        #
        # discountPrice = WebDriverWait(driver, 10).until(
        #        ec.presence_of_element_located((By.XPATH,
        #                                        "//input[@formcontrolname='discountPrice']")))
        #


        #discountPrice.send_keys(randint(1, 9000))  # заполеняем поле

        time.sleep(2)

        #k = randint(1, 5) #  генерим количество паров
        #print("count vapor equal k", k)

        #  заполняем первое поле Пары:
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//input[@role='combobox']")))[0].send_keys(self.my_metho_randem_stroka(randint(3, 10), randint(3, 5)))



        #for i in range(1, 4): #  было до  k Заполянем Пары i=0,4

        time.sleep(2)

        # оранжевая кнопкка Добавить
        WebDriverWait(driver, 10).until(
                        ec.presence_of_all_elements_located((By.XPATH, "//mat-icon[@class='mat-icon notranslate material-icons mat-icon-no-color']")))[1].click()



        # Поле Пар
        WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located((By.XPATH, "//input[@role='combobox']")))[1].send_keys(
                    self.my_metho_randem_stroka(randint(3, 10), randint(3, 5)))
        time.sleep(1)

        # оранжевая кнопкка Добавить
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located(
                (By.XPATH, "//mat-icon[@class='mat-icon notranslate material-icons mat-icon-no-color']")))[
            1].click()

        time.sleep(1)

        # Поле Пар
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//input[@role='combobox']")))[2].send_keys(
            self.my_metho_randem_stroka(randint(3, 10), randint(3, 5)))

        time.sleep(1)

        # оранжевая кнопкка Добавить
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located(
                (By.XPATH, "//mat-icon[@class='mat-icon notranslate material-icons mat-icon-no-color']")))[
            1].click()

        time.sleep(1)

        # Поле Пар
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//input[@role='combobox']")))[3].send_keys(
            self.my_metho_randem_stroka(randint(3, 10), randint(3, 5)))

        time.sleep(1)



        # # жмем чекбоксы крепости:
        # index_pred_checkox = 0
        # for i in range(0, randint(1, 5)):
        #
        #             rand_ind_checkox = randint(0, 4)
        #
        #             WebDriverWait(driver, 10).until(
        #                 ec.presence_of_all_elements_located((By.XPATH, "//mat-checkbox[@color='primary']")))[
        #                 rand_ind_checkox].click()
        #             time.sleep(1)
        #
        #             if rand_ind_checkox == index_pred_checkox:
        #                 WebDriverWait(driver, 10).until(
        #                     ec.presence_of_all_elements_located((By.XPATH, "//mat-checkbox[@color='primary']")))[rand_ind_checkox].click()
        #
        #             index_pred_checkox = rand_ind_checkox
        #

# ----------------------------------------------
#         pred_ind = 0  # будет хранить индекс  чекбокса нажатого на предыдущей итерации
#         for i in range(0, 5):
#             rand_ind_quisin = randint(2, 9)
#
#             list_cuizins[
#                 rand_ind_quisin].click()  # выбрает рандомный элемент  из списка с индексом от 2 до 9 вклбчительно
#             time.sleep(1)
#             if rand_ind_quisin == pred_ind:  # если индекс  на текущей итерации совпаддает с индекосм на продешой итерации
#                 list_cuizins[rand_ind_quisin].click()
#             time.sleep(1)
#             pred_ind = rand_ind_quisin
# -------------------------------------

        # m = randint(k + 1, k + 3) # геннерим количетсов вкусов
        # print("count tastes  equal m", m)
        #
        # # заоплняем первое поле Вкус:
        # WebDriverWait(driver, 10).until(
        #     ec.presence_of_all_elements_located((By.XPATH, "//input[@role='combobox']")))[k].send_keys(
        #     self.my_metho_randem_stroka(randint(3, 10), randint(3, 5)))
        #
        # for j in range(k+1, m):# Заполняем вкусы
        #         # поле Вкус
        #        WebDriverWait(driver, 10).until(
        #            ec.presence_of_all_elements_located((By.XPATH, "//input[@role='combobox']")))[j].send_keys(
        #            self.my_metho_randem_stroka(randint(3, 10), randint(3, 5)))
        #
        #        time.sleep(1)
        #
        #        #WebDriverWait(driver, 10).until(
        #                 #ec.presence_of_all_elements_located((By.XPATH, "//mat-icon[@class='mat-icon notranslate material-icons mat-icon-no-color']")))[2].click()  # кнопкка Добавить
        #        WebDriverWait(driver, 10).until(
        #                         ec.presence_of_element_located((By.XPATH, "//*[@id='portal-classic-content']/app-hookah/div/div/mat-card/mat-card-content/app-hookah-menu/div/div/div[2]/mat-card/app-edit-hookah/form/div[4]/app-form-list/div[2]/button"))).click()# кнопккаоранжевая   Добавить
        #
        # time.sleep(2)
        #
        #
        # count_trachs = k + 2

        # выбирает раномную корзину и удалет ее
        WebDriverWait(driver, 10).until(
                   ec.presence_of_all_elements_located((By.XPATH,  "//button[@class='remove-btn mat-icon-button mat-accent']" )))[randint(0, (k+2-1))].click()

        time.sleep(1)

        # кнопка Сохранить
        WebDriverWait(driver, 10).until(
                   ec.presence_of_element_located((By.XPATH, "//button[@type='undefined']"))).click()




        time.sleep(6)



    def tear_down(self):
        time.sleep(5)

        self.driver.close()
        #self.driver.quit()
        # pass


if __name__ == "__main__":
    unittest.main()