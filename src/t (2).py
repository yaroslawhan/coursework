from tkinter import *

root = Tk()
root.geometry("500x200")

# # Создаем функцию для создания виджетов Label с заданными параметрами оформления
# def create_label_with_style(parent, text, font=("Arial", 12), fill="#004de6"):
#     label = tk.Label(parent, text=text, font=font, fg=fill, bg="#ffebeb", bd=1, relief="solid", padx=5, pady=5)
#     return label

# # Пример создания виджетов Label с аналогичным оформлением
# days_and_dates = [("Monday", "10"), ("Tuesday", "11"), ("Wednesday", "12"), ("Thursday", "13"), ("Friday", "14"), ("Saturday", "15"), ("Sunday", "16")]

# for day, date in days_and_dates:
#     label_day_and_date = create_label_with_style(root, f"{day}\n{date}", font=("Arial", 12))
#     label_day_and_date.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# # Устанавливаем размер шрифта только для числа
# for label in root.winfo_children():
#     label.config(font=("Arial", 25))

main_canvas = Canvas(root)
scrollbar = Scrollbar(root, orient="vertical", command=main_canvas.yview)

win = Frame(main_canvas)
# group of widgets
for i in range(20):
    Label(win, text='label %i' % i).pack()
# put the frame in the canvas
main_canvas.create_window(0, 0, anchor='nw', window=win)
# make sure everything is displayed before configuring the scrollregion
main_canvas.update_idletasks()

main_canvas.configure(scrollregion=main_canvas.bbox('all'), 
                 yscrollcommand=scrollbar.set)
                 
main_canvas.pack(fill='both', expand=True, side='left')
scrollbar.pack(fill='y', side='right')

root.mainloop()
