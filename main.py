from PyQt5 import QtWidgets
from random import randint
from ql2 import Ui_MainWindow
import sys
import time
from exept import some_func, some_func_2, some_func_3
from loguru import logger
logger.add("h1.txt", format="{time} {level} {message}", level="DEBUG")

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.ui.pushButton.clicked.connect(self.run)



    def calculation_1(self,item):
        i = 0
        count = 0
        for c in item:
            if i % 2 == 0 and i != 0:
                count = count + c
            i = i + 1
        out = 'Сумма элементов,имеющих нечетные индексы:' + str(count) + '\n'
        return out



    def calculation_2(self,item,chek_elem):
        i = 0
        elem_allchek = 0
        for c in item:
            if c > chek_elem and c % 5 == 0:
                elem_allchek = elem_allchek + 1
        if elem_allchek > 0:
            out = 'Количество элементов массива, значение которых больше ' + str(
                chek_elem) + ' и они кратны 5:' + str(elem_allchek) + '\n'
        else:
            out = 'Количество элементов массива, значение которых больше ' + str(
                chek_elem) + ' и они кратны 5: Таких чисел нет' + '\n'
        return out

    def calculatiun_3(self,item):
        i = 1
        chek = True
        for c in item:
            if c < 0:
                lk = -(c)
                if c < 0 and lk % 5 == 2:
                    chek = False
                    out = 'Номер первого отрицательного элемента, делящегося на 5 с остатком 2: ' + str(
                        i) + '\n'
                    break
            i = i + 1
        if chek:
            out = 'Номер первого отрицательного элемента, делящегося на 5 с остатком 2: Таких чисел нет' + '\n'
        return out

    def run(self):
        chek_elem = self.ui.textEdit.toPlainText()
        try:
            some_func(chek_elem)
        except Exception:
            self.ui.messegbox.setText('Пустая строка или в строке пробел')
            self.ui.messegbox.exec()
            logger.opt(exception=True).debug("Exception logged with debug level:")
            return
        for natural_number in chek_elem:
            try:
                some_func(natural_number)
            except Exception:
                self.ui.messegbox.setText('Пустая строка или в строке пробел')
                self.ui.messegbox.exec()
                logger.opt(exception=True).debug("Exception logged with debug level:")
                return
            for count in natural_number:
                try:
                    some_func_2(count)
                except Exception:
                    self.ui.messegbox.setText('Введите число!')
                    self.ui.messegbox.exec()
                    logger.opt(exception=True).debug("Exception logged with debug level:")
                    return
        chek_elem = int(chek_elem)
        if self.ui.radioButton.isChecked():
            item = [lineEdit.text() for lineEdit in self.findChildren(QtWidgets.QLineEdit)]
            for natural_number in item:
                try:
                    some_func(natural_number)
                except Exception:
                    self.ui.messegbox.setText('Пустая строка или в строке пробел')
                    self.ui.messegbox.exec()
                    logger.opt(exception=True).debug("Exception logged with debug level:")
                    return
                for count in natural_number:
                    try:
                        some_func_2(count)
                    except Exception:
                        self.ui.messegbox.setText('Введите число!')
                        self.ui.messegbox.exec()
                        logger.opt(exception=True).debug("Exception logged with debug level:")
                        return
            i = 0
            for c in item:
                item[i] = int(c)
                i = i + 1
            from multiprocessing.pool import ThreadPool
            pool = ThreadPool(processes=3)
            async_result = pool.apply_async(self.calculation_1, (item,))
            async_result_2 = pool.apply_async(self.calculation_2, (item, chek_elem))
            async_result_3 = pool.apply_async(self.calculatiun_3, (item,))
            out = async_result.get() + async_result_2.get() + async_result_3.get()
            self.ui.textBrowser.setText(out)




        elif self.ui.radioButton_2.isChecked():
            item = []
            for lineEdit in self.findChildren(QtWidgets.QLineEdit):
                i = randint(-5000,5000)
                lineEdit.setText(str(i))
                item.append(i)
            if self.ui.checkBox.isChecked():

                from multiprocessing.pool import ThreadPool
                pool = ThreadPool(processes=3)
                tic_1 = time.perf_counter()
                async_result = pool.apply_async(self.calculation_1, (item,))
                async_result_2 = pool.apply_async(self.calculation_2,(item,chek_elem))
                async_result_3 = pool.apply_async(self.calculatiun_3,(item,))
                out = async_result.get() + async_result_2.get() + async_result_3.get()
                tic_2 = time.perf_counter()
                out = out + 'Время выполнения многопоточной части кода: ' + str(tic_2 - tic_1) + '\n'
                self.ui.textBrowser.setText(out)
                tic_1 = time.perf_counter()
                out = out + self.calculation_1(item)
                out = out + self.calculation_2(item, chek_elem)
                out = out + self.calculatiun_3(item)
                tic_2 = time.perf_counter()
                out = out + 'Время выполнения без многопоточности: ' + str(tic_2 - tic_1) + '\n'
                self.ui.textBrowser.setText(out)

            else:
                from multiprocessing.pool import ThreadPool
                pool = ThreadPool(processes=3)
                async_result = pool.apply_async(self.calculation_1, (item,))
                async_result_2 = pool.apply_async(self.calculation_2, (item, chek_elem))
                async_result_3 = pool.apply_async(self.calculatiun_3, (item,))
                out = async_result.get() + async_result_2.get() + async_result_3.get()
                self.ui.textBrowser.setText(out)




        elif self.ui.radioButton_3.isChecked():
            sleep = self.ui.textEdit_2.toPlainText()
            try:
                some_func(sleep)
            except Exception:
                self.ui.messegbox.setText('Пустая строка или в строке пробел')
                self.ui.messegbox.exec()
                logger.opt(exception=True).debug("Exception logged with debug level:")
                return
            for natural_number in sleep:
                try:
                    some_func(natural_number)
                except Exception:
                    self.ui.messegbox.setText('Пустая строка или в строке пробел')
                    self.ui.messegbox.exec()
                    logger.opt(exception=True).debug("Exception logged with debug level:")
                    return
                for count in natural_number:
                    try:
                        some_func_2(count)
                    except Exception:
                        self.ui.messegbox.setText('Введите число!')
                        self.ui.messegbox.exec()
                        logger.opt(exception=True).debug("Exception logged with debug level:")
                        return
            sleep = int(sleep)
            item = []
            for lineEdit in self.findChildren(QtWidgets.QLineEdit):
                i = randint(-5000, 5000)
                time.sleep(sleep/100)
                lineEdit.setText(str(i))
                item.append(i)

            from multiprocessing.pool import ThreadPool
            pool = ThreadPool(processes=3)
            async_result = pool.apply_async(self.calculation_1, (item,))
            async_result_2 = pool.apply_async(self.calculation_2, (item, chek_elem))
            async_result_3 = pool.apply_async(self.calculatiun_3, (item,))
            out = async_result.get() + async_result_2.get() + async_result_3.get()
            self.ui.textBrowser.setText(out)

        else:
            try:
                some_func_3()
            except Exception:
                logger.opt(exception=True).debug("Exception logged with debug level:")
                return
            self.ui.messegbox.setText('Выберите режим')
            self.ui.messegbox.exec()


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
