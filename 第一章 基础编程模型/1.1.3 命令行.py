# 编写一个程序，从命令行得到三个整数参数。如果它们都相等则打印equal，否则打印not equal


import sys
if int(sys.argv[1]) ==  int(sys.argv[2]) & int(sys.argv[1]) == int(sys.argv[3]):
    print('equal')
else:
    print('not equal')
