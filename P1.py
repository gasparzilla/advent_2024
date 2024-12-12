import pandas as pd

input = pd.read_csv("input_1.txt", sep = ' ', header=None, names=["a", "b","c", "d"])

a = input["a"].copy()
b = input["d"].copy()

a = a.sort_values().reset_index(drop=True)
b = b.sort_values().reset_index(drop=True)

c = abs(a-b)
sol1 = sum(c)

a2 = a.map(lambda x:len(b[b==x]))
sol2 = sum(a2*a)