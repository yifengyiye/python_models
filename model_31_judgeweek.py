# coding:utf-8
"""
题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。
"""
letter = raw_input("please input:")
#while letter  != 'Y':
if letter == 'S' or 's':
    print ('please input second letter:')
    letter = raw_input("please input:")
    if letter == 'a':
        print ('Saturday')
    elif letter  == 'u':
        print ('Sunday')
    else:
        print ('data error')
    
elif letter == 'F' or 'f':
    print ('Friday')
    
elif letter == 'M' or 'm':
    print ('Monday')
    
elif letter == 'T' or 't':
    print ('please input second letter')
    letter = raw_input("please input:")
 
    if letter  == 'u':
        print ('Tuesday')
    elif letter  == 'h':
        print ('Thursday')
    else:
        print ('data error')
        
elif letter == 'W' or 'w':
    print ('Wednesday')
else:
    print ('data error')