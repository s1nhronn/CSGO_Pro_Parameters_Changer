# coding=windows-1251
"""
Основной файл
"""
import configparser
import ctypes
import locale
import math
import os
import sys
import time
from threading import Thread
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QDialog, QTableWidgetItem, QAction, QFileDialog, \
    QListWidget, QLineEdit, QPushButton, QLabel, QProgressBar, QScrollArea, QTableWidget
from PyQt5.QtWidgets import QMessageBox, QListWidgetItem
import functions as fn
import variables

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)

start = configparser.ConfigParser()
start.read('start.ini')
if start['Statuses']['first_launch'] == 'True':
    cfg = open('start.ini', 'w')
    start.set('Statuses', 'first_launch', 'False')
    start.write(cfg)
    cfg.close()

    locale.getlocale()
    windll = ctypes.windll.kernel32
    if locale.windows_locale[windll.GetUserDefaultUILanguage()] == 'ru_RU':
        cfg = open('start.ini', 'w')
        start.set('Language', 'language', 'ru')
        start.write(cfg)
        cfg.close()
        language = 'ru'
    else:
        cfg = open('start.ini', 'w')
        start.set('Language', 'language', 'en')
        start.write(cfg)
        cfg.close()
        language = 'en'
else:
    language = start['Language']['language']

config_now = start['Config']['config']


class MainWindow(QMainWindow):
    """
    Главное окно с таблицей оружий
    """

    # noinspection PyUnresolvedReferences
    def __init__(self):
        self.default_items_game_list = []
        self.items_game_list = []
        self.add_weapon_button = QPushButton()
        self.scrollArea = QScrollArea()
        self.return_button = QPushButton()
        self.build_button = QPushButton()
        self.weapons_list = QTableWidget()
        self.reset_weapon_button = QPushButton()
        self.rename_button = QPushButton()
        self.delete_button = QPushButton()
        global config_now
        super().__init__()
        if language == 'en':
            uic.loadUi(fn.path() + '/UI/Main Window.ui', self)
        else:
            uic.loadUi(fn.path() + '/UI/Main Window ru.ui', self)

        self.all_weapons = []

        self.all_names = []

        self.isPushButton = False

        russian_icon = QIcon(fn.path() + '/icons/russia.png')
        english_icon = QIcon(fn.path() + '/icons/united-kingdom.png')
        download_icon = QIcon(fn.path() + '/icons/download.png')
        new_config_icon = QIcon(fn.path() + '/icons/new_config.png')
        rename_icon = QIcon(fn.path() + '/icons/rename.png')
        config_icon = QIcon(fn.path() + '/icons/config_2.png')

        if language == 'en':
            choose_config = QAction('&Load configuration from device', self)
            choose_config.setIcon(download_icon)
            choose_config.triggered.connect(self.choose_config)

            create_config = QAction('&Create configuration', self)
            create_config.setIcon(new_config_icon)
            create_config.triggered.connect(self.prepare_to_share)

            choose_table = QAction('&Select loaded configuration', self)
            choose_table.setIcon(config_icon)
            choose_table.triggered.connect(self.load_table)

            rename_config = QAction('&Rename active configuration', self)
            rename_config.setIcon(rename_icon)
            rename_config.triggered.connect(self.rename_active_config)

            change_language = QAction('Change to Russian language', self)
            change_language.setIcon(russian_icon)
            change_language.triggered.connect(self.change_language)

            self.menubar = self.menuBar()
            config_menu = self.menubar.addMenu('&Config')
            language_menu = self.menubar.addMenu('&Language')
        else:
            choose_config = QAction('&Загрузить конфигурацию с устройства', self)
            choose_config.setIcon(download_icon)
            choose_config.triggered.connect(self.choose_config)

            create_config = QAction('&Создать конфигурацию', self)
            create_config.setIcon(new_config_icon)
            create_config.triggered.connect(self.prepare_to_share)

            choose_table = QAction('&Выбрать загруженную конфигурацию', self)
            choose_table.setIcon(config_icon)
            choose_table.triggered.connect(self.load_table)

            rename_config = QAction('&Переименовать активную конфигурацию', self)
            rename_config.setIcon(rename_icon)
            rename_config.triggered.connect(self.rename_active_config)

            change_language = QAction('Сменить язык на английский', self)
            change_language.setIcon(english_icon)
            change_language.triggered.connect(self.change_language)

            self.menubar = self.menuBar()
            config_menu = self.menubar.addMenu('&Конфигурация')
            language_menu = self.menubar.addMenu('&Язык')
        config_menu.addAction(choose_config)
        config_menu.addAction(create_config)
        config_menu.addAction(choose_table)
        config_menu.addAction(rename_config)
        language_menu.addAction(change_language)

        self.path = fn.path()
        folder = self.path[:self.path.rfind('/')] + '/csgo/scripts/items/items_game.txt'
        file_1 = open(folder, 'r+')
        file_2 = open(fn.path() + '/defaults/default_items_game.txt')
        if file_1.readlines() != file_2.readlines():
            self.return_button.setEnabled(True)
        file_1.close()
        file_2.close()

        for j in range(fn.get_length_table(config_now)):
            weapon = fn.get_table_parameters(config_now, j)
            weapon_type = weapon[0]
            weapon = weapon[1:]
            self.all_weapons.append(weapon_type)
            self.weapons_list.insertRow(j)
            weapon_name = weapon[0]
            self.all_names.append(weapon_name)
            weapon = weapon[1:]
            for i in range(len(weapon)):
                self.weapons_list.setItem(j, i, QTableWidgetItem(str(weapon[i])))
            self.weapons_list.setVerticalHeaderItem(j, QTableWidgetItem(weapon_name))
            self.weapons_list.verticalHeaderItem(j).setText(weapon_name)
            self.weapons_list.verticalHeaderItem(j).setToolTip(weapon_type)
            if weapon_type != 'Automatic "Galil"':
                self.weapons_list.verticalHeaderItem(j).setIcon(QIcon(fn.path() + f'/icons/{weapon_type}.png'))
            else:
                self.weapons_list.verticalHeaderItem(j).setIcon(QIcon(fn.path() + '/icons/Automatic Galil.png'))

        self.scrollArea.setWidgetResizable(True)

        self.build_button.clicked.connect(self.build)

        self.add_weapon_button.clicked.connect(self.add_new_weapon)

        self.weapons_list.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.weapons_list.horizontalHeader().setMinimumSectionSize(0)

        self.description_en = variables.description_en

        self.description_ru = variables.description_ru

        if language == 'en':
            for i in range(len(self.description_en)):
                self.weapons_list.horizontalHeaderItem(i).setToolTip(self.description_en[i])
        else:
            for i in range(len(self.description_ru)):
                self.weapons_list.horizontalHeaderItem(i).setToolTip(self.description_ru[i])

        self.weapons_list.itemSelectionChanged.connect(self.click)

        self.return_button.clicked.connect(self.return_all)

        self.delete_button.clicked.connect(self.delete)

        self.rename_button.clicked.connect(self.rename)

        self.reset_weapon_button.clicked.connect(self.reset_weapon_parameters)

    def keyPressEvent(self, event) -> None:
        """
        Обработчик горячих клавиш
        :param event: То, что вызвало функцию
        """
        items = self.weapons_list.selectedItems()
        if int(event.modifiers()) == Qt.CTRL:
            if event.key() == Qt.Key_S:
                self.build()
            elif event.key() == Qt.Key_A:
                self.add_new_weapon()
            elif event.key() == Qt.Key_Z:
                self.return_all()
        elif event.key() == Qt.Key_Delete and len(items) == 40 and len(set(index.row() for index in
                                                                           self.weapons_list.selectedIndexes())) == 1:
            self.delete()

    # noinspection PyUnresolvedReferences
    def reload(self, old=''):
        """
        Функция, пересоздающая интерфейс
        """
        global config_now
        global language
        if not old:
            for j in range(self.weapons_list.rowCount()):
                parameters = {}
                for i in range(self.weapons_list.columnCount()):
                    parameters[self.weapons_list.horizontalHeaderItem(i).text().lower()] = (
                        self.weapons_list.item(j, i).text())
                fn.set_parameters(self.all_weapons[j], self.weapons_list,
                                  name=self.weapons_list.verticalHeaderItem(j).text(),
                                  parameters=parameters, config_name=config_now)
        else:
            for j in range(self.weapons_list.rowCount()):
                parameters = {}
                for i in range(self.weapons_list.columnCount()):
                    parameters[self.weapons_list.horizontalHeaderItem(i).text().lower()] = (
                        self.weapons_list.item(j, i).text())
                fn.set_parameters(self.all_weapons[j], self.weapons_list,
                                  name=self.weapons_list.verticalHeaderItem(j).text(),
                                  parameters=parameters, config_name=old)
        if language == 'en':
            uic.loadUi(fn.path() + '/UI/Main Window.ui', self)
        else:
            uic.loadUi(fn.path() + '/UI/Main Window ru.ui', self)

        self.all_weapons = []

        self.all_names = []

        self.isPushButton = False

        self.menubar.clear()

        russian_icon = QIcon(fn.path() + '/icons/russia.png')
        english_icon = QIcon(fn.path() + '/icons/united-kingdom.png')
        download_icon = QIcon(fn.path() + '/icons/download.png')
        new_config_icon = QIcon(fn.path() + '/icons/new_config.png')
        rename_icon = QIcon(fn.path() + '/icons/rename.png')
        config_icon = QIcon(fn.path() + '/icons/config_2.png')

        if language == 'en':
            choose_config = QAction('&Load configuration from device', self)
            choose_config.setIcon(download_icon)
            choose_config.triggered.connect(self.choose_config)

            create_config = QAction('&Create configuration', self)
            create_config.setIcon(new_config_icon)
            create_config.triggered.connect(self.prepare_to_share)

            choose_table = QAction('&Select loaded configuration', self)
            choose_table.setIcon(config_icon)
            choose_table.triggered.connect(self.load_table)

            rename_config = QAction('&Rename active configuration', self)
            rename_config.setIcon(rename_icon)
            rename_config.triggered.connect(self.rename_active_config)

            change_language = QAction('Change to Russian language', self)
            change_language.setIcon(russian_icon)
            change_language.triggered.connect(self.change_language)

            self.menubar = self.menuBar()
            config_menu = self.menubar.addMenu('&Config')
            language_menu = self.menubar.addMenu('&Language')
        else:
            choose_config = QAction('&Загрузить конфигурацию с устройства', self)
            choose_config.setIcon(download_icon)
            choose_config.triggered.connect(self.choose_config)

            create_config = QAction('&Создать конфигурацию', self)
            create_config.setIcon(new_config_icon)
            create_config.triggered.connect(self.prepare_to_share)

            choose_table = QAction('&Выбрать загруженную конфигурацию', self)
            choose_table.setIcon(config_icon)
            choose_table.triggered.connect(self.load_table)

            rename_config = QAction('&Переименовать активную конфигурацию', self)
            rename_config.setIcon(rename_icon)
            rename_config.triggered.connect(self.rename_active_config)

            change_language = QAction('Сменить язык на английский', self)
            change_language.setIcon(english_icon)
            change_language.triggered.connect(self.change_language)

            self.menubar = self.menuBar()
            config_menu = self.menubar.addMenu('&Конфигурация')
            language_menu = self.menubar.addMenu('&Язык')
        config_menu.addAction(choose_config)
        config_menu.addAction(create_config)
        config_menu.addAction(choose_table)
        config_menu.addAction(rename_config)
        language_menu.addAction(change_language)

        self.path = fn.path()
        folder = self.path[:self.path.rfind('/')] + '/csgo/scripts/items/items_game.txt'
        file_1 = open(folder, 'r+')
        file_2 = open(fn.path() + '/defaults/default_items_game.txt')
        if file_1.readlines() != file_2.readlines():
            self.return_button.setEnabled(True)
        file_1.close()
        file_2.close()
        for j in range(fn.get_length_table(config_now)):
            weapon = fn.get_table_parameters(config_now, j)
            weapon_type = weapon[0]
            weapon = weapon[1:]
            self.all_weapons.append(weapon_type)
            self.weapons_list.insertRow(j)
            weapon_name = weapon[0]
            self.all_names.append(weapon_name)
            weapon = weapon[1:]
            for i in range(len(weapon)):
                self.weapons_list.setItem(j, i, QTableWidgetItem(str(weapon[i])))
            self.weapons_list.setVerticalHeaderItem(j, QTableWidgetItem(weapon_name))
            self.weapons_list.verticalHeaderItem(j).setText(weapon_name)
            self.weapons_list.verticalHeaderItem(j).setToolTip(weapon_type)
            if weapon_type != 'Automatic "Galil"':
                self.weapons_list.verticalHeaderItem(j).setIcon(QIcon(fn.path() + f'/icons/{weapon_type}.png'))
            else:
                self.weapons_list.verticalHeaderItem(j).setIcon(QIcon(fn.path() + '/icons/Automatic Galil.png'))

        self.scrollArea.setWidgetResizable(True)

        items_game = open(folder, 'r+')
        default_items_game = open(fn.path() + '/defaults/default_items_game.txt')

        self.items_game_list = [elem.rstrip('\n') for elem in items_game.readlines()]
        self.default_items_game_list = [elem.rstrip('\n') for elem in default_items_game.readlines()]

        items_game.close()
        default_items_game.close()

        if self.items_game_list == self.default_items_game_list:
            self.return_button.setEnabled(False)

        self.build_button.clicked.connect(self.build)

        self.add_weapon_button.clicked.connect(self.add_new_weapon)

        self.weapons_list.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.weapons_list.horizontalHeader().setMinimumSectionSize(0)

        self.description_en = variables.description_en

        self.description_ru = variables.description_ru

        if language == 'en':
            for i in range(len(self.description_en)):
                self.weapons_list.horizontalHeaderItem(i).setToolTip(self.description_en[i])
        else:
            for i in range(len(self.description_ru)):
                self.weapons_list.horizontalHeaderItem(i).setToolTip(self.description_ru[i])

        self.weapons_list.itemSelectionChanged.connect(self.click)

        self.return_button.clicked.connect(self.return_all)

        self.delete_button.clicked.connect(self.delete)

        self.rename_button.clicked.connect(self.rename)

        self.reset_weapon_button.clicked.connect(self.reset_weapon_parameters)

    def change_language(self):
        """
        Функция для смены языка программы
        """
        global start
        global language

        if language == 'en':
            start_cfg = open('start.ini', 'w')
            start.set('Language', 'language', 'ru')
            start.write(start_cfg)
            start_cfg.close()
            language = 'ru'
            self.update()
            self.reload()
        else:
            start_cfg = open('start.ini', 'w')
            start.set('Language', 'language', 'en')
            start.write(start_cfg)
            start_cfg.close()
            language = 'en'
            self.update()
            self.reload()

    @staticmethod
    def load_table() -> None:
        """
        Выбор уже установленной конфигурации
        """
        tables = fn.get_all_tables()
        choice_table = ChoiceTable(tables)
        choice_table.exec_()

    def rename_active_config(self):
        """
        Функция для переименования активной конфигурации
        """
        global config_now
        global language
        if language == 'en':
            new_name, ok_pressed = QtWidgets.QInputDialog.getText(self,
                                                                  'Choosing a configuration name',
                                                                  'Configuration name:',
                                                                  QtWidgets.QLineEdit.Normal, config_now)
        else:
            new_name, ok_pressed = QtWidgets.QInputDialog.getText(self,
                                                                  'Назовите конфигурацию', 'Название конфигурации:',
                                                                  QtWidgets.QLineEdit.Normal, config_now)
        if ok_pressed:
            old = config_now
            if ' ' in new_name:
                new_name = '_'.join(new_name.split(' '))
            if new_name == '':
                new_name = config_now
            elif 'cs' + new_name in fn.get_all_tables():
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                if language == 'en':
                    msg.setText('There is already a configuration with the same name')
                    msg.setWindowTitle('Error')
                else:
                    msg.setText('Конфигурация с таким именем уже есть')
                    msg.setWindowTitle('Ошибка')
                msg.exec_()
                return
            config_now = new_name
            fn.rename_table(old, new_name)
            start_cfg = open('start.ini', 'w')
            start.set('Config', 'config', new_name)
            start.write(start_cfg)
            start_cfg.close()

    def prepare_to_share(self) -> None:
        """
        Функция для создания файла формата .ini для обмена конфигурацией с другими людьми.
        """
        global config_now
        global language
        if language == 'en':
            config_name, ok_pressed = QtWidgets.QInputDialog.getText(self,
                                                                     'Choosing a configuration name',
                                                                     'Configuration name:',
                                                                     QtWidgets.QLineEdit.Normal, config_now)
        else:
            config_name, ok_pressed = QtWidgets.QInputDialog.getText(self,
                                                                     'Назовите конфигурацию', 'Название конфигурации:',
                                                                     QtWidgets.QLineEdit.Normal, config_now)
        if ok_pressed:
            if config_name == '':
                config_name = config_now
            elif config_name in fn.get_all_tables():
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                if language == 'en':
                    msg.setText('There is already a configuration with the same name')
                    msg.setWindowTitle('Error')
                else:
                    msg.setText('Конфигурация с таким именем уже есть')
                    msg.setWindowTitle('Ошибка')
                msg.exec_()
                return
        else:
            return
        value = 0
        for j in range(self.weapons_list.rowCount()):
            parameters = {}
            for i in range(self.weapons_list.columnCount()):
                parameters[self.weapons_list.horizontalHeaderItem(i).text().lower()] = (
                    self.weapons_list.item(j, i).text())
            value += 40
            fn.set_parameters(self.all_weapons[j], self.weapons_list,
                              name=self.weapons_list.verticalHeaderItem(j).text(),
                              parameters=parameters, config_name=config_now)
        weapons = []
        for i in range(self.weapons_list.rowCount()):
            weapons.append(self.weapons_list.verticalHeaderItem(i).text().lower())
        if not weapons:
            return
        folder = self.path[:self.path.rfind('/')] + '/csgo/scripts/items/items_game.txt'
        file_1 = open(folder)
        file_2 = open(fn.path() + '/defaults/default_items_game.txt')
        if file_1.readlines() != file_2.readlines():
            self.return_button.setEnabled(True)
        else:
            self.return_button.setEnabled(False)
        file_1.close()
        file_2.close()
        cfgparser = configparser.ConfigParser()
        cfgparser.add_section('Guns')
        for i in range(fn.get_length_table(config_now)):
            params = list(fn.get_table_parameters(config_now, i))
            weapon_name = str(i + 1)
            params = ', '.join(params)
            cfgparser.set('Guns', weapon_name, params)
        with open(f'{config_name}.ini', 'w') as configfile:
            cfgparser.write(configfile)

    def choose_config(self) -> None:
        """
        Функция для выбора конфига на Вашем устройстве
        """
        global config_now
        if language == 'ru':
            filepath, _ = QFileDialog.getOpenFileName(self, 'Выбрать конфиг', '', filter='Конфиг (*.ini)')
        else:
            filepath, _ = QFileDialog.getOpenFileName(self, 'Choose config', '', filter='Config (*.ini)')
        another_config = configparser.ConfigParser()
        another_config.read(filepath)
        if not fn.get_filename(filepath):
            return
        elif fn.get_filename(filepath) == 'start':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            if language == 'en':
                msg.setText('This file cannot be used')
                msg.setWindowTitle('Error')
            else:
                msg.setText('Этот файл нельзя использовать')
                msg.setWindowTitle('Ошибка')
            msg.exec_()
            return
        config_now = '_'.join(fn.get_filename(filepath).split())
        start_cfg = open('start.ini', 'w')
        start.set('Config', 'config', '_'.join(fn.get_filename(filepath).split()))
        start.write(start_cfg)
        start_cfg.close()
        fn.create_config_table(config_now)
        fn.get_config_parameters(filepath)
        self.reload()

    def reset_weapon_parameters(self) -> None:
        """
        Возвращение параметров выбранного оружия до значений по умолчанию
        """
        index = self.weapons_list.currentRow()
        parameters = fn.get_default_parameters(self.all_weapons[index], self.weapons_list)
        headers = []
        for i in range(self.weapons_list.columnCount()):
            headers.append(self.weapons_list.horizontalHeaderItem(i).text().lower())
        lst = []
        if len(parameters) < len(headers):
            for i in headers:
                flag = False
                for j in parameters:
                    if i == j[0]:
                        flag = True
                if not flag:
                    lst.append(i)
        for i in range(len(headers)):
            if headers[i] in lst:
                if headers[i] == 'is full auto' or headers[i] == 'recoil angle' or headers[i] == 'recoil angle alt':
                    item = QTableWidgetItem('0')
                    self.weapons_list.setItem(index, i, item)
                elif headers[i] == 'bullets':
                    item = QTableWidgetItem('1')
                    self.weapons_list.setItem(index, i, item)
                elif headers[i] == 'cycletime':
                    item = QTableWidgetItem('0.100000')
                    self.weapons_list.setItem(index, i, item)
                self.update()
            else:
                try:
                    for sublist in range(len(parameters)):
                        if parameters[sublist][0] == headers[i]:
                            ind = sublist
                            item = QTableWidgetItem(parameters[ind][1])
                            self.weapons_list.setItem(index, i, item)
                            break
                    self.update()
                except IndexError:
                    break

    def rename(self) -> None:
        """
        Изменение названия выбранного оружия
        """
        index = self.weapons_list.currentRow()
        it = self.weapons_list.verticalHeaderItem(index)
        if language == 'en':
            new_header, ok_pressed = QtWidgets.QInputDialog.getText(self,
                                                                    'Choosing a weapon name', 'Weapon name:',
                                                                    QtWidgets.QLineEdit.Normal, self.all_names[index])
        else:
            new_header, ok_pressed = QtWidgets.QInputDialog.getText(self,
                                                                    'Назовите оружие', 'Название оружия:',
                                                                    QtWidgets.QLineEdit.Normal, self.all_names[index])
        if ok_pressed:
            if new_header == '':
                new_header = self.all_weapons[index]
            elif new_header in self.all_names:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                if language == 'en':
                    msg.setText('There is already a weapon with that name')
                    msg.setWindowTitle('Error')
                else:
                    msg.setText('Оружие с таким именем уже есть')
                    msg.setWindowTitle('Ошибка')
                msg.exec_()
                return
            self.all_names[index] = new_header
            it.setText(new_header)

    def build(self) -> None:
        """
        Функция, применяющая актуальную конфигурацию
        """
        load = Load()
        load.exec_()
        weapons = []
        for i in range(self.weapons_list.rowCount()):
            weapons.append(self.weapons_list.verticalHeaderItem(i).text().lower())
        if not weapons:
            return
        folder = self.path[:self.path.rfind('/')] + '/csgo/scripts/items/items_game.txt'
        file_1 = open(folder)
        file_2 = open(fn.path() + '/defaults/default_items_game.txt')
        if file_1.readlines() != file_2.readlines():
            self.return_button.setEnabled(True)
        else:
            self.return_button.setEnabled(False)
        file_1.close()
        file_2.close()

    def add_new_weapon(self) -> None:
        """
        Функция для добавления нового оружия в таблицу
        """
        add_weapon = AddWeapon()
        add_weapon.exec_()
        self.update()
        if self.isPushButton and self.all_weapons[-1] != '':
            row_position = self.weapons_list.rowCount()
            self.weapons_list.insertRow(row_position)
            index = self.weapons_list.rowCount() - 1
            it = self.weapons_list.verticalHeaderItem(index)
            if it is None:
                it = QtWidgets.QTableWidgetItem(str(self.all_weapons[-1]))
                self.weapons_list.setVerticalHeaderItem(index, it)
            if self.all_weapons[-1] != 'Automatic "Galil"':
                it.setIcon(QIcon(fn.path() + f'/icons/{self.all_weapons[-1]}.png'))
            else:
                it.setIcon(QIcon(fn.path() + '/icons/Automatic Galil.png'))
            if language == 'en':
                new_header, ok_pressed = QtWidgets.QInputDialog.getText(self,
                                                                        'Choosing a weapon name', 'Weapon name:',
                                                                        QtWidgets.QLineEdit.Normal,
                                                                        self.all_weapons[-1])
            else:
                new_header, ok_pressed = QtWidgets.QInputDialog.getText(self,
                                                                        'Назовите оружие', 'Название оружия:',
                                                                        QtWidgets.QLineEdit.Normal,
                                                                        self.all_weapons[-1])
            if ok_pressed:
                if new_header == '':
                    new_header = self.all_weapons[-1]
                elif new_header in self.all_names:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    if language == 'en':
                        msg.setText('There is already a weapon with that name')
                        msg.setWindowTitle('Error')
                    else:
                        msg.setText('Оружие с таким именем уже есть')
                        msg.setWindowTitle('Ошибка')
                    msg.exec_()
                    self.weapons_list.removeRow(index)
                    del self.all_weapons[-1]
                    self.isPushButton = False
                    return
                self.all_names.append(new_header)
                it.setText(new_header)
                self.weapons_list.verticalHeaderItem(index).setToolTip(self.all_weapons[-1])
                parameters = fn.get_default_parameters(self.all_weapons[-1], self.weapons_list)
                headers = []
                for i in range(self.weapons_list.columnCount()):
                    headers.append(self.weapons_list.horizontalHeaderItem(i).text().lower())
                lst = []
                if len(parameters) < len(headers):
                    for i in headers:
                        flag = False
                        for j in parameters:
                            if i == j[0]:
                                flag = True
                        if not flag:
                            lst.append(i)
                for i in range(len(headers)):
                    if headers[i] in lst:
                        if headers[i] == 'bullets':
                            item = QTableWidgetItem('1')
                            self.weapons_list.setItem(len(self.all_weapons) - 1, i, item)
                        elif (headers[i] == 'recoil angle' or headers[i] == 'recoil angle alt' or
                              headers[i] == 'is full auto'):
                            item = QTableWidgetItem('0')
                            self.weapons_list.setItem(len(self.all_weapons) - 1, i, item)
                        elif headers[i] == 'cycletime':
                            item = QTableWidgetItem('0.100000')
                            self.weapons_list.setItem(index, i, item)
                        self.update()
                    else:
                        try:
                            for sublist in range(len(parameters)):
                                if parameters[sublist][0] == headers[i]:
                                    index = sublist
                                    break
                            item = QTableWidgetItem(parameters[index][1])
                            self.weapons_list.setItem(len(self.all_weapons) - 1, i, item)
                            self.update()
                        except IndexError:
                            break
            else:
                self.weapons_list.removeRow(index)
                del self.all_weapons[-1]
            self.update()
        self.isPushButton = False

    def click(self) -> None:
        """
        Функция, которая при выборе ячейки в таблице проверяет, выбрана ли вся строка.
        """
        items = self.weapons_list.selectedItems()
        if len(items) == 40 and len(set(index.row() for index in self.weapons_list.selectedIndexes())) == 1:
            self.delete_button.setEnabled(True)
            self.rename_button.setEnabled(True)
            self.reset_weapon_button.setEnabled(True)
        else:
            self.delete_button.setEnabled(False)
            self.rename_button.setEnabled(False)
            self.reset_weapon_button.setEnabled(False)

    def return_all(self) -> None:
        """
        Возвращает игровые настройки до значений по умолчанию.
        """
        file = open(fn.path() + '/defaults/default_items_game.txt')
        lst = file.readlines()
        file.close()
        folder = fn.path()
        folder = folder[:folder.rfind('/')] + '/csgo/scripts/items/new_items_game.txt'
        new_items_game = open(folder, 'w')
        new_items_game.writelines(lst)
        os.remove(folder[:folder.rfind('/')] + '/items_game.txt')
        new_items_game.close()
        os.rename(folder, folder[:folder.rfind('/')] + '/items_game.txt')
        folder = fn.path()
        if language == 'en':
            file = open(fn.path() + '/defaults/default_csgo_english.txt', encoding='utf-16')
            folder = folder[:folder.rfind('/')] + '/csgo/resource/new_csgo_english.txt'
        else:
            file = open(fn.path() + '/defaults/default_csgo_russian.txt', encoding='utf_16')
            folder = folder[:folder.rfind('/')] + '/csgo/resource/new_csgo_russian.txt'
        lst = file.readlines()
        file.close()
        new_csgo = open(folder, 'w', encoding='utf-16')
        new_csgo.writelines(lst)
        new_csgo.close()
        if language == 'en':
            os.remove(folder[:folder.rfind('/')] + '/csgo_english.txt')
            os.rename(folder, folder[:folder.rfind('/')] + '/csgo_english.txt')
        else:
            os.remove(folder[:folder.rfind('/')] + '/csgo_russian.txt')
            os.rename(folder, folder[:folder.rfind('/')] + '/csgo_russian.txt')
        msg = QMessageBox()
        if language == 'en':
            msg.setText('The settings were successfully changed')
            msg.setWindowTitle('Success')
        else:
            msg.setText('Настройки успешно изменены')
            msg.setWindowTitle('Успех')
        msg.exec_()
        self.return_button.setEnabled(False)

    def delete(self) -> None:
        """
        Удаляет выбранное оружие.
        """
        global config_now

        name = self.weapons_list.verticalHeaderItem(self.weapons_list.currentRow()).text()
        fn.delete_weapon_from_table(config_now, name)
        self.all_weapons.pop(self.weapons_list.currentRow())
        self.all_names.pop(self.weapons_list.currentRow())
        self.weapons_list.removeRow(self.weapons_list.currentRow())


class ChoiceTable(QDialog):
    """
    Класс, создающий окно выбора установленной конфигурации
    """

    # noinspection PyUnresolvedReferences
    def __init__(self, tables: tuple):
        super().__init__()
        self.ok_button = QPushButton()
        self.choose_table = QLineEdit()
        self.tables_list = QListWidget()
        if language == 'en':
            uic.loadUi(fn.path() + '/UI/Choice Table.ui', self)
        else:
            uic.loadUi(fn.path() + '/UI/Choice Table ru.ui', self)

        self.lst = []
        icon = QIcon(fn.path() + '/icons/config.png')
        for i in tables:
            i = QListWidgetItem(i[2:])
            i.setIcon(icon)
            self.lst.append(i)
        self.lst_now = self.lst[:]

        for table in self.lst:
            self.tables_list.addItem(table)

        self.tables_list.itemClicked.connect(self.item_clicked_event)

        self.ok_button.clicked.connect(self.load_table)

        self.choose_table.textChanged.connect(self.search)

    def item_clicked_event(self, item) -> None:
        """
        Функция для вывода названия оружия в QLineEdit, если на него (оружие) нажали.
        :param item: Конфигурация, на которую нажали.
        """
        self.choose_table.setText(item.text())

    def load_table(self) -> None:
        """
        Применение конфигурации после ее выбора
        """
        global ex
        global config_now
        global start
        if self.choose_table.text() == '':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            if language == 'en':
                msg.setText("You haven't chosen a configuration")
                msg.setWindowTitle('Error')
            else:
                msg.setText('Вы не выбрали конфигурацию')
                msg.setWindowTitle('Ошибка')
            msg.exec_()
        else:
            start_cfg = open('start.ini', 'w')
            start.set('Config', 'config', self.choose_table.text())
            start.write(start_cfg)
            start_cfg.close()
            old = config_now
            config_now = self.choose_table.text()
            ex.reload(old=old)
            self.close()

    def search(self) -> None:
        """
        Функция, выполняющая поиск элементов в QListWidget при изменении текста в QLineEdit.
        """
        request = self.choose_table.text().lower()
        if request == '':
            for item in self.lst:
                self.remove(item)
                self.tables_list.addItem(item)
            for i in range(self.tables_list.count()):
                if self.tables_list.item(i) not in self.lst_now:
                    self.lst_now.append(self.tables_list.item(i))
        else:
            for item in self.lst:
                if (request == item.text().lower()[:len(request)] and
                        item not in self.lst_now):
                    self.lst_now.append(item)
                    self.tables_list.addItem(item)
                elif (request != item.text().lower()[:len(request)] and
                      item in self.lst_now):
                    self.lst_now.remove(item)
                    self.remove(item)
        self.update()

    def remove(self, elem) -> None:
        """
        Функция, удаляющая элемент из QListWidget.
        :param elem: Элемент, который требуется удалить
        """
        try:
            lst = [self.tables_list.item(i) for i in range(self.tables_list.count())]
            self.tables_list.takeItem(lst.index(elem))
        except ValueError:
            pass


class Load(QDialog):
    """
    Класс, создающий окно применения всех параметров
    """

    # noinspection PyUnresolvedReferences
    def __init__(self):
        self.ok_button = QPushButton()
        self.label = QLabel()
        self.progress_bar = QProgressBar()
        global config_now
        super().__init__()
        if language == 'en':
            uic.loadUi(fn.path() + '/UI/Load.ui', self)
        else:
            uic.loadUi(fn.path() + '/UI/Load ru.ui', self)

        self.progress_bar.setValue(0)
        self.ok_button.clicked.connect(self.close)
        self.config_now = config_now
        Thread(target=self.load).start()

    def load(self) -> None:
        """
        Функция, применяющая параметры.
        """
        global ex
        global language
        folder = fn.path()
        folder = folder[:folder.rfind('/')] + '/csgo/scripts/items/items_game.txt'
        new_items_game = open(folder, 'w')
        default_items_game = open(fn.path() + '/defaults/default_items_game.txt')
        lst = default_items_game.readlines()
        default_items_game.close()
        new_items_game.writelines(lst)
        new_items_game.close()
        for j in range(ex.weapons_list.rowCount()):
            if language == 'ru':
                self.label.setText(f'Загружаем параметры для оружия {ex.weapons_list.verticalHeaderItem(j).text()}')
            else:
                self.label.setText(f'Loading parameters for weapons {ex.weapons_list.verticalHeaderItem(j).text()}')
            parameters = {}
            for i in range(ex.weapons_list.columnCount()):
                parameters[ex.weapons_list.horizontalHeaderItem(i).text().lower()] = (
                    ex.weapons_list.item(j, i).text())
            time.sleep(0.2)
            self.progress_bar.setValue(math.floor(100 * j / (ex.weapons_list.rowCount())))
            fn.set_parameters(ex.all_weapons[j], ex.weapons_list,
                              name=ex.weapons_list.verticalHeaderItem(j).text(),
                              parameters=parameters, config_name=self.config_now)
        self.ok_button.setEnabled(True)
        self.progress_bar.setValue(100)
        if language == 'ru':
            self.label.setText('Параметры успешно изменены')
        else:
            self.label.setText('Settings successfully changed')


class AddWeapon(QDialog):
    """
    Класс, создающий окно добавления оружия.
    """

    # noinspection PyUnresolvedReferences
    def __init__(self):
        super().__init__()
        self.ok_button = QPushButton()
        self.choose_weapon = QLineEdit()
        self.weapons_list = QListWidget()
        if language == 'en':
            uic.loadUi(fn.path() + '/UI/Add weapon.ui', self)
        else:
            uic.loadUi(fn.path() + '/UI/Add weapon ru.ui', self)

        self.lst = []
        for i in range(self.weapons_list.count()):
            self.lst.append(self.weapons_list.item(i))
        self.lst_now = self.lst[:]

        self.weapons_list.itemClicked.connect(self.item_clicked_event)

        self.ok_button.clicked.connect(self.add_weapon)

        self.choose_weapon.textChanged.connect(self.search)

    def item_clicked_event(self, item) -> None:
        """
        Функция для вывода названия оружия в QLineEdit, если на него (оружие) нажали.
        :param item: Оружие, на которое нажали.
        """
        self.choose_weapon.setText(item.text())

    def add_weapon(self) -> None:
        """
        Добавление оружия в таблицу
        """
        global ex
        if self.choose_weapon.text() == '':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            if language == 'en':
                msg.setText("You haven't chosen a weapon")
                msg.setWindowTitle('Error')
            else:
                msg.setText('Вы не выбрали оружие')
                msg.setWindowTitle('Ошибка')
            msg.exec_()
        elif self.choose_weapon.text() in ex.all_weapons:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            if language == 'en':
                msg.setText(f'This weapon ({self.choose_weapon.text()}) has already been added')
                msg.setWindowTitle('Error')
            else:
                msg.setText(f'Такое оружие ({self.choose_weapon.text()}) уже добавлено')
                msg.setWindowTitle('Ошибка')
            msg.exec_()
        else:
            ex.isPushButton = True
            ex.all_weapons.append(self.choose_weapon.text())
            self.close()

    def search(self) -> None:
        """
        Функция, выполняющая поиск элементов в QListWidget при изменении текста в QLineEdit.
        """
        request = self.choose_weapon.text().lower()
        if request == '':
            for item in self.lst:
                self.remove(item)
                self.weapons_list.addItem(item)
            for i in range(self.weapons_list.count()):
                if self.weapons_list.item(i) not in self.lst_now:
                    self.lst_now.append(self.weapons_list.item(i))
        else:
            for item in self.lst:
                if (request == item.text().lower()[:len(request)] and
                        item not in self.lst_now):
                    self.lst_now.append(item)
                    self.weapons_list.addItem(item)
                elif (request != item.text().lower()[:len(request)] and
                      item in self.lst_now):
                    self.lst_now.remove(item)
                    self.remove(item)
        self.update()

    def remove(self, elem) -> None:
        """
        Функция, удаляющая элемент из QListWidget.
        :param elem: Элемент, который надо удалить.
        """
        try:
            lst = [self.weapons_list.item(i) for i in range(self.weapons_list.count())]
            self.weapons_list.takeItem(lst.index(elem))
        except ValueError:
            pass


def except_hook(cls, exception, traceback) -> None:
    """
    Функция, которая не позволяет закрыться окну при ошибке.
    :param cls:
    :param exception:
    :param traceback:
    """
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
