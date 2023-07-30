# Import necessary packages
import pandas as pd
import os
import warnings

# Ignore all types of warnings
warnings.filterwarnings("ignore", category=FutureWarning, module="pandas", lineno=27)

# Navigate to the folder where your CSV files are 
# os.
# chdir('E:\data science\Data Engneering\ProFintech\MODULE 1\raw_data\Individual_files')
# E:\data science\Data Engneering\ProFintech\MODULE 1\raw_data\Individual_files
path='E:\\data science\\Data Engneering\\ProFintech\MODULE 1\\transformed_data'
# Create an empty dataframe
df = pd.DataFrame()

# os.listdir(path)
indiFiles = os.listdir(path)
# for x in indiFiles:
#   print(x)
# files = [f for f in indiFiles if os.path.isfile(Direc+'/'+f)] #Filtering only the files.
# print(*files, sep="\n")

# Read all CSV files and append them to df
for files in indiFiles:
  try:
    #  for name in files:
      #  print(name)
   print("files:",files)
   df_temp = pd.read_csv(files,encoding='utf-8')
   df = df.append([df,df_temp])
  except:
    pass
# Save df to a CSV file
df.to_csv('Consolidated_mod1.csv')