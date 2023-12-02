import tkinter as tk
import requests
import json


def get_repo_info():
    repo_name = entry.get()
    url = f"https://api.github.com/users/{repo_name}"
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
        'name': repo_name,
        'url': url
    }

    with open('result.json', 'w') as file:
        json.dump(result, file)

    label.config(text="Результат получен и сохранен в файл 'result.json'.")


root = tk.Tk()
root.title('Информации о пользователе')
root.geometry('400x300')

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Получить информацию", command=get_repo_info)
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()
