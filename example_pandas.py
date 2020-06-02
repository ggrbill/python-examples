import pandas as pd

def main():
	# reading from a CSV file
	df = pd.read_csv('./files/data.csv', index_col='Component')

	# Adding a new Column called 'name'
	names = ['Nitrogen','Carbon Dioxide','Methane','Ethane','Propane','Iso-Butane', 'Butane', 'Iso-Pentane', 'Pentane', 'Hexane', 'Pseudo-C-7-15', 'Pseudo-C-16-37', 'Pseudo-C-38-80']
	df.insert(0, 'Name', names, True)

	# Printing a Component info (data frame line)
	print(df.loc['iC4'], '\n\n')

	# Printing the number of NANs in each column
	print(df.isnull().sum(), '\n\n')

	# Filling NAN ρL_g_cm3 values to be 0.0
	for series in ['ρL_g_cm3']:
		rho_series = df[series]
		rho_series.fillna(0.0, inplace = True)

	# Add new Column by condition
	condition = lambda x: 'pseudo-component' if 'Pseudo' in x else 'pure-component'
	df['Type'] = df['Name'].apply(condition)

	# Printing the entire DataFrame
	print(df, '\n\n')

	# Printing the DataFrame statistics
	print(df.describe(), '\n\n')

	# Printing data in which MW columns is greater than 100.0 
	print(df[df.MW > 100.0], '\n\n')

	# Saving new CSV file (The enconding is used to save properly the unicode of 'rho')
	df.to_csv('./files/new_data.csv', encoding='utf-8-sig')


if __name__ == '__main__':
    main()
