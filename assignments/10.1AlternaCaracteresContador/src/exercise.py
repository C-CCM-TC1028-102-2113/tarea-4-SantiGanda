
num=int(input())
carct=1
simb=1 
a=1

while a<=num:
    if simb%2!=0:
        value='#'
    elif simb%2==0:
        value='%'
    print(str(carct)+'-'+str(value))
    carct=carct+1
    simb=simb+1
    a=a+1


