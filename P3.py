import re

with open("input_3.txt", 'r') as file:
    a= file.read()

regex_mul = "mul\(\d+,\d+\)"
regex_mul_2 = "mul\(\d+,\d+\)|do\(\)|don't\(\)"

mults = re.findall(regex_mul, a)

m_i = list(map(lambda x: x.split("do()"),"".join(re.findall(regex_mul_2, a)).split("don't")))
m_ii = sum(m_i, [])
mults_3 = re.findall(regex_mul, "".join([x for x in m_ii if x[0]!="("]))

def mul(texto):
    t = texto.strip('mul(').strip(')').split(',')
    return int(t[0])*int(t[1])

sum(map(lambda x: mul(x), mults))
sum(map(lambda x: mul(x), mults_3))
