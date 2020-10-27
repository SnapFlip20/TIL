'''
* How to print elements in list *

all the output is same as: 'I am SnapFlip 20',
and there is no blank at the end of the line.
'''

lst = ['I', 'am', 'SnapFlip', '20']


# 1 (simple but we must edit that line when the number of lst[n] change.)
print(lst[0], lst[1], lst[2], lst[3])


# 2 (this method is inefficient :< )
print(lst[0] + ' ' + lst[1] + ' ' + lst[2] + ' ' + lst[3])


# 3 (I used this method when I first learned algorithm in python.)
for i in range(len(lst)-1):
    print(lst[i], end = ' ')
print(lst[-1])


# 4 (umm......)
for i in lst[0:-1]:
    print(i, end = ' ')
print(lst[-1])


# 5 (using while loop)
cnt = 0

while True:
    if cnt == len(lst)-1:
        print(lst[cnt])
        break
    
    print(lst[cnt], end = ' ')
    
    cnt += 1


# 6 (' '.join() can merge elements in list separated on a blank)
print(' '.join(lst))


# 7 (I love this method.)
print(*lst, sep = ' ')
