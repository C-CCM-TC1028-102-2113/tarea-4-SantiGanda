
num=0
divisor=0
suma=0

while True:
    num=float(input())
    if num>-1:
        suma=suma+num
        divisor=divisor+1
    elif num<=-1:
        break

print(suma/divisor)

