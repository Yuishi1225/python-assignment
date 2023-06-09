text = "How I want a drink, alcoholic of course, after the heavy chapters involving quantum mechanics. All of thy geometry, Herr Planck, is fairly hard."

# TODO


import re

re.split('[./,/ ]+', text)

a=re.split('[./,/ ]+', text)
b=''
c=','
d='.'
e=' '

for item in [b, c, d, e]:
    while item in a:
        a.remove(item)

list(map(len,a))
a=list(map(len,a))
list(map(str, a))
a=list(map(str, a))
result="".join(a)

print(result)






    
