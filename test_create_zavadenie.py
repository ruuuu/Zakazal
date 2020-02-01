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

class create_zavadenie(unittest.TestCase):


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
                           '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] # добавить символы !,  ? , *, %, #, $, ~

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



        time.sleep(2)  # чтобы сразу окно не закрывалось
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='login']"))).send_keys(
            "admin@ujezakazal.ru")

        time.sleep(2)
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='password']"))).send_keys("password")

        time.sleep(2)

        # кнопка Войти
        WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//button[@type='button']")))[
            1].click()



    def setUp(self):
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver')  #Firefox()

        #self.driver.set_window_position(0, 0)  # устанавливает позицию левого верзнего угла окна браузера
        self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна, в сафари не работет


        #self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()
        self.driver.get("https://admin.preorder.technaxis.com/external/login")

        self.list_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                                'R', 'S',
                                'T', 'U', 'W', 'X', 'Y', 'Z',
                                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'k', 'm', 'n', 'o', 'p', 'q',
                                'r', 's',
                                't', 'u', 'w', 'x', 'y', 'z', 'A'
                                ' ']  # поле



    def test_create_zavedenie_method_(self):  # главный метод, надо чтобы он начинался  с test_

        driver = self.driver
        self.authorization(driver)

        time.sleep(3)

        #кнпока Добавить заведение:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='header-action-button mat-flat-button mat-primary ng-star-inserted']"))).click()

        time.sleep(5)

        # #  жмемна спсиок выбора города:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//div[@class='mat-select-value']"))).click()


        time.sleep(1)
        # список городов:
        list_cities =  WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']")))

        # выбираем рандомный город и жмем на него
        WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']")))[randint(0, len(list_cities) - 1)].click() #1
        time.sleep(1)

        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='managerFullName']"))).send_keys(self.my_metho_randem_stroka(randint(4,7),3) )

        time.sleep(1)

        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Идентификатор магазина']"))).send_keys("ujezakazal")



        time.sleep(1)

        file_dicitionary = {0: "/Users/rufina/Desktop/dishs/salute.jpg",
                            1: "/Users/rufina/Desktop/dishs/Restaurant-desember-news-07-696x522.jpg", 2: "/Users/rufina/Desktop/dishs/bd33ed99edcb4638b5750bc45add91cd.JPG",
                            3: "/Users/rufina/Desktop/dishs/salat_kinoa.jpg__1499258543__50030.jpg",
                            4: "/Users/rufina/Desktop/dishs/527_768x764_80f.jpg", 5: "/Users/rufina/Desktop/dishs/salat-gril-300x300.jpg",
                            6: "/Users/rufina/Desktop/dishs/1505752856_1.jpeg",
                            7: "/Users/rufina/Desktop/dishs/450x300 (1).jpeg",
                            8:"/Users/rufina/Desktop/dishs/205_geraldine_posta-magazine.jpg",
                            9:"/Users/rufina/Desktop/dishs/305794452_b.jpg",
                            10:"/Users/rufina/Desktop/dishs/205_geraldine_posta-magazine.jpg",
                            11:"/Users/rufina/Desktop/dishs/caption (2).jpg",
                            12:"/Users/rufina/Desktop/dishs/orig (1).jpeg",
                            13:"/Users/rufina/Desktop/dishs/salat1.jpg",
                            14:"/Users/rufina/Desktop/dishs/orig.jpeg"}






        WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//input[@type='file']")))[0].send_keys(file_dicitionary[randint(0, len(file_dicitionary) - 1)])

        time.sleep(1)

        # # название заведения
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='companyName']"))).send_keys(self.my_metho_randem_stroka(randint(4, 7), 3))

        time.sleep(1)

        #  ФИО представителя завденеия
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='representativeFullName']"))).send_keys(
            self.my_metho_randem_stroka(randint(4, 7), 3))

        time.sleep(1)

        # номер телефона
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='phone']"))).send_keys(self.generation_tel_phone())# генерит номер телефона

        time.sleep(1)

        # доп. номер телефона
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='administratorPhone']"))).send_keys(self.generation_tel_phone())

        time.sleep(1)

        #  поле Емейл
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH,  "//input[@formcontrolname='email']"))).send_keys(self.my_metho_randem_stroka_for_email(randint(3, 7), 1))

        time.sleep(1)

        # поле Пароль
        password_8 = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='password']"))).send_keys("password") # self.my_metho_randem_stroka(randint(7, 12), 1)

        time.sleep(1)
        #print(password_8.text)


        # # полправить здесь:
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='dPassword']"))).send_keys("password")

        time.sleep(1)

        # поле Адрес
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Адрес']"))).send_keys("Ямашева")

        time.sleep(1)

        for i in range(0,3):
            WebDriverWait(driver, 10).until(                                                        #Keys.DOWN + Keys.ENTER
                ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Адрес']"))).send_keys(Keys.DOWN) # сперва нажимает на  Keys.DOWN потом на  Keys.ENTER
            time.sleep(2)

        Keys.ENTER
        time.sleep(1)



        #чекбоксы Формат заведения(пАр, бизнес -ланчи)
        rand_index = randint(0, 1) #   выберет рандомно Пар(0) или Бизнес-ланчи(1)
        print("rand_index_of_format_zavedenia", rand_index) # рандомный индекс формата завеения

            #if rand_index == 1: # если выбрал Бизнес ланч
                #rand_index -= 1

        format_checkbox  = WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//mat-checkbox[@color='primary']")))[rand_index] #

        driver.execute_script("arguments[0].scrollIntoView(true);", format_checkbox) # скроллим  к этому чекбоксу

        time.sleep(1)
        format_checkbox.click()
        time.sleep(1)


        if rand_index == 0: # если нажали на Пар

           #   выбираем ранломный индекс радиобаннттона (Pro /Standart)
            WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH,
                                                     "//mat-radio-button[@class='mat-radio-button mat-primary ng-star-inserted']")))[randint(0, 1)].click()

        else: # если rand_index ==1 , то есть нажали на  Бизнес-ланчи

            k = randint(0, 2)  # k=2   включительно (Обычное Наборное Комбо)
            print('index equal toggler type meny k=', k)

            WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH,
                                                     "//mat-radio-button[@class='mat-radio-button mat-primary ng-star-inserted']")))[k].click()  # выбираем ранломный индекс радиобаннттона Обычное Наборное Комбо

            time.sleep(1)
            #  выбираем ранломный индекс радиобаннттона (Pro /Standart)

            print("select Pro /Standart:" )
            WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH,
                    "//mat-radio-button[@class='mat-radio-button mat-primary ng-star-inserted']")))[randint(1, 2)].click()

            print("selected Pro /Standart:")

        # тип Кухня: спсиок кухонь
        list_cuizins = WebDriverWait(driver, 10).until(
              ec.presence_of_all_elements_located((By.XPATH, "//mat-checkbox[@color='primary']")))

        pred_ind = 0 #  будет хранить индекс  чекбокса нажатого на предыдущей итерации
        for i in range(0, 5):
            rand_ind_quisin = randint(2, 9)

            list_cuizins[rand_ind_quisin].click() # выбрает рандомный элемент  из списка с индексом от 2 до 9 вклбчительно
            time.sleep(1)
            if rand_ind_quisin == pred_ind:# если индекс  на текущей итерации совпаддает с индекосм на продешой итерации
                list_cuizins[rand_ind_quisin].click()
            time.sleep(1)
            pred_ind = rand_ind_quisin


        time.sleep(1)

        # Дополнительно
        list_cuizins[randint(10, 11)].click()# выбрает рандомный элемент  из списка с индексом от 10 до 11 вклбчительно

        time.sleep(1)





        time.sleep(2)

        predy = 0#  будет хранить индекс  чекбокса нажатого на предыдущей итерации
        for i in range(0, 4):
            rand_ind_sposob_oplaty = randint(12, 15)

            print("rand_ind_sposob_oplaty equal", rand_ind_sposob_oplaty )
            list_cuizins[rand_ind_sposob_oplaty].click() # выбирает рандомный чекбокс Способ оплаты
            time.sleep(1)
            if rand_ind_sposob_oplaty == predy: # если индекс  на текущей итерации совпаддает с индекосм на продешой итерации
                list_cuizins[rand_ind_sposob_oplaty].click()

            time.sleep(1)
            predy = rand_ind_sposob_oplaty


        # Процент сервису
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Процент сервису (%)']"))).send_keys(randint(0, 10))
        time.sleep(1)

        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Процент банку (%)']"))).send_keys(
            randint(0, 10))
        time.sleep(1)

        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Процент пользователю на бонусы (%)']"))).send_keys(
            randint(0, 10))
        time.sleep(1)





        if rand_index ==1: # если выбрали  Бизнес-ланчи
            # Заполнение графика работы
            for i in range(0, 4):


                # список тогглеров:
                WebDriverWait(driver, 10).until(
                                     ec.presence_of_all_elements_located((By.XPATH, "//div[@class='mat-slide-toggle-thumb']")))[i].click()

                #if toggler.is_selected():# если  i-ый тогглер включен
                    #toggler.click() # нажимаем еще раз  на этот же  тогглер


                #toggler.click()
                WebDriverWait(driver, 10).until(
                                            ec.presence_of_all_elements_located((By.XPATH, "//div[@class='mat-select-arrow']")))[4*i+1].click() # нажимаем на маленький треугольничек Открывается
                time.sleep(1)


                # спсик таймингов Открытия
                list_timings_open = WebDriverWait(driver, 10).until(
                                         ec.presence_of_all_elements_located((By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']")))

                list_timings_open[randint(0, len(list_timings_open)-1)].click() # выбираем  рандомный тайминг из списка и кликаем
                time.sleep(1)


                WebDriverWait(driver, 10).until(
                                             ec.presence_of_all_elements_located((By.XPATH, "//div[@class='mat-select-arrow']")))[4*i+2].click()  # нажимаем на малеонки треугольничек  Закывается
                time.sleep(1)

                list_timings_close = WebDriverWait(driver, 10).until(
                            ec.presence_of_all_elements_located((By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']")))# спсиок таймингов закрытия

                list_timings_close[
                            randint(0, len(list_timings_close) - 1)].click()  # выбираем  рандомный тайминг из списка и кликаем

                time.sleep(1)



                WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located((By.XPATH, "//div[@class='mat-select-arrow']")))[4 * i + 3].click()  # нажимаем на маленький треугольничек Открывается
                time.sleep(1)

                # спсик таймингов Открытия
                list_timings_open = WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located(
                        (By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']")))

                list_timings_open[
                    randint(0, len(list_timings_open) - 1)].click()  # выбираем  рандомный тайминг из списка и кликаем
                time.sleep(1)

                WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located((By.XPATH, "//div[@class='mat-select-arrow']")))[4 * i + 4].click()  # нажимаем на малеонки треугольничек  Закывается
                time.sleep(1)

                list_timings_close = WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located(
                        (By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']")))  # спсиок таймингов закрытия

                list_timings_close[
                    randint(0, len(list_timings_close) - 1)].click()  # выбираем  рандомный тайминг из списка и кликаем

                time.sleep(1)


        else: # если выбраи Пар

            # Заолнение графика работы
            for i in range(0, 4):
                # список тогглеров:
                WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located((By.XPATH, "//div[@class='mat-slide-toggle-thumb']")))[
                    i].click()

                # if toggler.is_selected():# если  i-ый тогглер включен
                # toggler.click() # нажимаем еще раз  на этот же  тогглер

                # toggler.click()
                WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located((By.XPATH, "//div[@class='mat-select-arrow']")))[2 * i + 1].click()  # нажимаем на маленький треугольничек Открывается
                time.sleep(2)

                # спсик таймингов Открытия
                list_timings_open = WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located(
                        (By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']")))

                list_timings_open[
                    randint(0, len(list_timings_open) - 1)].click()  # выбираем  рандомный тайминг из списка и кликаем
                time.sleep(2)

                WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located((By.XPATH, "//div[@class='mat-select-arrow']")))[2 * i + 2].click()  # нажимаем на малеонки треугольничек  Закывается
                time.sleep(2)

                list_timings_close = WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located(
                        (By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']")))  # спсиок таймингов закрытия

                try:  # если элемент в спсике всего один, попытаеся на него нажать
                    WebDriverWait(driver, 10).until(
                        ec.presence_of_element_located(
                            (By.XPATH, "//mat-option[@class='mat-option ng-star-inserted mat-active']"))).click()
                except:  # если  не один, то выберет любой
                    list_timings_close[randint(0, len(list_timings_close) - 1)].click()  # выбираем  рандомный тайминг из списка и кликаем

                time.sleep(2)



        # краткое описание
        short_description = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//textarea[@formcontrolname='description']")))

        driver.execute_script("arguments[0].scrollIntoView(true);", short_description)  # скроллим  к этому заведению
        time.sleep(2)

        short_description.send_keys(self.my_metho_with_predlojenie(1, randint(1, 10), randint(5, 10)))


        time.sleep(2)





        WebDriverWait(driver, 10).until(
             ec.presence_of_all_elements_located((By.XPATH, "//input[@type='file']")))[0].send_keys(file_dicitionary[randint(0, len(file_dicitionary) - 1)])

        time.sleep(2)

        for i in range(0, 9):# грузим фото опционально
            WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//input[@type='file']")))[0].send_keys(file_dicitionary[randint(0, len(file_dicitionary) - 1)])
            time.sleep(1)





        # клик по тогглеру Опубликовать заведение
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//div[@class='mat-slide-toggle-thumb']")))[7].click()

        time.sleep(2)

        # кнопка Добавить
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='mat-button mat-flat-button']"))).click()


        time.sleep(15)



    def tear_down(self):
        time.sleep(10)
        self.driver.quit()
        #self.driver.close() #  закрываем браузер
        # pass


if __name__ == "__main__":
    unittest.main()
