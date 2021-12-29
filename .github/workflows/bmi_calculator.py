import json
import os
import pandas as pd

script_path = os.path.abspath(__file__)
script_dir = os.path.split(script_path)[0]

data = open(script_dir+'/data.json')
data = json.load(data)
df = pd.json_normalize(data)

df['Height_in_mts'] = df['HeightCm']/100
df['body_mass_index'] = df['WeightKg']/df['Height_in_mts']**2

for index,row in df.iterrows():
    if row.body_mass_index >= 40:
        df.loc[index,'BMI Category'] = "Very severely obese"
        df.loc[index,'Health Risk'] = "Very high risk"
    elif row.body_mass_index <= 39.9 and row.body_mass_index >= 35:
        df.loc[index,'BMI Category'] = "Severely obese"
        df.loc[index,'Health Risk'] = "High risk"
    elif row.body_mass_index <= 34.9 and row.body_mass_index >= 30:
        df.loc[index,'BMI Category'] = "Moderately obese"
        df.loc[index,'Health Risk'] = "Medium risk"
    elif row.body_mass_index <= 29.9 and row.body_mass_index >= 25:
        df.loc[index,'BMI Category'] = "Overweight"
        df.loc[index,'Health Risk'] = "Enhanced risk"
    elif row.body_mass_index <= 24.9 and row.body_mass_index >= 18.5:
        df.loc[index,'BMI Category'] = "Normal Weight"
        df.loc[index,'Health Risk'] = "Low risk"
    elif row.body_mass_index <= 18.4 and row.body_mass_index >= 0:
        df.loc[index,'BMI Category'] = "Underweight"
        df.loc[index,'Health Risk'] = "Malnutrition risk"
    else:
        print("Cannot calculate BMI")

df2 = df[['Gender','HeightCm','WeightKg','BMI Category','Health Risk']]
print(df2)
overweight = df2.apply(lambda x : True
            if x['BMI Category'] == "Overweight" else False, axis = 1)

num_rows = len(overweight[overweight == True].index)
print("Number of overweight persons:",num_rows)

