#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

li = MyList()


li.append("b")
li.append("a")
li.append("m")


print(li)

li.print_sorted()
