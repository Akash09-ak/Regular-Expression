import re                        
h=open("regex_sum_707740.txt")
x=[]
s=0
for i in h: 
    i=i.rstrip()
    y=re.findall('[0-9]+',i)
    x=x+y
# print(x)
for i in x:
    s=s+int(i)
print(s)
