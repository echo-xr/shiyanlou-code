
#!/usr/bin/env python3

a=1

while a<101:
    if a%7 == 0:  #7\u7684\u500d\u6570
        pass
    elif a//10 == 7:  # 70\uff0d79
        pass
    elif a%10 ==7:  #\u4e2a\u4f4d\u6570\u662f7
        a = a+1
        continue
    else:
        print(a, end = ' ')
    a = a+1
