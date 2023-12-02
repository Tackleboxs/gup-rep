import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog


def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operation = operation_var.get()

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Ошибка: деление на ноль"

    result_label.config(text="Результат: " + str(result))


def show_checkbox_selection():
    selected_options = ""
    if var1.get():
        selected_options += "Вы выбрали первый вариант\n"
    if var2.get():
        selected_options += "Вы выбрали второй вариант\n"
    if var3.get():
        selected_options += "Вы выбрали третий вариант\n"

    messagebox.showinfo("Выбранные опции", selected_options)


def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            file_content = file.read()
            text_area.delete(1.0, tk.END)  # Очистить содержимое Text элемента
            text_area.insert(tk.END, file_content)  # Вставить содержимое файла в Text элемент


root = tk.Tk()
root.title("Гупалов Владислав Александрович")
root.geometry("390x250")
tab_control = ttk.Notebook(root)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Калькулятор')
tab_control.add(tab2, text='Чекбоксы')
tab_control.add(tab3, text='Работа с текстом')

# Вкладка 1 - Калькулятор
label1 = tk.Label(tab1, text="Введите число 1:")
label1.grid(row=0, column=0)
entry1 = tk.Entry(tab1)
entry1.grid(row=0, column=1)

label2 = tk.Label(tab1, text="Введите число 2:")
label2.grid(row=1, column=0)
entry2 = tk.Entry(tab1)
entry2.grid(row=1, column=1)

operations = ["+", "-", "*", "/"]
operation_var = tk.StringVar(tab1)
operation_dropdown = tk.OptionMenu(tab1, operation_var, *operations)
operation_dropdown.grid(row=2, column=0)

calculate_button = tk.Button(tab1, text="Вычислить", command=calculate)
calculate_button.grid(row=2, column=1)

result_label = tk.Label(tab1, text="Результат: ")
result_label.grid(row=3, columnspan=2)

# Вкладка 2 - Чекбоксы
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()

checkbox1 = tk.Checkbutton(tab2, text="Первый", variable=var1)
checkbox1.grid(row=0, sticky=tk.W)
checkbox2 = tk.Checkbutton(tab2, text="Второй", variable=var2)
checkbox2.grid(row=1, sticky=tk.W)
checkbox3 = tk.Checkbutton(tab2, text="Третий", variable=var3)
checkbox3.grid(row=2, sticky=tk.W)

show_selection_button = tk.Button(tab2, text="Показать выбор", command=show_checkbox_selection)
show_selection_button.grid(row=3)

# Вкладка 3 - Работа с текстом
open_file_button = tk.Button(tab3, text="Открыть файл", command=open_file)
open_file_button.pack()
text_area = tk.Text(tab3)
text_area.pack()
tab_control.pack(expand=1, fill='both')

root.mainloop()
