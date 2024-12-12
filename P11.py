# import multiprocessing
# pool = multiprocessing.Pool()
# from defs import blink

with open("input_11.txt", 'r') as file:
    a= file.read()
    
def blink(s):
    if s == '0':
        return ['1']
    if len(s)%2 == 0:
        r=s[int(len(s)/2):]
        l=s[:int(len(s)/2)]
        return [str(int(l)),str(int(r))]
    else:
        return [str(int(s)*2024)]

stones = a.split()

# result = sum(list(pool.map(blink, stones)), [])
result = sum(list(map(blink, stones)), [])

for i in range(24):
    print(i, len(result))
    # result = sum(list(pool.map(blink, result)), [])
    result = sum(list(map(blink, result)), [])
    
len(result)