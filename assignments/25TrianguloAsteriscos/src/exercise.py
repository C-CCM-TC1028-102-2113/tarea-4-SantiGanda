num=int(input('Enter triangle height'))
a=1

while a<=num:
    spaces=num-a
    print(' '*spaces+'*'*a)
    a=a+1

