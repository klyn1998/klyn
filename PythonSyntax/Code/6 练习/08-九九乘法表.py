# j = 0
# while j < 9:
#     j += 1
#     i = 0
#     while i < j:
#         i += 1
#         print('*', end=' ')
#     print()

for i in range(1, 10):
    for j in range(1, i + 1):
        print(j, '*', i, '=', i * j, end=' ', sep='')
    print()
