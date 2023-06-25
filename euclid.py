a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO

def gcd(c,d):
    while d != 0:
        c, d= d, c%d
    print(c)

gcd(10, 20)
gcd(14, 91)
gcd(91, 14)




