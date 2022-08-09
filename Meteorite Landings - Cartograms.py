import numpy as np
import pandas as pd
import folium
import matplotlib.pyplot as plt
met_df = pd.read_csv('https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/meteorite-landings/meteorite-landings.csv')
# Rows containing the year values less than 860 and greater than 2016
correct_years_df = met_df[(met_df['year'] >= 860) & (met_df['year'] <= 2016)]
# Rows having the 'reclong' values greater than or equal to -180 degrees and less than or equal to 180 degrees.
correct_long_df = correct_years_df[(correct_years_df['reclong'] >= -180) & (correct_years_df['reclong'] <= 180)]
# Rows containing the 0 'reclat' and 0 'reclong' values from the 'correct_long_df'.
correct_lat_long_df = correct_long_df[~((correct_long_df['reclat'] == 0) & (correct_long_df['reclong'] == 0))]
# List of the indices of above rows.
row_indices = correct_lat_long_df[correct_lat_long_df['mass'].isnull() == True].index
# Missing values in the 'mass' column in the 'correct_lat_long_df' DataFrame with median of mass.
correct_lat_long_df.loc[row_indices, 'mass'] = correct_lat_long_df['mass'].median()
#Convert the 'year' values into integer type values.
correct_lat_long_df['year']=correct_lat_long_df['year'].astype("int")

#There are 69 meteorites found which have withered due to the prolonged exposure to probably the extreme weather conditions, creating a dataframe and cartogram of those
found_relict_df=correct_lat_long_df[(correct_lat_long_df["fall"]=="Found")&(correct_lat_long_df["nametype"]=="Relict")]
map1=folium.Map(location=[0,0],width="90%",height="90%",zoom_start=1,tiles="Stamen Toner")
for i in found_relict_df.index:
    folium.Marker(location=[found_relict_df.loc[i,"reclat"],found_relict_df.loc[i,"reclong"]],popup=found_relict_df.loc[i,"name"]).add_to(map1)
print(map1)

#30,871 meteorites were found in good condition. Creating a dataframe and cartogram for those found after 2010
found_valid_df=correct_lat_long_df[(correct_lat_long_df["fall"]=="Found")&(correct_lat_long_df["nametype"]=="Valid")]
years=found_valid_df[found_valid_df["year"]>2010]
map2=folium.Map(location=[0,0],width="90%",height="90%",zoom_start=1,tiles="Stamen Toner")
for i in years.index:
    folium.Marker(location=[years.loc[i,"reclat"],years.loc[i,"reclong"]],popup=years.loc[i,"name"]).add_to(map2)
print(map2)


