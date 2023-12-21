# coding=windows-1251
"""
Файл с основными функциями
"""
from PyQt5.QtWidgets import QTableWidget
import os
import configparser
import variables
import sqlite3
import locale
import ctypes


def path() -> str:
    """
    Функция для возвращения директории, в которой находится исполняемый файл.
    :return path: Путь к программе.
    """
    return os.getcwd().replace('\\', '/')


folder = path()
folder = folder[:folder.rfind('/')] + '/csgo/scripts/items/items_game.txt'

weapons_format = variables.weapons_format


def get_filename(filepath: str) -> str:
    """
    Функция, возвращающая имя файла по директории, в которой он лежит
    :param filepath: Путь к файлу.
    :return filename: Имя файла.
    """
    filepath.replace('\\', '/')
    if '/' in filepath:
        filename = filepath[filepath.rfind('/') + 1:]
        filename = filename[:filename.rfind('.')]
    else:
        filename = filepath
    return filename


def get_default_parameters(weapon: str, weapon_list: QTableWidget) -> list:
    """
    Получение параметров по умолчанию конкретного оружия
    :param weapon: Тип оружия.
    :param weapon_list: Таблица с оружиями.
    :return weapon_params: Параметры оружия.
    """
    # noinspection SpellCheckingInspection
    weapon = weapons_format[weapon.upper()]
    items_game = open(path() + '/defaults/default_items_game.txt')
    lst = [string.strip('\n\t') for string in items_game.readlines()]
    weapon_index = [i for i in range(len(lst)) if weapon in lst[i]][0]
    attributes_index = [i for i in range(weapon_index, len(lst)) if 'attributes' in lst[i]][0]
    start_index = attributes_index + 2
    end_index = start_index + 1
    for i in range(start_index, len(lst)):
        if '}' in lst[i] and i > start_index:
            end_index = i
            break
    lst = lst[start_index:end_index]
    headers = []
    for i in range(weapon_list.columnCount()):
        headers.append(weapon_list.horizontalHeaderItem(i).text().lower())
    result = []
    for line in lst:
        line = line.replace('\t\t', '---')
        line = line.split('---')
        parameter = line[0].strip('"')
        value = line[1].strip('"')
        if parameter in headers:
            result.append((parameter, value))
    items_game.close()
    return result


def set_parameters(weapon: str, weapon_list: QTableWidget, parameters: dict, name: str, config_name: str) -> None:
    """
    Запись параметров
    :param weapon: Тип оружия.
    :param weapon_list: Таблица с оружиями.
    :param parameters: Параметры оружия.
    :param name: Имя оружия.
    :param config_name: Имя текущей конфигурации.
    """
    # noinspection SpellCheckingInspection
    global folder
    reformat_weapon = weapons_format[weapon.upper()]
    items_game = open(folder)
    lst = [string for string in items_game.readlines()]
    weapon_index = [i for i in range(len(lst)) if reformat_weapon in lst[i]][0]
    attributes_index = [i for i in range(weapon_index, len(lst)) if 'attributes' in lst[i]][0]
    start_index = attributes_index + 2
    end_index = [i for i in range(start_index, len(lst)) if '}' in lst[i]][0]
    headers = []
    for i in range(weapon_list.columnCount()):
        headers.append(weapon_list.horizontalHeaderItem(i).text().lower())
    text = str(f'{name}, ')
    pars = [[j.strip('"') for j in i.strip('\t\n').replace('\t\t', '/t/t').split('/t/t')] for i in
            lst[start_index:end_index]]
    for header in headers:
        flag = False
        for i in range(start_index, end_index):
            if header == pars[i - start_index][0]:
                del lst[i]
                lst.insert(i, f'\t\t\t\t"{header}"\t\t"{parameters[header]}"\n')
                text += str(f'{parameters[header]}, ')
                flag = True
                break
        if not flag:
            lst.insert(end_index - 1, f'\t\t\t\t"{header}"\t\t"{parameters[header]}"\n')
            text += str(f'{parameters[header]}, ')
    items_game.close()
    new_items_game = open(folder, 'w')
    new_items_game.writelines(lst)
    new_items_game.close()
    text = weapon + ', ' + text
    text = tuple(text.split(', '))[:-1]
    locale.getlocale()
    windll = ctypes.windll.kernel32
    if locale.windows_locale[windll.GetUserDefaultUILanguage()] == 'ru_RU':
        folder_3 = path()
        folder_3 = folder_3[:folder_3.rfind('/')] + '/csgo/resource/csgo_russian.txt'
        file = open(folder_3, encoding='utf-16')
        lst = file.readlines()
        new_lst = lst[:]
        start_index = lst.index('\t\t"SFUI_WPNHUD_Pistol"\t\t"Пистолет"\n')
        end_index = lst.index('\t\t"SFUI_WPNHUD_KnifeBayonet"\t"Штык-нож"\n')
        lst = lst[start_index:end_index]
        for i in range(len(lst)):
            if lst[i] in variables.csgo_russian[weapon]:
                index = start_index + i
                old = new_lst[index]
                old = old.replace('\t', '/t')
                new = old[:old.rfind('/t') + 3] + name + '"\n'
                new = new.replace('/t', '\t')
                del new_lst[index]
                new_lst.insert(index, new)
                new_file = open(path()[:path().rfind('/')] + '/csgo/resource/new_csgo_russian.txt', 'w',
                                encoding='utf-16')
                new_file.writelines(new_lst)
                new_file.close()
                file.close()
                os.remove(path()[:path().rfind('/')] + '/csgo/resource/csgo_russian.txt')
                os.rename(path()[:path().rfind('/')] + '/csgo/resource/new_csgo_russian.txt',
                          path()[:path().rfind('/')] + '/csgo/resource/csgo_russian.txt')
    else:
        folder_3 = path()
        folder_3 = folder_3[:folder_3.rfind('/')] + '/csgo/resource/csgo_english.txt'
        file = open(folder_3, encoding='utf-16')
        lst = file.readlines()
        new_lst = lst[:]
        start_index = lst.index('\t\t"SFUI_WPNHUD_Pistol"\t\t"Pistol"\n')
        end_index = lst.index('\t\t"SFUI_WPNHUD_KnifeBayonet"\t"Bayonet"\n')
        lst = lst[start_index:end_index]
        for i in range(len(lst)):
            if lst[i] in variables.csgo_english[weapon]:
                index = start_index + i
                old = new_lst[index]
                old = old.replace('\t', '/t')
                new = old[:old.rfind('/t') + 3] + name + '"\n'
                new = new.replace('/t', '\t')
                del new_lst[index]
                new_lst.insert(index, new)
                new_file = open(path()[:path().rfind('/')] + '/csgo/resource/new_csgo_english.txt', 'w',
                                encoding='utf-16')
                new_file.writelines(new_lst)
                new_file.close()
                file.close()
                os.remove(path()[:path().rfind('/')] + '/csgo/resource/csgo_english.txt')
                os.rename(path()[:path().rfind('/')] + '/csgo/resource/new_csgo_english.txt',
                          path()[:path().rfind('/')] + '/csgo/resource/csgo_english.txt')
    set_cfg_params_in_table(config_name, text)
    return


def get_table_parameters(table: str, i: int) -> tuple:
    """
    Получение параметров из таблицы.
    :param table: Таблица БД.
    :param i: id оружия
    :return weapon_params: Параметры оружия.
    """
    connect = sqlite3.connect(path() + '/database/database.db')
    cursor = connect.cursor()
    # noinspection SqlResolve
    weapon = cursor.execute('SELECT * FROM cs' + table).fetchall()[i]
    connect.commit()
    return weapon


def set_cfg_params_in_table(table: str, values: tuple) -> None:
    """
    Параметры, полученные из конфигурации, записывает в таблицу.
    :param table: Таблица БД.
    :param values: Значения.
    """
    connect = sqlite3.connect(path() + '/database/database.db')
    cursor = connect.cursor()
    # noinspection SqlResolve
    table = '_'.join(table.split())
    # noinspection SqlResolve
    cursor.execute('INSERT INTO cs' + table + ' values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, '
                                              '?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);', values)
    connect.commit()
    return


def get_length_table(table: str) -> int:
    """
    Возвращает длину таблицы.
    :param table: Таблица БД.
    :return length: Длина таблицы.
    """
    connect = sqlite3.connect(path() + '/database/database.db')
    cursor = connect.cursor()
    # noinspection SqlResolve
    length = len(cursor.execute('SELECT * FROM cs' + table).fetchall())
    connect.commit()
    return length


def create_config_table(name: str) -> None:
    """
    Создает таблицу.
    :param name: Имя таблицы.
    """
    connect = sqlite3.connect(path() + '/database/database.db')
    cursor = connect.cursor()
    name = '_'.join(name.split())
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cs''' + name + ''' (
            gun_name                        TEXT PRIMARY KEY ON CONFLICT REPLACE,
            gun_type                        TEXT,
            [Primary reserve ammo max]      TEXT,
            [Recovery time crouch]          TEXT,
            [Recovery time crouch final]    TEXT,
            [Recovery time stand]           TEXT,
            [Recovery time stand final]     TEXT,
            [Inaccuracy jump initial]       TEXT,
            [Inaccuracy jump]               TEXT,
            [Max player speed]              TEXT,
            [Is full auto]                  TEXT,
            [In game price]                 TEXT,
            [Armor ratio]                   TEXT,
            Damage                          TEXT,
            Range                           TEXT,
            Bullets                         TEXT,
            Cycletime                       TEXT,
            Spread                          TEXT,
            [Inaccuracy crouch]             TEXT,
            [Inaccuracy stand]              TEXT,
            [Inaccuracy land]               TEXT,
            [Inaccuracy ladder]             TEXT,
            [Inaccuracy fire]               TEXT,
            [Inaccuracy move]               TEXT,
            [Recoil angle]                  TEXT,
            [Recoil angle variance]         TEXT,
            [Recoil magnitude]              TEXT,
            [Recoil magnitude variance]     TEXT,
            [Recoil seed]                   TEXT,
            [Primary clip size]             TEXT,
            [Inaccuracy crouch alt]         TEXT,
            [Inaccuracy fire alt]           TEXT,
            [Inaccuracy jump alt]           TEXT,
            [Inaccuracy ladder alt]         TEXT,
            [Inaccuracy land alt]           TEXT,
            [Inaccuracy move alt]           TEXT,
            [Inaccuracy stand alt]          TEXT,
            [Max player speed alt]          TEXT,
            [Recoil angle alt]              TEXT,
            [Recoil angle variance alt]     TEXT,
            [Recoil magnitude alt]          TEXT,
            [Recoil magnitude variance alt] TEXT
        );
        ''')
    connect.commit()
    return


def get_config_parameters(path_to_config: str) -> list:
    """
    Возвращает параметры из конфигурации
    :param path_to_config: Путь к конфигурации.
    :return list: Имена и типы оружий.
    """
    config_name = get_filename(path_to_config)
    create_config_table(config_name)
    config = configparser.ConfigParser()
    config.read(f'{config_name}.ini')
    lst = []
    for weapon_type in config['Guns']:
        weapon = config['Guns'][weapon_type].split(', ')
        weapon_type = weapon[0]
        weapon_name = weapon[1]
        weapon = weapon[2:]
        dct = dict(weapon_type=weapon_type, weapon_name=weapon_name, weapon=weapon)
        lst.append(dct)
        tpl = [weapon_type, weapon_name]
        tpl.extend(weapon)
        tpl = tuple(tpl)
        set_cfg_params_in_table(config_name, tpl)
    return lst


def delete_weapon_from_table(table_name, weapon_name):
    """
    Удаление оружия из таблицы
    :param table_name: Имя таблицы БД.
    :param weapon_name: Имя оружия.
    """
    connect = sqlite3.connect(path() + '/database/database.db')
    cursor = connect.cursor()
    # noinspection SqlResolve
    cursor.execute("DELETE FROM cs" + table_name + " WHERE gun_name = ?", (weapon_name,))
    connect.commit()


def get_all_tables():
    """
    Получение всех таблиц БД
    :return:
    """
    con = sqlite3.connect(path() + '/database/database.db')
    cursor = con.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    con.commit()
    return tuple(i[0] for i in cursor.fetchall())


def rename_table(old_name, new_name):
    """
    Функция для переименования таблицы
    :param old_name:
    :param new_name:
    """
    con = sqlite3.connect(path() + '/database/database.db')
    cursor = con.cursor()
    # noinspection SpellCheckingInspection
    cursor.execute("ALTER TABLE cs" + old_name + " RENAME TO cs" + new_name)
    con.commit()
