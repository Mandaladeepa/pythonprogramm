l=[1,9,11,23,65,78,43]
sum=0
pro=1
if len(l)%2==0: 
    for i in l:
        sum=sum+i
    print(sum)
else:
    for i in l:
        pro=pro*i
    print(pro)
