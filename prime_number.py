a = int(input("aの値を入力:"))

# TODO
def is_prime(a):
    if a <2:
        return False
    else:
        for i in range(2, a):
            if a%i==0:
                return False
    return True

result=is_prime(a)
print(result)






        

    

        






