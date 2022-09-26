#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

li = MyList()
li.append(1)
li.append(3)
li.append(2)



print(li)

a = li.print_sorted()
print(a)