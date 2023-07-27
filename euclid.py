a =int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

# TODO

def gcd(a,b):
    while b != 0:
        a, b= b, a%b
    return a

print (gcd(a,b))
    

print(gcd(10, 20))
print(gcd(14, 91))
print(gcd(91, 14))

#4問目

def gcd(a,b):
    while b != 0:
        a, b= b, a%b
    return a==1 








