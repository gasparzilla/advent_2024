import itertools

with open("input_4.txt", 'r') as file:
    a= file.read().splitlines()

aa = list(map(lambda x: list(x), a))

directions = list(itertools.product([0,1,-1],[0,1,-1]))

def check_xmas(text,i,j):
    n = 0
    for d in directions:
        word = ''
        for w in range(4):
            try:
                if (i+w*d[0] >= 0) and (j+w*d[1] >= 0) :
                    word += text[i+w*d[0]][j+w*d[1]]    
            except:
                break
        # print(word)
        if word == 'XMAS':
            n+=1
    return n

def check_x_mas(text,i,j):
    word_1 = ''
    word_2 = ''
    for k in [-1,0,1]:
        try:
            if (i+k >= 0) and (j+k) >=0 and (j-k)>=0:
                word_1 += text[i+k][j+k]
                word_2 += text[i+k][j-k]
        except:
            break
    if (word_1 == 'MAS' or word_1 == 'SAM') and (word_2 == 'MAS' or word_2 == 'SAM'):
        return 1
    return 0        

total = 0

for i in range(len(aa)):
    for j in range(len(aa[0])):
        if aa[i][j] =="X":
            total += check_xmas(aa,i,j)

total = 0

for i in range(len(aa)):
    for j in range(len(aa[0])):
        if aa[i][j] =="A":
            total += check_x_mas(aa,i,j)
            