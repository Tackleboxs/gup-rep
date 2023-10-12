# # Задание 1
# t = input()
# t = t.split()
# k = 0
# for n in t:
#     if n[0] == "е" or n[0] == "Е": #В задание "е" с маленькой, но уточнить не могу, взял обе
#         k = k+1;
# print (k,t)

# # Задание 2
# t = input()
# k = 0
# for n in t:
#     if n == ':':
#         k = k + 1
#         t = t.replace(":",'%')
# print(k,t)

# # Задание 3
# t = input()
# k = 0
# for n in t:
#     if n == '.':
#         k = k + 1
#         t = t.replace(".","")
# print(k)

# # Задание 4
# t = input()
# k = 0
# for n in t:
#     if n == 'а':
#         k = k + 1
#         t = t.replace("а","о")
# print(k,len(t))

# # Задание 5
# t = input()
# t1 = t.lower()
# print(t1)

# # Задание 6
# t = input()
# k = 0
# for n in t:
#     if n == 'а':
#         k = k + 1
#         t = t.replace("а","")
# print(k,t)

# # Задание 10
# t = input()
# print(t.title())

# # Задание 12
# t = input()
# for n in t.split():
#     if n[-1] == 'я':
#         print(n)

# # Задание 13
# t = input()
# print(t[t.find('(') + 1:t.find(')')])

# # Задание 14
# t = input()
# for n in t.split():
#     if n [0] == 'а' or n[-1] == 'я' :
#         print(n)

# # Задание 15
# t = input()
# n = t.count('т')
# print(n)