'''
Программа запрашивает навание планеты
сохраняет в файл и по желанию выводит на экран
имена всех существ этой планеты 
'''

import requests
from bs4 import BeautifulSoup
import re

print("Здравствуйте")

while True:

    print("Введите название планеты")
    planet = input()

    path = 'https://swapi.dev/api/planets/'

    # Для проверки есть ли такая планета.
    flag = 0 

    # Бежим по всем записям о планетах, пока не найдем нужную 
    # или пока не достигнем последней записи.
    for i in range(1, 60): 

        # Парсим данные с сайта.
        path += str(i)
        web_url = requests.get(path).text

        # Преобразуем данные, чтобы можно было их сравнить с введенными.
        inf = re.split(r",", web_url)
        name = re.split(r"\"", inf[0])
       
        # Если планета найдена, выходим.
        if name[3] == planet:
            flag = 1
            break
    
    # Проверка найдена ли планета.
    if flag == 0:
        print("К сожалению такой планеты нет.\
             Хотите попробовать еще раз?")
        choice = input()

        if choice.lower() == "нет" or choice.lower() == "no":
            print("Спасибо за внимание")
            break
        continue  # Начинаем новую итерацию т.к. планета не найдена.
    
    count = 0  # Для проверки.
    peoples = []  # Для хранения всех имен.

    for i in range(1, 83): 

        # Парсим данные с сайта.
        web_url = requests.get('https://swapi.dev/api/people/'+str(i)).text
        
        # Преобразуем данные для сравнения.
        inf = re.split(r",", web_url)

        for j in range(5, len(inf)):
            homeworld = re.split(r"\"", inf[j])

            if len(homeworld)>3:
                if homeworld[1]== 'homeworld':
                    break

        # Сравниваем адреса планет.
        if homeworld[3]== path+'/':
            count += 1
            name = re.split(r"\"", inf[0])

            peoples.append(name[3]) # Сохраняем имя существа.

    # Открываем файл для сохранения данных.
    f = open("data.txt", "w")

    # Выводим данные на экран и в файл.
    buf = "Имена всех жителей планеты под названием "+ planet+ " :"
    f.write(buf+"\n")
    print(buf)

    for j in range (len(peoples)):
        print(str(j+1)+ ")  "+ peoples[j])
        f.write(str(j+1)+ ")  "+ peoples[j]+"\n")

    f.close()

    print("Хотите попробовать еще раз?")
    choice = input()

    if choice.lower() == "нет" or choice.lower() == "no":
        print("Спасибо за внимание")
        break
    