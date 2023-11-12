# # Блок А
# #
# # 3 Задание
# def r(x):
#     if x > 0:
#        print(x%10)
#        r(x//10)
# r(8841)
#
# # Блок Б
# def num():
#     n = int(input())
#     if n == 0:
#         return 0, 0
#     else:
#         one, two = num()
#     if n > one:
#         return n, one
#     elif n > two:
#         return one, n
#     else:
#         return one, two
# _, top = num()
# print(top)