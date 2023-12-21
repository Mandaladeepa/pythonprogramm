per=int(input('Enter percentage:-'))
if per>=90 and per<=100:
    print('A+')
elif per>=80 and per<=90:
    print('A')
elif per>=70 and per<=80:
    print('B')
elif per>=60 and per<=70:
    print('C')
elif per>=35 and per<=60:
    print('pass')
else:
    print('fail')
