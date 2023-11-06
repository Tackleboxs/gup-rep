# # 1 Вариант
#
# # 1 Задание
# N = 5
# A = [[-2, 3, 4, -1, 0],
#      [5, -6, 7, 8, -9],
#      [10, 11, -12, 13, 14],
#      [15, -16, 17, -18, 19],
#      [20, 21, 22, -23, -24]]
# s = 0
# k = 0
# for i in range(N):
#     for j in range(i+1, N):
#         if A[i][j] > 0:
#             s += A[i][j]
#             k += 1
# print(s)
# print(k)
#
# 2 Задание
#
# N = 3
# M = 4
# A = [[1, 2, 3 ,4],
#      [5, 6 , 7 ,8],
#      [9, 10, 11, 12]]
# for i in range(N):
#     mx = A[i][0]
#     mn = A[i][0]
#     for j in range(M):
#         if A[i][j] > mx:
#             mx = A[i][j]
#         if A[i][j] < mn:
#             mn = A[i][j]
#     A[i][0], A[i][M-1] = mx, mn
# for r in A:
#     print(r)