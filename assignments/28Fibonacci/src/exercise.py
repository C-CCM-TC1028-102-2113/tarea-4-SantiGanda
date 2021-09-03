num1=0
num2=1
num3=0
index=0
numfinal=int(input('Enter a number: '))



while index<numfinal:
    num3=num1+num2
    num1=num2
    num2=num3
    index=index+1

print(num1)
