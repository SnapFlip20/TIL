'''
* How to print elements in list *
'''

lst = ['I', 'am', 'Snapflip', '20']


# 1
print(lst[0], lst[1], lst[2], lst[3])


# 2
print(lst[0] + ' ' + lst[1] + ' ' + lst[2] + ' ' + lst[3])


# 3
for i in range(len(lst)-1):
    print(lst[i], end = ' ')
print(lst[-1])


# 4
for i in lst[0:-1]:
    print(i, end = ' ')
print(lst[-1])


# 5
cnt = 0

while True:
    if cnt == len(lst)-1:
        print(lst[cnt])
        break
    
    print(lst[cnt], end = ' ')
    
    cnt += 1


# 6
print(' '.join(lst))


# 7
print(*lst, sep = ' ')
