import numpy as np
x = np.arange(0.0,5.0,1.0)
y = np.arange(5.0,10.0,1.0)
z = np.arange(10.0,15.0,1.0)

filename = "./files/arrays_in_columns.csv"
f = open(filename, "w")

f.write(f'a,b,c\n')
for v in zip(x, y, z):
	f.write(f'{v[0]},{v[1]},{v[2]}\n')

f.close()

print(f' File {filename} saved.')
