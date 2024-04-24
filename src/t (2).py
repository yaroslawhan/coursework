import tkinter as tk

root = tk.Tk()

# Создание и размещение фрейма, заполняющего все пространство по горизонтали
frame = tk.Frame(root)
frame.pack(fill=tk.X, padx=10, pady=10)

# Создание списка для хранения виджетов
widgets = []

# Создание и размещение 7 виджетов внутри фрейма
for i in range(7):
    widget = tk.Label(frame, text=f"Виджет {i+1}", bg="lightblue", relief="solid")
    widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    widgets.append(widget)

root.mainloop()
