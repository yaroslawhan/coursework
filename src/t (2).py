import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

# Создаем Frame для размещения всех элементов
frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

# Создаем Canvas внутри Frame
canvas = tk.Canvas(frame)
canvas.pack(side="left", fill="both", expand=True)

# Создаем вертикальную полосу прокрутки
scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

# Привязываем полосу прокрутки к Canvas
canvas.config(yscrollcommand=scrollbar.set)

# Создаем внутренний Frame для содержимого
inner_frame = tk.Frame(canvas)

# Размещаем элементы во внутреннем Frame
for i in range(50):
    tk.Label(inner_frame, text=f"Item {i}").pack()

# Помещаем внутренний Frame в Canvas
canvas.create_window((0, 0), window=inner_frame, anchor="nw")

# Функция для обновления Canvas при изменении размеров содержимого
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

# Привязываем функцию к событию изменения размеров внутреннего Frame
inner_frame.bind("<Configure>", on_frame_configure)

root.mainloop()
