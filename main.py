import tkinter as tk
from tkinter import ttk


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        self.add_img = tk.PhotoImage(file="add2.gif")
        btn_open_dialog = tk.Button(command=self.open_dialog, image=self.add_img)
        btn_open_dialog.pack(side=tk.TOP)
        self.razbavlenie_img = tk.PhotoImage(file="razbavlenie.gif")
        btn_open_dialog = tk.Button(command=self.open_dialog2, image=self.razbavlenie_img)
        btn_open_dialog.pack(side=tk.TOP)
        self.smecspirta_img = tk.PhotoImage(file="smecspirta.gif")
        btn_open_dialog = tk.Button(command=self.open_dialog3, image=self.smecspirta_img)
        btn_open_dialog.pack(side=tk.TOP)

        self.braga_img = tk.PhotoImage(file="Braga.gif")
        btn_open_dialog = tk.Button(command=self.open_dialog4, image=self.braga_img)
        btn_open_dialog.pack(side=tk.TOP)

        self.rasnapitok_img = tk.PhotoImage(file="rasnapitok.gif")
        btn_open_dialog = tk.Button(command=self.open_dialog5, image=self.rasnapitok_img)
        btn_open_dialog.pack(side=tk.TOP)

        self.drobnaya_img = tk.PhotoImage(file="drobnaya.gif")
        btn_open_dialog = tk.Button(command=self.open_dialog6, image=self.drobnaya_img)
        btn_open_dialog.pack(side=tk.TOP)

        # but_lst = ['razbavlenie.img', 'add2.gif']
        # i = int(0)
        # for item in but_lst:
        #     but = tk.Button(root, image=item, width=10)
        #     but.pack()
        #     i += 1

    def open_dialog(self):
        Child()

    def open_dialog2(self):
        Child2()

    def open_dialog3(self):
        Child3()

    def open_dialog4(self):
        Child4()

    def open_dialog5(self):
        Child5()

    def open_dialog6(self):
        Child6()


class Child2(tk.Toplevel):
    """ Разбавление водой спирта"""

    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        self.title('Куркулятор')
        self.geometry('301x175+400+300')
        self.resizable(False, False)
        lebel_lst = ['Объем продукта(л):', 'Начальная крепость(%):', 'Необходимая крепость(%):']
        i = int(0)
        for item in lebel_lst:
            self.leb = ttk.Label(self, width='26', text=item)
            self.leb.grid(row=i, sticky=tk.W)
            i += 1
        self.lab4 = ttk.Label(self, text='Необходимый объем воды').grid(row=4, sticky=tk.W)
        self.lab5 = ttk.Label(self, text='Общий объем продукта').grid(row=6, sticky=tk.W)
        # self.lab6 = ttk.Label(self, text='Данные результаты актуальны и'
        #                                  ' верны при температуре компонентов равной 20°С.').grid(row=8)

        self.entry_amount = ttk.Entry(self, width=7, font='Arial 16')  # Обьем продукта в литрах
        self.entry_amount.grid(row=0, column=1, sticky=tk.E)
        self.entry_initial = ttk.Entry(self, width=7, font='Arial 16')  # Началья крепость
        self.entry_initial.grid(row=1, column=1, sticky=tk.E)
        self.entry_krepost = ttk.Entry(self, width=7, font='Arial 16')  # Необходимая крепость
        self.entry_krepost.grid(row=2, column=1, sticky=tk.E)
        self.entry_water = ttk.Entry(self, width=7, font='Arial 16')  # Необходимый объем воды
        self.entry_water.grid(row=4, column=1, sticky=tk.E)
        self.entry_gotamount = ttk.Entry(self, width=7, font='Arial 16')  # Общий обьем продукта
        self.entry_gotamount.grid(row=6, column=1, sticky=tk.E)

        def proizvedenie():
            entry_amount = self.entry_amount.get()
            entry_amount = float(entry_amount)  # * 1000  # Обьем продукта в миллилитрах
            initial = self.entry_initial.get()
            initial = float(initial)  # Началья крепость
            krepost = self.entry_krepost.get()
            krepost = float(krepost)  # Необходимая крепость
            # X = Р * (N / M - 1) x = entry_water, P = entry_amount,
            kol_water = entry_amount * (initial / krepost - 1)  # / 1000
            kol_water = round(kol_water, 3)
            rezult_voda = str(kol_water)  # необходимый объем воды
            got_amount = entry_amount + kol_water
            got_amount = round(got_amount, 3)
            result_amount = str(got_amount)  # Общий обьем продукта

            self.entry_water.delete(0, tk.END)  # очищаем текстовое поле
            self.entry_gotamount.delete(0, tk.END)  # очищаем текстовое поле полностью
            self.entry_water.insert(0, rezult_voda)  # вставляем результат в начало
            self.entry_gotamount.insert(0, result_amount)
            # Данные результаты актуальны и верны при температуре компонентов равной 20°С.

        self.but = ttk.Button(self, text='Рассчитать объем воды', command=proizvedenie)
        self.but.grid(row=3, column=1, sticky=tk.E)

        self.grab_set()
        self.focus_set()


class Child(tk.Toplevel):
    """ Рассчеты собестоимость литра самогона"""

    def __init__(self):
        super().__init__(root)
        self.init_child2()

    def init_child2(self):
        self.title('Куркулятор')
        self.geometry('327x210+400+300')
        self.resizable(False, False)

        self.EntryWater = ttk.Entry(self, width=7, font='Arial 16')
        self.EntryWater.grid(row=0, column=1, sticky=tk.E)
        # self.EntryWater = ttk.Entry(self, width=7, font='Arial 14').place(x=240, y=0)
        self.EntryElectricity = ttk.Entry(self, width=7, font='Arial 16')
        self.EntryElectricity.grid(row=1, column=1, sticky=tk.E)
        self.EntrySugar = ttk.Entry(self, width=7, font='Arial 16')
        self.EntrySugar.grid(row=2, column=1, sticky=tk.E)
        self.EntryYeast = ttk.Entry(self, width=7, font='Arial 16')
        self.EntryYeast.grid(row=3, column=1, sticky=tk.E)
        self.EntryTincture = ttk.Entry(self, width=7, font='Arial 16')
        self.EntryTincture.grid(row=4, column=1, sticky=tk.E)
        self.EntryAlcohol_output = ttk.Entry(self, width=7, font='Arial 16')
        self.EntryAlcohol_output.grid(row=5, column=1, sticky=tk.E)
        self.EntryC = ttk.Entry(self, width=10, font='Arial 16')
        self.EntryC.grid(row=6, columnspan=1, sticky=tk.W)

        # первая метка в строке 0, столбце 0 (0 по умолчанию)
        # парамет sticky  означает выравнивание. W, E,N,S — запад, восток, север, юг
        lebel_lst = ['Потрачено м.кв воды', 'Потрачено электроэнергии', 'Кг сахара', 'Цена дрожжей', 'Цена настойки',
                     'Выход литров']
        i = int(0)
        for item in lebel_lst:
            self.leb = ttk.Label(self, width='26', text=item)
            self.leb.grid(row=i, sticky=tk.W)
            i += 1

        # переменные для расчетов
        # bentonit = 25  # рублей уходит на 2 перегонки, 8 литров сэма
        ugoly = 20  # рублей уходит на 2 перегонки, 8 литров сэма
        voda_zacub = 23.09  # цена за кубометр воды
        cvet_kilovat = 3.67  # цена за киловатт

        def proizv():
            water = self.EntryWater.get()  # берем текст из первого поля
            water = float(water) * voda_zacub  # преобразуем в число дробного типа типа
            electricity = self.EntryElectricity.get()
            electricity = float(electricity) * cvet_kilovat
            sugar = self.EntrySugar.get()
            sugar = float(sugar) * 95
            yeast = self.EntryYeast.get()
            yeast = float(yeast)
            tincture = self.EntryTincture.get()
            tincture = float(tincture)
            alcohol_output = self.EntryAlcohol_output.get()
            alcohol_output = float(alcohol_output)
            sena_za_litr = ((water + electricity + sugar + yeast + tincture + ugoly) / alcohol_output)
            sena_za_litr = round(sena_za_litr, 2)
            result = str(sena_za_litr)  # результат переведем в строку для
            # дальнейшего вывода
            self.EntryC.delete(0, tk.END)  # очищаем текстовое поле полностью
            self.EntryC.insert(0, result)  # вставляем результат в начало

        # размещаем кнопку в строке 3 во втором столбце
        self.but = ttk.Button(self, text='Рассчитать стоимость литра', command=proizv)
        self.but.grid(row=6, column=1, sticky=tk.E)

        self.grab_set()
        self.focus_set()


class Child3(tk.Toplevel):
    """ Класс для расчета смешивания спитров"""

    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        self.title('Куркулятор')
        self.geometry('345x210+400+300')
        self.resizable(False, False)
        lebel_lst = ['Объем жидкости 1 (л):', 'Крепость жидкости 1 (%):', 'Объем жидкости 2 (л):', 'Крепость жидкости '
                                                                                                   '2(%)']
        i = int(0)
        for item in lebel_lst:
            self.leb = ttk.Label(self, width='26', text=item)
            self.leb.grid(row=i, sticky=tk.W)
            i += 1
        self.lab4 = ttk.Label(self, text='Крепость напитка после смешивания:').grid(row=5, sticky=tk.W)
        self.lab5 = ttk.Label(self, text='Общий объем продукта (л)').grid(row=6, sticky=tk.W)
        # self.lab6 = ttk.Label(self, text='Данные результаты актуальны и'
        #                                  ' верны при температуре компонентов равной 20°С.').grid(row=8)

        self.entry_amount1 = ttk.Entry(self, width=7, font='Arial 16')  # Обьем продукта 1 в литрах
        self.entry_amount1.grid(row=0, column=1, sticky=tk.E)
        self.initial1 = ttk.Entry(self, width=7, font='Arial 16')  # Крепость жидкости 1
        self.initial1.grid(row=1, column=1, sticky=tk.E)
        self.entry_amount2 = ttk.Entry(self, width=7, font='Arial 16')  # Обьем продукта 1 в литрах
        self.entry_amount2.grid(row=2, column=1, sticky=tk.E)
        self.initial2 = ttk.Entry(self, width=7, font='Arial 16')  # Крепость жидкости 2
        self.initial2.grid(row=3, column=1, sticky=tk.E)
        self.smesinitial = ttk.Entry(self, width=7, font='Arial 16')  # Крепость после смешивания
        self.smesinitial.grid(row=5, column=1, sticky=tk.E)
        self.entry_gotamount = ttk.Entry(self, width=7, font='Arial 16')  # Общий обьем продукта
        self.entry_gotamount.grid(row=6, column=1, sticky=tk.E)

        def proizvedenie():
            """ Формула смешивания спиртосодержащих жидкостей, X = (A*B + C*D) / A+C ; X-Крепость напитка после смешивания,
             A-Объем жидкасти 1, B-Крепость напитка 1 C-Объем жидкасти 2, D-Крепость напитка 2"""
            entry_amount1 = self.entry_amount1.get()
            entry_amount1 = float(entry_amount1)  # * 1000  # Обьем продукта 1 в литрах
            initial1 = self.initial1.get()
            initial1 = float(initial1)  # Крепость жидкости 1
            entry_amount2 = self.entry_amount2.get()
            entry_amount2 = float(entry_amount2)  # * 1000  # Обьем продукта 2 в литрах
            initial2 = self.initial2.get()
            initial2 = float(initial2)  # Крепость жидкости 2

            initialprod = (entry_amount1 * initial1 + entry_amount2 * initial2) / (entry_amount1 + entry_amount2)  #
            # расчет по формуле
            initialprod = round(initialprod, 1)
            rezult_initial = str(initialprod)  # результат в стр
            amount_litr = (entry_amount1 + entry_amount2) / 100 * 99.5
            amount_litr = round(amount_litr, 3)
            result_amount = str(amount_litr)

            self.smesinitial.delete(0, tk.END)  # очищаем текстовое поле
            self.entry_gotamount.delete(0, tk.END)  # очищаем текстовое поле полностью
            self.smesinitial.insert(0, rezult_initial)  # вставляем результат в начало
            self.entry_gotamount.insert(0, result_amount)
            # Данные результаты актуальны и верны при температуре компонентов равной 20°С.

        self.but = ttk.Button(self, text='Рассчитать', width=20, command=proizvedenie)
        self.but.grid(row=4, column=1, sticky=tk.E)

        self.grab_set()
        self.focus_set()


class Child4(tk.Toplevel):
    """ Калькулятор расчета сахарной браги"""

    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        self.title('Куркулятор')
        self.geometry('363x145+400+300')
        self.resizable(False, False)

        lebel_lst = ['Вес сахара (кг):', 'Объем смеси (сахар + вода):']
        i = int(0)
        for item in lebel_lst:
            self.leb = ttk.Label(self, width='26', text=item)
            self.leb.grid(row=i, sticky=tk.W)
            i += 1
        self.lab4 = ttk.Label(self, text='Максимальная расчетная спиртуозность:').grid(row=3, sticky=tk.W)
        self.lab5 = ttk.Label(self, text='Необходимое количество воды (л)').grid(row=4, sticky=tk.W)

        self.entry_braga = ttk.Entry(self, width=7, font='Arial 16')  # Вес сахара
        self.entry_braga.grid(row=0, column=1, sticky=tk.E)
        self.volime_smesy = ttk.Entry(self, width=7, font='Arial 16')  # Объем смеси сахар + вода
        self.volime_smesy.grid(row=1, column=1, sticky=tk.E)
        self.initialmax = ttk.Entry(self, width=7, font='Arial 16')  # Вывод максимальной спиртуозности
        self.initialmax.grid(row=3, column=1, sticky=tk.E)
        self.volime_prod = ttk.Entry(self, width=7, font='Arial 16')  # Необходимое количество воды
        self.volime_prod.grid(row=4, column=1, sticky=tk.E)

        def proizvedenie():
            """ Формула смешивания спиртосодержащих жидкостей, X = (A*B + C*D) / A+C ; X-Крепость напитка после смешивания,
             A-Объем жидкасти 1, B-Крепость напитка 1 C-Объем жидкасти 2, D-Крепость напитка 2"""
            pass
            # entry_amount1 = self.entry_amount1.get()
            # entry_amount1 = float(entry_amount1)  # * 1000  # Обьем продукта 1 в литрах
            # initial1 = self.initial1.get()
            # initial1 = float(initial1)  # Крепость жидкости 1
            # entry_amount2 = self.entry_amount2.get()
            # entry_amount2 = float(entry_amount2)  # * 1000  # Обьем продукта 2 в литрах
            # initial2 = self.initial2.get()
            # initial2 = float(initial2)  # Крепость жидкости 2
            #
            # initialprod = (entry_amount1 * initial1 + entry_amount2 * initial2) / (entry_amount1 + entry_amount2)  #
            # # расчет по формуле
            # initialprod = round(initialprod, 1)
            # rezult_initial = str(initialprod)  # результат в стр
            # amount_litr = (entry_amount1 + entry_amount2) / 100 * 99.5
            # amount_litr = round(amount_litr, 3)
            # result_amount = str(amount_litr)
            #
            # self.smesinitial.delete(0, tk.END)  # очищаем текстовое поле
            # self.entry_gotamount.delete(0, tk.END)  # очищаем текстовое поле полностью
            # self.smesinitial.insert(0, rezult_initial)  # вставляем результат в начало
            # self.entry_gotamount.insert(0, result_amount)
            # # Данные результаты актуальны и верны при температуре компонентов равной 20°С.

        self.but = ttk.Button(self, text='Рассчитать', width=20, command=proizvedenie)
        self.but.grid(row=2, column=1, sticky=tk.E)


class Child5(tk.Toplevel):
    """ Расчет количества воды для разбавления спирта до нужного объема напитка"""

    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        self.title('Куркулятор')
        self.geometry('279x175+400+300')
        self.resizable(False, False)

        lebel_lst = ['Начальная крепость(%):', 'Конечная крепость(%):', 'Желаемый объем(л):']
        i = int(0)
        for item in lebel_lst:
            self.leb = ttk.Label(self, width='26', text=item)
            self.leb.grid(row=i, sticky=tk.W)
            i += 1
        self.lab4 = ttk.Label(self, text='Объем исходного продукта (л):').grid(row=4, sticky=tk.W)
        self.lab5 = ttk.Label(self, text='Объем воды для разбавления (л):').grid(row=6, sticky=tk.W)
        # self.lab6 = ttk.Label(self, text='Данные результаты актуальны и'
        #                                  ' верны при температуре компонентов равной 20°С.').grid(row=8)

        self.entry_amount = ttk.Entry(self, width=7, font='Arial 16')  # Обьем продукта в литрах
        self.entry_amount.grid(row=0, column=1, sticky=tk.E)
        self.entry_initial = ttk.Entry(self, width=7, font='Arial 16')  # Началья крепость
        self.entry_initial.grid(row=1, column=1, sticky=tk.E)
        self.entry_krepost = ttk.Entry(self, width=7, font='Arial 16')  # Необходимая крепость
        self.entry_krepost.grid(row=2, column=1, sticky=tk.E)
        self.entry_water = ttk.Entry(self, width=7, font='Arial 16')  # Необходимый объем воды
        self.entry_water.grid(row=4, column=1, sticky=tk.E)
        self.entry_gotamount = ttk.Entry(self, width=7, font='Arial 16')  # Общий обьем продукта
        self.entry_gotamount.grid(row=6, column=1, sticky=tk.E)

        def proizvedenie():
            entry_amount = self.entry_amount.get()
            entry_amount = float(entry_amount)  # * 1000  # Обьем продукта в миллилитрах
            initial = self.entry_initial.get()
            initial = float(initial)  # Началья крепость
            krepost = self.entry_krepost.get()
            krepost = float(krepost)  # Необходимая крепость
            # X = Р * (N / M - 1) x = entry_water, P = entry_amount,
            kol_water = entry_amount * (initial / krepost - 1)  # / 1000
            kol_water = round(kol_water, 3)
            rezult_voda = str(kol_water)  # необходимый объем воды
            got_amount = entry_amount + kol_water
            got_amount = round(got_amount, 3)
            result_amount = str(got_amount)  # Общий обьем продукта

            self.entry_water.delete(0, tk.END)  # очищаем текстовое поле
            self.entry_gotamount.delete(0, tk.END)  # очищаем текстовое поле полностью
            self.entry_water.insert(0, rezult_voda)  # вставляем результат в начало
            self.entry_gotamount.insert(0, result_amount)
            # Данные результаты актуальны и верны при температуре компонентов равной 20°С.

        self.but = ttk.Button(self, text='Рассчитать', command=proizvedenie)
        self.but.grid(row=3, column=1, sticky=tk.E)

        self.grab_set()
        self.focus_set()


class Child6(tk.Toplevel):
    """ Расчет чистого спирта и отбора голов"""

    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        self.title('Куркулятор')
        self.geometry('278x265+400+300')
        self.resizable(False, False)

        lebel_lst = ['Спирт-сырец(л):', 'Крепость сырца(%):', 'Крепость на выходе(%):', 'Отбор голов(%)']
        i = int(0)
        for item in lebel_lst:
            self.leb = ttk.Label(self, width='26', text=item)
            self.leb.grid(row=i, sticky=tk.W)
            i += 1
        self.lab4 = ttk.Label(self, text='Общий объем спирта:').grid(row=5, sticky=tk.W)
        self.lab5 = ttk.Label(self, text='Голов(л):').grid(row=6, sticky=tk.W)
        self.lab6 = ttk.Label(self, text='Тело(л):').grid(row=7, sticky=tk.W)
        self.lab7 = ttk.Label(self, text='Хвостов(л):').grid(row=8, sticky=tk.W)
        # self.lab6 = ttk.Label(self, text='Данные результаты актуальны и'
        #                                  ' верны при температуре компонентов равной 20°С.').grid(row=8)

        self.entry_amount = ttk.Entry(self, width=7, font='Arial 16')  # Обьем продукта в литрах
        self.entry_amount.grid(row=0, column=1, sticky=tk.E)
        self.entry_initial = ttk.Entry(self, width=7, font='Arial 16')  # Началья крепость
        self.entry_initial.grid(row=1, column=1, sticky=tk.E)
        self.entry_krepost = ttk.Entry(self, width=7, font='Arial 16')  # Необходимая крепость
        self.entry_krepost.grid(row=2, column=1, sticky=tk.E)
        self.entry_water = ttk.Entry(self, width=7, font='Arial 16')  # Необходимый объем воды
        self.entry_water.grid(row=3, column=1, sticky=tk.E)
        self.entry_gotamount = ttk.Entry(self, width=7, font='Arial 16')  # Общий обьем продукта
        self.entry_gotamount.grid(row=5, column=1, sticky=tk.E)
        self.entry_gotamount = ttk.Entry(self, width=7, font='Arial 16')  # Общий обьем продукта
        self.entry_gotamount.grid(row=6, column=1, sticky=tk.E)
        self.entry_gotamount = ttk.Entry(self, width=7, font='Arial 16')  # Общий обьем продукта
        self.entry_gotamount.grid(row=7, column=1, sticky=tk.E)
        self.entry_gotamount = ttk.Entry(self, width=7, font='Arial 16')  # Общий обьем продукта
        self.entry_gotamount.grid(row=8, column=1, sticky=tk.E)

        def proizvedenie():
            entry_amount = self.entry_amount.get()
            entry_amount = float(entry_amount)  # * 1000  # Обьем продукта в миллилитрах
            initial = self.entry_initial.get()
            initial = float(initial)  # Началья крепость
            krepost = self.entry_krepost.get()
            krepost = float(krepost)  # Необходимая крепость
            # X = Р * (N / M - 1) x = entry_water, P = entry_amount,
            kol_water = entry_amount * (initial / krepost - 1)  # / 1000
            kol_water = round(kol_water, 3)
            rezult_voda = str(kol_water)  # необходимый объем воды
            got_amount = entry_amount + kol_water
            got_amount = round(got_amount, 3)
            result_amount = str(got_amount)  # Общий обьем продукта

            self.entry_water.delete(0, tk.END)  # очищаем текстовое поле
            self.entry_gotamount.delete(0, tk.END)  # очищаем текстовое поле полностью
            self.entry_water.insert(0, rezult_voda)  # вставляем результат в начало
            self.entry_gotamount.insert(0, result_amount)
            # Данные результаты актуальны и верны при температуре компонентов равной 20°С.

        # self.but = ttk.Button(self, text='Рассчитать', width=18, command=proizvedenie)
        style = ttk.Style()
        style.configure("C.TButton", background="#FF4500")

        style.map("C.TButton",
                  foreground=[('pressed', 'blue'), ('active', '#FF4500')],
                  background=[('pressed', '!disabled', 'red'), ('active', 'black')], )

        self.but = ttk.Button(self, text="Расчитать", width=18, command=proizvedenie, style="C.TButton")
        self.but.grid(row=4, column=1, sticky=tk.E)

        self.grab_set()
        self.focus_set()


if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Калькуляторы Самогонщика")
    root.geometry("650x276+300+200")
    root.iconbitmap(r'icon1.ico')
    root.resizable(False, False)
    root.mainloop()
