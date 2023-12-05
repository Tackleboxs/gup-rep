import tkinter as tk
import requests
import json


def get_info():
    name = entry.get()
    url = f"https://api.github.com/users/{name}"
    response = requests.get(url)
    data = response.json()

    if 'company' in data:
        company = data['company']
    else:
        company = ""

    if 'created_at' in data:
        created_at = data['created_at']
    else:
        created_at = ""

    if 'email' in data:
        email = data['email']
    else:
        email = ""

    if 'id' in data:
        id = data['id']
    else:
        id = ""

    if 'url' in data:
        url = data['url']
    else:
        url = ""

    result = {
        'company': company,
        'created_at': created_at,
        'email': email,
        'id': id,
        'name': name,
        'url': url
    }

    with open('result.json', 'w') as file:
        json.dump(result, file)

    label.config(text="Результат получен и сохранен в файл 'result.json'.")


win = tk.Tk()
win.title('Информация о пользователе')
win.geometry('400x300')

entry = tk.Entry(win)
entry.pack()

button = tk.Button(win, text="Получить информацию", command=get_info)
button.pack()

label = tk.Label(win, text="")
label.pack()

win.mainloop()
