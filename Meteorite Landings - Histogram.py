import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

met_df = pd.read_csv('https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/meteorite-landings/meteorite-landings.csv')

#Find the number of rows and columns in the DataFrame. 
print(met_df.shape)

# Rows containing the year values less than 860 and greater than 2016.
correct_years_df = met_df[(met_df['year'] >= 860) & (met_df['year'] <= 2016)]

# Rows having the 'reclong' values greater than or equal to -180 degrees and less than or equal to 180 degrees.
correct_long_df = correct_years_df[(correct_years_df['reclong'] >= -180) & (correct_years_df['reclong'] <= 180)]

#5. Rows containing the '0 reclat' and '0 reclong' values from the 'correct_long_df'.
correct_lat_long_df = correct_long_df[~((correct_long_df['reclat'] == 0 ) & (correct_long_df['reclong'] == 0))]

# Indices of the rows having missing mass values.
row_indices = correct_lat_long_df[correct_lat_long_df['mass'].isnull() == True].index

# Missing values in the 'mass' column in the 'correct_lat_long_df' DataFrame with median of mass.
median_mass = correct_lat_long_df['mass'].median()
correct_lat_long_df.loc[row_indices, 'mass'] = median_mass

# Convert the 'year' values into an integer type values.
correct_lat_long_df.loc[:, 'year'] = correct_lat_long_df.loc[:, 'year'].astype('int')

# Create a DataFrame for the meteorites fallen between 1970 and 2000 including both.
df=correct_lat_long_df[(correct_lat_long_df["year"]>=1970)&(correct_lat_long_df["year"]<=2000)]
# Create a count plot for the meteorites fallen between 1970 and 2000 including both.
plt.figure(figsize=(18,11))
sns.countplot(x="year",data=df)
plt.show()

#Create a Pandas series containing the year values between 1970 and 2000 including both of them.
met_1970_2000_series=correct_lat_long_df.loc[(correct_lat_long_df['year'] >= 1970) & (correct_lat_long_df['year'] < 2001),"year"]

# Create a histogram for the Pandas series containing the year values between 1970 and 2000 including both of them.
plt.figure(figsize=(10,6))
plt.hist(met_1970_2000_series,bins=10)
plt.grid()
plt.show()
