# password checker
import re
items = []
username = input("i dont need ur username but pls enter smg hahaha! ")
p = [x for x in input("now enter ur passwords to be checked! : ").split(',')]

for i in p:
        if (len(i)>=6 or len(i)<=12):
            l = 1
        else:
            l = 0
        if re.search("[a-z]",i):
            a = 1
        else:
            a = 0
        if re.search("[0-9]",i):
            n = 1
        else: 
            n = 0
        if re.search("[A-Z]",i):
            c = 1
        else:
            c = 0
        if re.search("[$#@]",i):
            ch = 1
        else:
            ch = 0

        if l==1 and a==1 and n==1 and c==1 and ch==1:
            items.append(i)
            l = 0
            a = 0
            n = 0
            c = 0
            ch = 0

        
        
if not items:
    print (" no valid pass has found!")
else:
    print(','.join(items))