a = input("aの値を入力:61")
b = input("bの値を入力:10")

# TODO
n=61
def is_prime(n):
    if n <1:
        return False
    else:
        for i in range(2, n):
            if n%i==0:
                return False
    return True

if is_prime(n):
    print("素数です")
else:
    print("素数ではありません")

#2
n=91
def is_prime(n):
    if n <1:
        return False
    else:
        for i in range(2, n):
            if n%i==0:
                return False
    return True

if is_prime(n):
    print("素数です")
else:
    print("素数ではありません")





        

    

        






