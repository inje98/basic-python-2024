# file : test19_starprint.py
# desc : 별찍기 또는 피라미드 만들기

# for i in range(1,6):
#     for j in range(i):
#         print('*', end ='')
#     print()


# for i in range(1, 6):
#     for j in range(6 - i):
#         print('*', end = '')
#     print()

for h in range(3):
    for i in range(1,6):
        for j in range(5-i):
            print(' ', end = '')
        for j in range(2*i-1):
            print('*', end = '')
        print()    