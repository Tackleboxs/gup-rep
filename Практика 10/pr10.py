with open('Гупалов Владислав Александрович_УБ-31_Ввод.txt', 'r') as file:
    data = file.readlines()
    new = str(data)

with open('Гупалов Владислав Александрович_УБ-31_Вывод.txt', 'w') as file2:
    file2.write(new)