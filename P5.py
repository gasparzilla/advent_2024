import re

with open("input_5.txt", 'r') as file:
    a= file.read()
    
regex_mul = "\d+\|\d+"
rules = re.findall(regex_mul, a)
rules = list(map(lambda x: x.split('|'), rules))

before = {}
after = {}

for r in rules:
    try:
        before[r[0]] += [r[1]]
    except:
        before[r[0]] = [r[1]]
    try:
        after[r[1]] += [r[0]]
    except:
        after[r[1]] = [r[0]]

pages = a.splitlines()[a.splitlines().index("")+1:]
pages = list(map(lambda x: x.split(','), pages))

def list_in(l1,l2):
    for i in l1:
        if i not in l2:
            return False
    return True

clas = []
res = 0

for ps in pages:
    ok = True
    for i in range(len(ps)):
        p = ps[i]
        ok = ok and list_in(ps[:i],after[p]) and list_in(ps[i+1:],before[p])
    clas += [ok]
    if ok:
        res += int(ps[int(len(ps)/2)])
        
