# -*- coding: utf8 -*-
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import requests
from datetime import datetime

#Создание и обработка запроса
# url = "https://lk.gubkin.ru/schedule/api/api.php"
today = datetime.today()
formatted_date = today.strftime("%d-%m-%Y")
# params = {
#     "act": "schedule",
#     "date": "29.04.2024", #formatted_date
#     "groupId": "9199"
# }
# response = requests.get(url, params=params)
# data = response.json()

# Временное решение
data = {'state': True, 'rows': {'week': {'weekRussia': {'type': 'upper', 'number': 12, 'days': [{'date': '22-04-2024', 'isStudyDay': True, 'weekDayNumber': 0}, {'date': '23-04-2024', 'isStudyDay': True, 'weekDayNumber': 1}, {'date': '24-04-2024', 'isStudyDay': True, 'weekDayNumber': 2}, {'date': '25-04-2024', 'isStudyDay': True, 'weekDayNumber': 3}, {'date': '26-04-2024', 'isStudyDay': True, 'weekDayNumber': 4}, {'date': '27-04-2024', 'isStudyDay': True, 'weekDayNumber': 5}, {'date': '28-04-2024', 'isStudyDay': False, 'weekDayNumber': 6}]}, 'weekTashkent': {'type': 'upper', 'number': 12, 'days': [{'date': '22-04-2024', 'isStudyDay': True, 'weekDayNumber': 0}, {'date': '23-04-2024', 'isStudyDay': True, 'weekDayNumber': 1}, {'date': '24-04-2024', 'isStudyDay': True, 'weekDayNumber': 2}, {'date': '25-04-2024', 'isStudyDay': True, 'weekDayNumber': 3}, {'date': '26-04-2024', 'isStudyDay': True, 'weekDayNumber': 4}, {'date': '27-04-2024', 'isStudyDay': True, 'weekDayNumber': 5}, {'date': '28-04-2024', 'isStudyDay': False, 'weekDayNumber': 6}]}}, 'organizations': [{'id': 0, 'name': 'Москва', 'lessonsTimeChunks': ['8:30-9:15', '9:15-10:00', '10:15-11:00', '11:00-11:45', '12:00-12:45', '12:45-13:30', '14:00-14:45', '14:45-15:30', '15:45-16:30', '16:30-17:15', '17:20-18:05', '18:05-18:50', '18:55-19:40', '19:40-20:25', '20:30-21:15', '21:15-22:00'], 'lessons': [{'type': 'Семинар', 'subgroup': 0, 'events': [], 'isCanceled': False, 'isMoved': False, 'weekDayNumber': 1, 'timeChunks': [2, 3], 'selectivelyCourseId': None, 'resourceLink': None, 'course': {'id': 741, 'name': 'Интегралы, ряды, функции многих переменных', 'additionalInfo': ''}, 'versionId': 0, 'individualPlan': 0, 'studentAmount': 0, 'id': 316020, 'rooms': [{'id': 813, 'number': '501', 'typeId': 1}], 'changes': [], 'teachers': [{'id': 'BwFvZgo=', 'firstName': 'Инна', 'lastName': 'Мельникова', 'patronymic': 'Николаевна', 'shortComments': None, 'divisionsIds': [143]}], 'groups': [{'id': 9199, 'code': 'АС-23-04', 'qualificationType': 2, 'hasSpecializations': False, 'facultyId': 5, 'dateBegin': None, 'dateEnd': None}], 'divisions': [{'id': 143, 'name': 'кафедра высшей математики'}]}, {'type': 'Семинар', 'subgroup': 2, 'events': [], 'isCanceled': False, 'isMoved': False, 'weekDayNumber': 1, 'timeChunks': [4, 5], 'selectivelyCourseId': None, 'resourceLink': None, 'course': {'id': 12646, 'name': 'Иностранный язык (английский)', 'additionalInfo': ''}, 'versionId': 0, 'individualPlan': 0, 'studentAmount': 0, 'id': 315264, 'rooms': [{'id': 208, 'number': '2412', 'typeId': 1}], 'changes': [], 'teachers': [{'id': 'AgZmbQg=', 'firstName': 'Анна', 'lastName': 'Ткачева', 'patronymic': 'Владимировна', 'shortComments': None, 'divisionsIds': [29]}], 'groups': [{'id': 9199, 'code': 'АС-23-04', 'qualificationType': 2, 'hasSpecializations': False, 'facultyId': 5, 'dateBegin': None, 'dateEnd': None}], 'divisions': [{'id': 29, 'name': 'кафедра иностранных языков'}]}, {'type': 'Лекция', 'subgroup': 0, 'events': [], 'isCanceled': False, 'isMoved': False, 'weekDayNumber': 2, 'timeChunks': [4, 5], 'selectivelyCourseId': None, 'resourceLink': None, 'course': {'id': 7176, 'name': 'Периферийные устройства', 'additionalInfo': ''}, 'versionId': 0, 'individualPlan': 0, 'studentAmount': 0, 'id': 314690, 'rooms': [{'id': 5258, 'number': '1208', 'typeId': 1}], 'changes': [], 'teachers': [{'id': 'BgdsaQs=', 'firstName': 'Галина', 'lastName': 'Малиновская', 'patronymic': 'Николаевна', 'shortComments': None, 'divisionsIds': [142]}], 'groups': [{'id': 9199, 'code': 'АС-23-04', 'qualificationType': 2, 'hasSpecializations': False, 'facultyId': 5, 'dateBegin': None, 'dateEnd': None}], 'divisions': [{'id': 142, 'name': 'кафедра автоматизированных систем управления'}]}, {'type': 'Семинар', 'subgroup': 0, 'events': [], 'isCanceled': False, 'isMoved': False, 'weekDayNumber': 0, 'timeChunks': [6, 7], 'selectivelyCourseId': None, 'resourceLink': None, 'course': {'id': 7176, 'name': 'Периферийные устройства', 'additionalInfo': ''}, 'versionId': 0, 'individualPlan': 0, 'studentAmount': 0, 'id': 315843, 'rooms': [{'id': 328, 'number': '1207', 'typeId': 3}], 'changes': [], 'teachers': [{'id': 'BgdsaQs=', 'firstName': 'Галина', 'lastName': 'Малиновская', 'patronymic': 'Николаевна', 'shortComments': None, 'divisionsIds': [142]}, {'id': 'BQNtaAoF', 'firstName': 'Анастасия', 'lastName': 'Арбузова', 'patronymic': 'Викторовна', 'shortComments': None, 'divisionsIds': [142]}], 'groups': [{'id': 9199, 'code': 'АС-23-04', 'qualificationType': 2, 'hasSpecializations': False, 'facultyId': 5, 'dateBegin': None, 'dateEnd': None}], 'divisions': [{'id': 142, 'name': 'кафедра автоматизированных систем управления'}]}, {'type': 'Семинар', 'subgroup': 0, 'events': [], 'isCanceled': False, 'isMoved': False, 'weekDayNumber': 0, 'timeChunks': [4, 5], 'selectivelyCourseId': None, 'resourceLink': None, 'course': {'id': 6394, 'name': 'Деловой этикет и культура коммуникации', 'additionalInfo': ''}, 'versionId': 0, 'individualPlan': 0, 'studentAmount': 0, 'id': 315280, 'rooms': [{'id': 5268, 'number': '1510', 'typeId': 1}], 'changes': [], 'teachers': [{'id': 'BQNsbwoB', 'firstName': 'Ольга', 'lastName': 'Пумпянская', 'patronymic': 'Владимировна', 'shortComments': None, 'divisionsIds': [686]}], 'groups': [{'id': 9199, 'code': 'АС-23-04', 'qualificationType': 2, 'hasSpecializations': False, 'facultyId': 5, 'dateBegin': None, 'dateEnd': None}], 'divisions': [{'id': 686, 'name': 'кафедра истории'}]}, {'type': 'Лекция', 'subgroup': 0, 'events': [], 'isCanceled': False, 'isMoved': False, 'weekDayNumber': 2, 'timeChunks': [2, 3], 'selectivelyCourseId': None, 'resourceLink': None, 'course': {'id': 741, 'name': 'Интегралы, ряды, функции многих переменных', 'additionalInfo': ''}, 'versionId': 0, 'individualPlan': 0, 'studentAmount': 0, 'id': 314689, 'rooms': [{'id': 5258, 'number': '1208', 'typeId': 1}], 'changes': [], 'teachers': [{'id': 'BQNmbg0L', 'firstName': 'Евгений', 'lastName': 'Асташов', 'patronymic': 'Александрович', 'shortComments': None, 'divisionsIds': [143]}], 'groups': [{'id': 9199, 'code': 'АС-23-04', 'qualificationType': 2, 'hasSpecializations': False, 'facultyId': 5, 'dateBegin': None, 'dateEnd': None}], 'divisions': [{'id': 143, 'name': 'кафедра высшей математики'}]}, {'type': 'Лекция', 'subgroup': 0, 'events': [], 'isCanceled': False, 'isMoved': False, 'weekDayNumber': 2, 'timeChunks': [6, 7], 'selectivelyCourseId': None, 'resourceLink': None, 'course': {'id': 371, 'name': 'Правоведение', 'additionalInfo': ''}, 'versionId': 0, 'individualPlan': 0, 'studentAmount': 0, 'id': 314691, 'rooms': [{'id': 4817, 'number': 'Большая академическая аудитория им. В.Н.Виноградова (БАА)', 'typeId': 1}], 'changes': [], 'teachers': [{'id': 'AgRvZw4=', 'firstName': 'Оксана', 'lastName': 'Остапенко', 'patronymic': 'Юрьевна', 'shortComments': None, 'divisionsIds': [1316]}], 'groups': [{'id': 9199, 'code': 'АС-23-04', 'qualificationType': 2, 'hasSpecializations': False, 'facultyId': 5, 'dateBegin': None, 'dateEnd': None}], 'divisions': [{'id': 1316, 'name': 'кафедра гражданско-правовых дисциплин'}]}, {'type': 'Лекция', 'subgroup': 0, 'events': [], 'isCanceled': False, 'isMoved': False, 'weekDayNumber': 0, 'timeChunks': [0, 1], 'selectivelyCourseId': None, 'resourceLink': None, 'course': {'id': 860, 'name': 'Основы механики и молекулярная физика', 'additionalInfo': ''}, 'versionId': 0, 'individualPlan': 0, 'studentAmount': 0, 'id': 314685, 'rooms': [{'id': 4491, 'number': '343', 'typeId': 1}], 'changes': [], 'teachers': [{'id': 'BQVpaAs=', 'firstName': 'Сергей', 'lastName': 'Серебряков', 'patronymic': 'Георгиевич', 'shortComments': None, 'divisionsIds': [111]}], 'groups': [{'id': 9199, 'code': 'АС-23-04', 'qualificationType': 2, 'hasSpecializations': False, 'facultyId': 5, 'dateBegin': None, 'dateEnd': None}], 'divisions': [{'id': 111, 'name': 'кафедра физики'}]}, {'type': 'Семинар', 'subgroup': 0, 'events': [], 'isCanceled': False, 'isMoved': False, 'weekDayNumber': 4, 'timeChunks': [6, 7], 'selectivelyCourseId': None, 'resourceLink': None, 'course': {'id': 860, 'name': 'Основы механики и молекулярная физика', 'additionalInfo': ''}, 'versionId': 0, 'individualPlan': 0, 'studentAmount': 0, 'id': 341262, 'rooms': [{'id': 4493, 'number': '351', 'typeId': 1}], 'changes': [], 'teachers': [{'id': 'BQVpaAs=', 'firstName': 'Сергей', 'lastName': 'Серебряков', 'patronymic': 'Георгиевич', 'shortComments': None, 'divisionsIds': [111]}], 'groups': [{'id': 9199, 'code': 'АС-23-04', 'qualificationType': 2, 'hasSpecializations': False, 'facultyId': 5, 'dateBegin': None, 'dateEnd': None}], 'divisions': [{'id': 111, 'name': 'кафедра физики'}]}, {'type': 'Лекция', 'subgroup': 0, 'events': [], 'isCanceled': False, 'isMoved': False, 'weekDayNumber': 1, 'timeChunks': [0, 1], 'selectivelyCourseId': None, 'resourceLink': None, 'course': {'id': 1110, 'name': 'Основы алгоритмизации и программирования', 'additionalInfo': ''}, 'versionId': 0, 'individualPlan': 0, 'studentAmount': 0, 'id': 314688, 'rooms': [{'id': 4875, 'number': '725', 'typeId': 1}], 'changes': [], 'teachers': [{'id': 'BQVsbwk=', 'firstName': 'Валерий', 'lastName': 'Сидоров', 'patronymic': 'Васильевич', 'shortComments': None, 'divisionsIds': [137]}], 'groups': [{'id': 9199, 'code': 'АС-23-04', 'qualificationType': 2, 'hasSpecializations': False, 'facultyId': 5, 'dateBegin': None, 'dateEnd': None}], 'divisions': [{'id': 137, 'name': 'кафедра информатики'}]}, {'type': 'Лабораторная работа', 'subgroup': 0, 'events': [], 'isCanceled': False, 'isMoved': False, 'weekDayNumber': 4, 'timeChunks': [2, 3], 'selectivelyCourseId': None, 'resourceLink': None, 'course': {'id': 860, 'name': 'Основы механики и молекулярная физика', 'additionalInfo': ''}, 'versionId': 0, 'individualPlan': 0, 'studentAmount': 0, 'id': 314940, 'rooms': [{'id': 4489, 'number': '338', 'typeId': 2}], 'changes': [], 'teachers': [{'id': 'AAJvaAA=', 'firstName': 'Лариса', 'lastName': 'Филиппова', 'patronymic': 'Борисовна', 'shortComments': None, 'divisionsIds': [111]}, {'id': 'AAFsagk=', 'firstName': 'Александр', 'lastName': 'Серовайский', 'patronymic': 'Юрьевич', 'shortComments': None, 'divisionsIds': [111]}], 'groups': [{'id': 9199, 'code': 'АС-23-04', 'qualificationType': 2, 'hasSpecializations': False, 'facultyId': 5, 'dateBegin': None, 'dateEnd': None}], 'divisions': [{'id': 111, 'name': 'кафедра физики'}]}, {'type': 'Семинар', 'subgroup': 0, 'events': [], 'isCanceled': False, 'isMoved': False, 'weekDayNumber': 4, 'timeChunks': [0, 1], 'selectivelyCourseId': None, 'resourceLink': None, 'course': {'id': 595, 'name': 'Физическая культура', 'additionalInfo': ''}, 'versionId': 0, 'individualPlan': 0, 'studentAmount': 0, 'id': 316233, 'rooms': [{'id': 4719, 'number': 'Спортзал №2', 'typeId': 4}], 'changes': [], 'teachers': [{'id': 'DQRnZwk=', 'firstName': 'Наталья', 'lastName': 'Баркова', 'patronymic': 'Дмитриевна', 'shortComments': None, 'divisionsIds': [28]}], 'groups': [{'id': 9199, 'code': 'АС-23-04', 'qualificationType': 2, 'hasSpecializations': False, 'facultyId': 5, 'dateBegin': None, 'dateEnd': None}], 'divisions': [{'id': 28, 'name': 'кафедра физического воспитания и спорта'}]}, {'type': 'Семинар', 'subgroup': 0, 'events': [], 'isCanceled': False, 'isMoved': False, 'weekDayNumber': 0, 'timeChunks': [2, 3], 'selectivelyCourseId': None, 'resourceLink': None, 'course': {'id': 1110, 'name': 'Основы алгоритмизации и программирования', 'additionalInfo': ''}, 'versionId': 0, 'individualPlan': 0, 'studentAmount': 0, 'id': 315983, 'rooms': [{'id': 5171, 'number': '138', 'typeId': 3}], 'changes': {'teachers': [{'id': 'BQVvbA0=', 'firstName': 'Ирина', 'lastName': 'Перепухова', 'patronymic': 'Глебовна', 'shortComments': None, 'divisionsIds': [137]}, {'id': 'AwNpbwo=', 'firstName': 'Елена', 'lastName': 'Камнева', 'patronymic': 'Борисовна', 'shortComments': None, 'divisionsIds': [137]}]}, 'teachers': [{'id': 'BQVvbA0=', 'firstName': 'Ирина', 'lastName': 'Перепухова', 'patronymic': 'Глебовна', 'shortComments': None, 'divisionsIds': [137]}], 'groups': [{'id': 9199, 'code': 'АС-23-04', 'qualificationType': 2, 'hasSpecializations': False, 'facultyId': 5, 'dateBegin': None, 'dateEnd': None}], 'divisions': [{'id': 137, 'name': 'кафедра информатики'}]}, {'type': 'Семинар', 'subgroup': 1, 'events': [], 'isCanceled': False, 'isMoved': False, 'weekDayNumber': 1, 'timeChunks': [4, 5], 'selectivelyCourseId': None, 'resourceLink': None, 'course': {'id': 12646, 'name': 'Иностранный язык (английский)', 'additionalInfo': ''}, 'versionId': 0, 'individualPlan': 0, 'studentAmount': 0, 'id': 315263, 'rooms': [{'id': 219, 'number': '2423', 'typeId': 1}], 'changes': [], 'teachers': [{'id': 'AgZpags=', 'firstName': 'Марина', 'lastName': 'Максимова', 'patronymic': 'Евгеньевна', 'shortComments': None, 'divisionsIds': [29]}], 'groups': [{'id': 9199, 'code': 'АС-23-04', 'qualificationType': 2, 'hasSpecializations': False, 'facultyId': 5, 'dateBegin': None, 'dateEnd': None}], 'divisions': [{'id': 29, 'name': 'кафедра иностранных языков'}]}, {'type': 'Семинар', 'subgroup': 0, 'events': [], 'isCanceled': False, 'isMoved': False, 'weekDayNumber': 4, 'timeChunks': [4, 5], 'selectivelyCourseId': None, 'resourceLink': None, 'course': {'id': 13381, 'name': 'Профессионально-личностное саморазвитие', 'additionalInfo': ''}, 'versionId': 0, 'individualPlan': 0, 'studentAmount': 0, 'id': 315816, 'rooms': [{'id': 5174, 'number': '1419', 'typeId': 1}], 'changes': {'rooms': [{'id': 5263, 'number': '1528'}]}, 'teachers': [{'id': 'BwFmbg0=', 'firstName': 'Татьяна', 'lastName': 'Семенова', 'patronymic': 'Николаевна', 'shortComments': None, 'divisionsIds': [25]}], 'groups': [{'id': 9199, 'code': 'АС-23-04', 'qualificationType': 2, 'hasSpecializations': False, 'facultyId': 5, 'dateBegin': None, 'dateEnd': None}], 'divisions': [{'id': 25, 'name': 'кафедра философии и социально-политических технологий'}]}, {'type': 'Семинар', 'subgroup': 0, 'events': [], 'isCanceled': False, 'isMoved': False, 'weekDayNumber': 5, 'timeChunks': [8, 9, 10, 11], 'selectivelyCourseId': None, 'resourceLink': None, 'course': {'id': 9589, 'name': 'Иностранный язык (русский)', 'additionalInfo': ''}, 'versionId': 0, 'individualPlan': 0, 'studentAmount': 0, 'id': 341058, 'rooms': [{'id': 249, 'number': '1518б', 'typeId': 1}], 'changes': {'teachers': [{'id': 'BQRmaw0=', 'firstName': 'Александр', 'lastName': 'Акишин', 'patronymic': 'Петрович', 'shortComments': None, 'divisionsIds': [27]}]}, 'teachers': [], 'groups': [{'id': 9199, 'code': 'АС-23-04', 'qualificationType': 2, 'hasSpecializations': False, 'facultyId': 5, 'dateBegin': None, 'dateEnd': None}], 'divisions': [{'id': 27, 'name': 'кафедра русского языка'}]}, {'type': 'Мероприятие', 'groups': [{'id': 9199, 'code': 'АС-23-04', 'qualificationType': 2, 'hasSpecializations': False, 'facultyId': 5, 'dateBegin': None, 'dateEnd': None}], 'subgroup': 0, 'events': [], 'isCanceled': False, 'isMoved': False, 'weekDayNumber': 2, 'timeChunks': [8], 'selectivelyCourseId': None, 'course': {'id': 27207, 'name': 'Кураторский час', 'additionalInfo': None}, 'id': 27207, 'rooms': [{'id': 4705, 'number': '1213', 'typeId': 1}], 'teachers': [{'id': 'BwZtaQ4=', 'firstName': 'Денис', 'lastName': 'Волков', 'patronymic': 'Андреевич', 'shortComments': None, 'divisionsIds': [142]}], 'changes': [], 'divisions': [{'id': None, 'name': ''}]}], 'alternativeLessonsTimeChunks': []}, {'id': 1, 'name': 'Оренбург', 'lessonsTimeChunks': ['08:30-09:15', '09:15-10:00', '10:05-10:50', '10:50-11:35', '11:45-12:30', '12:30-13:15', '13:45-14:30', '14:30-15:15', '15:20-16:05', '16:05-16:50', '16:55-17:40', '17:40-18:25', '18:30-19:15', '19:15-20:00', '20:15-21:00', '21:00-21:45'], 'lessons': []}, {'id': 2, 'name': 'Ташкент', 'lessonsTimeChunks': ['8:30-9:15', '9:15-10:00', '10:10-10:55', '10:55-11:40', '12:20-13:05', '13:05-13:50', '14:00-14:45', '14:45-15:30', '15:40-16:25', '16:25-17:10'], 'lessons': []}, {'id': 3, 'name': 'Атырау', 'lessonsTimeChunks': [], 'lessons': [], 'alternativeLessonsTimeChunks': ['8:30-9:15', '9:15-10:00', '10:15-11:00', '11:00-11:45', '12:00-12:45', '12:45-13:30', '14:00-14:45', '14:45-15:30', '15:45-16:30', '16:30-17:15', '17:20-18:05', '18:05-18:50', '18:55-19:40', '19:40-20:25', '20:30-21:15', '21:15-22:00']}]}}

# Блок данных
month_names = {
    1: 'января',
    2: 'февраля',
    3: 'марта',
    4: 'апреля',
    5: 'мая',
    6: 'июня',
    7: 'июля',
    8: 'августа',
    9: 'сентября',
    10: 'октября',
    11: 'ноября',
    12: 'декабря'
}
days_of_week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
ents = {}
lbls = []
raw_heads = []
raw_text = []
week_info_dict = {}
column_headers = {}
row_headers = {}
weekday = today.weekday()
main_title = (data["rows"]["week"]["weekRussia"]["days"][0]["date"]).split("-")[0] + " " + month_names[int((data["rows"]["week"]["weekRussia"]["days"][0]["date"]).split("-")[1])] + " - " + (data["rows"]["week"]["weekRussia"]["days"][6]["date"]).split("-")[0] + " " + month_names[int((data["rows"]["week"]["weekRussia"]["days"][6]["date"]).split("-")[1])] + ", " + (data["rows"]["week"]["weekRussia"]["days"][6]["date"]).split("-")[2] # int(today.strftime("%d "))
dates = [(int(today.strftime("%d ")) + i - weekday) for i in range(7)]

# Функция рисования расписания
def schedule_drawing():
    # Вывод информации о неделе
    if data["rows"]["week"]["weekRussia"]["type"] == "lower":
        right_subtitle = str(data["rows"]["week"]["weekRussia"]["number"]) + "-я неделя, нижняя"
    else:
        right_subtitle = str(data["rows"]["week"]["weekRussia"]["number"]) + "-я неделя, верхняя"
    # week_info_dict["frame"] = Frame(win, bg="#fafafa", height=30)
    # week_info_dict["frame"].pack(fill=X, pady=10)
    # week_info_dict["right_subtitle"] = ttk.Label(week_info_dict["frame"], text=right_subtitle, font=('Arial', 14), background="#fafafa", foreground="#6f6f6f")
    # week_info_dict["right_subtitle"].pack(side=RIGHT, padx=30, pady=10, anchor=NE, expand=False)
    # week_info_dict["main_title"] = ttk.Label(week_info_dict["frame"], text=main_title, font=('Arial', 16), background="#fafafa")
    # week_info_dict["main_title"].pack(side=TOP, pady=10)

    #Рисование заголовков рядов
    # column_headers["frame"] = Frame(win)
    # column_headers["frame"].pack(fill=X, padx=(150, 30), pady=30)
    # column_headers["canvases"] = []
    # for i in range(7):
    #     if data["rows"]["week"]["weekRussia"]["days"][i]["isStudyDay"] == False:
    #         column_headers["canvases"].append([Canvas(column_headers["frame"], bg="#ffebeb", highlightthickness=1, highlightbackground="#fefefe", width=50, height=100)])
    #     else:
    #         column_headers["canvases"].append([Canvas(column_headers["frame"], bg="#f0f0f0", highlightthickness=1, highlightbackground="#fefefe", width=50, height=100)]) # Label(column_frame, text=f"Виджет {i+1}", bg="lightblue", relief="solid")
    #     column_headers["canvases"][i][0].pack(side=LEFT, fill=BOTH, expand=True)
    #     if int((data["rows"]["week"]["weekRussia"]["days"][i]["date"]).split("-")[0]) == int(today.strftime("%d ")):
    #         column_headers["canvases"][i].append(column_headers["canvases"][i][0].create_text(5, 7, anchor=NW, text=days_of_week[i], font=("Arial", 12), fill="#004de6"))
    #         column_headers["canvases"][i].append(column_headers["canvases"][i][0].create_text(5, 33, anchor=NW, text=(data["rows"]["week"]["weekRussia"]["days"][i]["date"]).split("-")[0], font=("Arial", 35), fill="#004de6"))
    #     else:
    #         column_headers["canvases"][i].append(column_headers["canvases"][i][0].create_text(5, 7, anchor=NW, text=days_of_week[i], font=("Arial", 12), fill="#2f2f2f"))
    #         column_headers["canvases"][i].append(column_headers["canvases"][i][0].create_text(5, 33, anchor=NW, text=(data["rows"]["week"]["weekRussia"]["days"][i]["date"]).split("-")[0], font=("Arial", 35), fill="#2f2f2f"))

    # # Рисование заголовков строк
    # frame_for_scroll = Frame(win)
    # frame_for_scroll.place(x=19, y=202) # pack(fill=Y, padx=20, anchor=NW)
    # row_headers["labels"] = []
    # for i in range(13):
    #     row_headers["labels"].append(Label(frame_for_scroll, text=data["rows"]["organizations"][0]["lessonsTimeChunks"][i], bg="#ffffff", highlightthickness=1, highlightbackground="#000000", width=15, height=5, relief="solid", font=("Arial", 10), fg="#6f6f6f"))
    #     row_headers["labels"][i].pack(side=TOP, fill=BOTH, expand=True)
        
    # row_headers["canvases"] = []
    # for i in range(13):
    #     row_headers["canvases"].append([Canvas(row_headers["frame"], bg="#ffffff", highlightthickness=1, highlightbackground="#000000", width=128, height=70, relief="solid")])
    #     row_headers["canvases"][i][0].pack(side=TOP, fill=BOTH, expand=True)
    #     row_headers["canvases"][i].append(row_headers["canvases"][i][0].create_text(10, 5, anchor=NW, text=data["rows"]["organizations"][0]["lessonsTimeChunks"][i], font=("Arial", 10), fill="#6f6f6f"))


# Создание окна
# root = Tk()
# root.title("Расписание")
# root.geometry("1620x900")
# root.config(bg="#fafafa")

# main_canvas = Canvas(root)
# scrollbar = Scrollbar(root, orient="vertical", command=main_canvas.yview)
# win = Frame(main_canvas)
# main_canvas.create_window(0, 0, anchor='nw', window=win)
# main_canvas.update_idletasks()
# main_canvas.configure(scrollregion=main_canvas.bbox('all'), 
#                  yscrollcommand=scrollbar.set)
# main_canvas.pack(fill='both', expand=True, side='left')
# scrollbar.pack(fill='y', side='right')

# Временное решение для вывода data
# editor = Text()
# editor.pack(fill=BOTH, expand=1)
# editor.insert("1.0", data)

# Рисование окна
# if data["state"] == True:
#     schedule_drawing()

#     win.mainloop()
# else:
#     messagebox.showerror("Ошибка", "Расписание на указанную дату недоступно")
#     win.destroy

# Создание окна
class Window(QMainWindow):
	def __init__(self):

		def add_label(self):
			print("Hi")
			self.new_text.setText("HAHAHHA")
			self.new_text.move(100, 300)
			self.new_text.adjustSize()

		super(Window, self).__init__()

		self.new_text = QtWidgets.QLabel(self)
		
		self.main_text = QtWidgets.QLabel(self)
		self.main_text.setText("sasddasdhew;gnlkdsav")
		self.main_text.move(100, 100)
		self.main_text.adjustSize()
		self.butt = QtWidgets.QPushButton(self)
		self.butt.move(100, 200)
		self.butt.setText("Press on me")
		self.butt.adjustSize()
		self.butt.clicked.connect(add_label)
	
		self.setWindowTitle("Text or test")
		self.setGeometry(300, 250, 600, 600)

def application():
	app = QApplication(sys.argv)
	win = Window()

	win.show()
	sys.exit(app.exec_())

# Запуск окна
if __name__ == "__main__":
	application()