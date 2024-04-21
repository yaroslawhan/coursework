import tkinter as tk
from tkinter import ttk

# Создаем главное окно
root = tk.Tk()
root.title("Расписание на неделю")
root.geometry("1600x500")

# Создаем таблицу для расписания
tree = ttk.Treeview(root, columns=("time", "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"), show="headings")
tree.pack(expand=True, fill="both")

# Задаем заголовки столбцов
tree.heading("time", text="Время")
days_of_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
for day in days_of_week:
    tree.heading(day, text=day)

# Временные промежутки
time_slots = [
    "8:30 - 9:15", "9:15 - 10:00", "10:15 - 11:00", "11:00 - 11:45",
    "12:00 - 12:45", "12:45 - 13:30", "14:00 - 14:45", "14:45 - 15:30",
    "15:45 - 16:30", "16:30 - 17:15", "17:20 - 18:05", "18:05 - 18:50",
    "18:55 - 19:40"
]

# Добавляем временные промежутки в таблицу
for time_slot in time_slots:
    tree.insert("", tk.END, values=(time_slot, "", "", "", "", "", "", ""))

# Запускаем главный цикл обработки событий
root.mainloop()