"""More notes than anything. Could not figure out how to import the csv file."""


import pandas as pd
POKEMON_DATA_CSV_FILE_PATH: str = "../../data/pokemon.csv"

# Setting up the dictionary with str keys and list[int] values
d: dict[str, list[int]] = {'col1': [1, 2], 'col2': [3, 4]}

# Creating the DataFrame from the above structure
df = pd.DataFrame(data=d)

# We do not have to use df.head() (more info to come) here because the DataFrame is quite small (this will not be true going forward)
print(df)

# Reading in the CSV
pokemon = pd.read_csv(POKEMON_DATA_CSV_FILE_PATH)

# Sorting the values rows and resetting their indices
pokemon_sorted = pokemon.sort_values("HP", ascending=True)
pokemon_sorted = pokemon_sorted.reset_index(drop=True)

# Writing the new DataFrame to the new csv
pokemon_sorted.to_csv("pokemon_new.csv", index=False)

# Getting the number of rows in your DataFrame
print(len(pokemon))

# Getting the dimensions of your DataFrame (rows, columns)
pokemon.shape

# Getting a list of the column names in your DataFrame
pokemon.columns

# Provides the most comprehensive overview of the columns in your DataFrame
# also provides the name, count of non-null values and datatype of each column
# as well as some information about memory usage!
pokemon.info()


# Importing numpy
import numpy as np

# Selecting a column using . notation and find the mean HP of the pokemon in our dataset
hp = pokemon.HP
print(np.mean(hp))

# Selecting a column using subscription notation (should be more familiar), also finding the standard deviation using numpy
defense = pokemon["Defense"]
print(np.std(defense))

# Selecting multiple columns, can be useful to "declutter" your data or more directly compare columns
narrowed_pokemon = pokemon[["Name","HP","Attack","Defense"]]
print(narrowed_pokemon.head())

# Selecting columns in a range using .loc() and columns at certian indices using .iloc()
names_and_types = pokemon.loc[:,'Name':'Type 2']
narrowed_pokemon = pokemon.iloc[:,[2,6,7,8]] # note that this achieves the same thing as the subscription notation above!
print(names_and_types.head())
print(narrowed_pokemon.head())

# Filtering columns using .filter(), getting only the columns that start with T
types_and_total = pokemon.filter(regex="^T")
print(types_and_total.head())

# Selecting columns based on data type, only columns of a numeric types
numbers_only = pokemon.select_dtypes(include='number')
print(numbers_only.head())


# Using .head() and tail() to select the first and last 'n' rows respectively (n defaults to 5)
first_5 = pokemon.head(5)
last_5 = pokemon.tail(5)
print(first_5)
print(last_5)

# Filtering rows for a specific Boolean condition, all Pokemon with HP greater than 100
healthy_pokemon = pokemon[pokemon.HP > 100]
print(healthy_pokemon.head())

# Dropping duplicate observations from a DataFrame
no_repeats = pokemon.drop_duplicates()
print(no_repeats.head())

# Randomly sample (select) (1-frac)100% of the rows in the DataFrame
sample_frac = pokemon.sample(frac=0.25)
print(sample_frac.head())

# Randomly sample (select) n of the rows in the DataFrame
sample_n = pokemon.sample(n=10)
print(sample_n)