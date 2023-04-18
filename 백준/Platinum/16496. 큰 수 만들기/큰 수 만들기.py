n = int(input())

int_list = input().split()

int_list.sort(key=lambda x: x*10, reverse=True)

if int_list[0] == '0':
    print('0')

else:
    print(''.join(int_list))