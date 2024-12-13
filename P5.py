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

def check_order(ps):
    ok = True
    for i in range(len(ps)):
        p = ps[i]
        ok = ok and list_in(ps[:i],after[p]) and list_in(ps[i+1:],before[p])
    return ok

def fix_order(ps):
    for i in ps:
        # l = 0
        order = []
        r = 0
        for j in ps:
            if i != j:
                # l += j in before[i]
                r += j in after[i]
            order += [r]
    # return [x for _, x in sorted(zip(order, ps))]
    return order

clas = []
res = 0
res_2 = 0

for ps in pages:
    ok = check_order(ps)
    clas += [ok]
    if ok:
        res += int(ps[int(len(ps)/2)])
    else:
        ps_o = fix_order(ps)
        res_2 += int(ps_o[int(len(ps_o)/2)])
        
print(res)

print(res_2)

test = pages[56]
test
fix_order(test)
check_order(test)
# check_order(fix_order(test))