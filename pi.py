text = "How I want a drink, alcoholic of course, after the heavy chapters involving quantum mechanics. All of thy geometry, Herr Planck, is fairly hard."

# TODO


import re

re.split('[./,/ ]+', text)

a=re.split('[./,/ ]+', text)
b=''
c=','
d='.'
e=' '
if b or c or d or e in a:
    while b or c or d or e in a:
     a.remove(''), a.remove(' '),a.remove(','),a.remove('.')
     if b and c and d and e not in a:
        break
     print(a)

list(map(len,a))
a=list(map(len,a))
list(map(str, a))
a=list(map(str, a))
"".join(a)






    
