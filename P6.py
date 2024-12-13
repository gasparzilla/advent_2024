import copy

with open("input_6.txt", 'r') as file:
    a= file.read().splitlines()

aa = list(map(lambda x: list(x), a))
bb = aa.copy()

directions = [">", "^", "<", "v"]
rot = [(0,1), (-1,0), (0,-1), (1,0)]

def find_start(floor):
    for i in range(len(floor)):
        for j in range(len(floor[0])):
            if floor[i][j] in directions:
                return (i,j)

def step(floor, x):
    dir_i = directions.index(floor[x[0]][x[1]])
    dir = rot[dir_i]
    if (x[0]+dir[0] <0 or x[0]+dir[0] > 129) or (x[1]+dir[1] < 0 or x[1]+dir[1] > 129):
        floor[x[0]][x[1]] = 'O'
        return (-1,-1)
    elif floor[x[0]+dir[0]][x[1]+dir[1]] == '#':
        floor[x[0]][x[1]] = directions[(dir_i-1)%4]
        return x
    else:
        floor[x[0]][x[1]] = 'O'
        next = tuple(map(lambda i, j: i + j, x, dir))
        floor[next[0]][next[1]] = directions[dir_i]
        return next

start_position = find_start(aa)

while start_position != (-1,-1):
    start_position = step(aa,start_position)
    
def show_map(floor):
    for i in range(len(floor)):
        for j in range(len(floor[0])):
            print(floor[i][j], end='')
        print('')

def count_unique(floor):
    N = 0
    for i in range(len(floor)):
        for j in range(len(floor[0])):
            if floor[i][j] == 'O':
                N += 1
    return N

count_unique(aa)

def is_loop(floor):
    loops = 0
    start_position = find_start(floor)
    start_dir = floor[start_position[0]][start_position[1]]
    position = start_position
    while position != (-1,-1):
        position = step(floor,position)
        loops += 1
        if (loops >= 50000):
            return 1
    return 0

NLoops = 0
for i in range(len(bb)):
        for j in range(len(bb[0])):
            print(i,' ',j)
            cc = copy.deepcopy(bb)
            start_position = find_start(cc)
            if (i,j) != start_position:
                cc[i][j] = '#'
                NLoops += is_loop(cc)
                
                
print(NLoops)