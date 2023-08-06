"""PackChecker 2.0 by oneeyeddancer/GPL3 License"""
import importlib.util
import subprocess
import sys


class PackChecker:
    def __init__(self):
        self.to_install = []  # список пакетов для установки

    def check(self, req='requirements.txt'):  # Пример: 'data/req.txt' или ['PySide6', 'bs4']
        if isinstance(req, str):  # если строка, то это считается путем до файла
            with open(req) as file:
                packages = file.read().splitlines()  # считываем все строки и преобразуем в список
        elif isinstance(req, list) or isinstance(req, tuple):  # либо берем значения из списка/кортежа
            packages = req
        else:
            return print('Неверный формат для записи зависимостей!')

        for package in packages:  # проверка всех пакетов на наличие
            spec = importlib.util.find_spec(package)  # нахождение с помощью find_spec()
            if spec is None:
                self.to_install.append(package)  # если его нет, то добавляем в список для закачки

        if self.to_install:  # если список закачки пуст, то завершаем работу
            print(f"Необходимые пакеты не установлены: {', '.join(self.to_install)}")
            if input("Установить их? [y/n]: ").lower() == 'y':
                self.install()
            else:
                print("Загрузка отменена")
        else:
            print('Все пакеты установлены!')

    def install(self):
        command = [sys.executable, "-m", "pip", "install"]  # инструкция для скачивания пакета
        command.extend(self.to_install)  # расширяем, добавляя пакеты
        subprocess.check_call(command)  # выполнение инструкции
        input("Команда завершена. Enter для продолжения ")
