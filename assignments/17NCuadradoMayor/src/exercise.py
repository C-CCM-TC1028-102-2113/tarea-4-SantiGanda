numfinal=int(input('Escribe un número: '))
check=1
cuad=0

while cuad<numfinal:
    if check<numfinal:
        cuad=check**2
    
    elif check>numfinal:
        break
    check=check+1

print(check-1)



