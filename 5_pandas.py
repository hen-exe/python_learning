import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 3 Data Structures 
# > Series (1D), DataFrame (2D), Panel (3D)

# Series
print("====Series====")
data_series = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(data_series)
print (s)

s = pd.Series(data_series, index=[10, 20, 30 , 40])
print (s)

data_dict = {'a' : 0, 'b' : 1, 'c' : 2}
s = pd.Series(data_dict)
print (s)

#DataFrame
print("====DataFrame====")
data_df = [1, 2, 3, 4, 5]
df = pd.DataFrame(data_df)
print (df)

data_df = [['Alex', 10], ['Bob', 12], ['Clarke', 13]]
df = pd.DataFrame(data_df, columns=['Name', 'Age'])
print (df)

df['Address'] = pd.Series(['HG', 'PH', 'ML'])
print (df)

# Concat columns
df['Combo'] = df['Name'] + df['Address']
print(df)

del df['Age'] #or use df.pop
print(df)

# export to csv, JSON, Excel, txt
# df.to_csv("kids.csv", index=False)


# importing csv
print("====Importing====")
days = pd.read_csv(r"C:\Users\flora\OneDrive\Desktop\elinnov\Code\python_learning\day.csv", index_col=0)

print(days.info())
print(days.head(10)) #returns headers and rows 
print(days.tail())

# importing text 
text = pd.read_csv(r"C:\Users\flora\OneDrive\Desktop\elinnov\Code\python_learning\sample.txt", sep="\t") # separator argument, wat separates rows
print(text)

# ======CLEANING DATA========

# remove empty cells
print('======ORIGINAL DATASET======')
data_orig = pd.read_csv(r"C:\Users\flora\OneDrive\Desktop\elinnov\Code\python_learning\data.csv")
print (data_orig)

print('======CLEANED DATASET======')
# remove empty rows and NULL values | inplace does not return a copy  
# data_orig.dropna(inplace=True)
data_clean_1 = data_orig.dropna() 
print(data_clean_1)

# replace empty values
data_clean_2 = data_orig['Date'].fillna("'2020/12/1'")
print(data_clean_2)

# convert date wrong format
data_orig['Date'] = pd.to_datetime(data_orig['Date'], errors='coerce')
print(data_orig)

# replacing values
data_orig.loc[7, "Duration"] = 45
print(data_orig)

for x in data_orig.index:
    if data_orig.loc[x, "Duration"] > 60:
        data_orig.loc[x, "Duration"] = 60

# duplicate values
print(data_orig.duplicated())

data_clean_3 = data_orig.drop_duplicates()

print(data_clean_3)


# ======DATA ANALYSIS========

# correlations
data_analysis = pd.read_csv(r"C:\Users\flora\OneDrive\Desktop\elinnov\Code\python_learning\analysis.csv")
print(data_analysis)
print(data_analysis.corr())

# plotting
    # data_analysis.plot()

    # data_analysis.plot(kind="scatter", x="Duration", y="Calories")

    # data_analysis['Duration'].plot(kind="hist")
    # plt.show()


# summary operators
print("======== MEAN, MEDIAN, MODE ========")
print(data_analysis.mean())
print(data_analysis.mode())
print(data_analysis.median())