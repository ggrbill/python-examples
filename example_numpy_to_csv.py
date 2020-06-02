import numpy as np

def export_to_csv(filename):
	# Creating 3 vectors
	XX = np.arange(0.0,5.0,1.0)
	YY = np.arange(5.0,10.0,1.0)
	ZZ = np.arange(10.0,15.0,1.0)

	# Opening a new csv file
	with open("./files/"+filename+".csv", "w") as f:
		# Writing the vectors as columns 
		f.write(f'x,y,z\n')
		for x, y, z in zip(XX, YY, ZZ):
			f.write(f'{x},{y},{z}\n')

	# Final message
	print(f'CSV File called \'{filename}\' saved.')


if __name__ == '__main__':
    export_to_csv("arrays_in_columns")