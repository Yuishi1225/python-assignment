text = "How I want a drink, alcoholic of course, after the heavy chapters involving quantum mechanics. All of thy geometry, Herr Planck, is fairly hard."

# TODO


import re

re.split('[./,/ ]+', text)

a=re.split('[./,/ ]+', text)
b=''
while b in a:
    a.remove('')
print(a)

    
