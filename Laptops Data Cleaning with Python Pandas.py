#In these project based exercises fundamental Data Cleaning operations are applied in Python Pandas to clean laptops data.

#Fundamental data cleaning operations used to clean the data:
#• Loading csv files with encodings
#• Using a definition and for-loop to clean column names from characters and change it to snake case.
#• Extracting string 0 as new names.
#• Replacing / (stripping columns from substrings) substrings in column entries with ‘nothing’ and converting the column datatype to numerical.
#• Using a mapping dictionary to correct bad values.
#• Dropping or filling missing values.
#• Cleaning a string column.
#• Saving the cleaned data to a new csv file.

# The Python exercises in Pandas were done through DataQuest and they also provided the dataset laptops.csv.


import pandas as pd

# Reading CSV Files with Encodings:

laptops = pd.read_csv("laptops.csv", encoding = "Latin-1")
laptops.info()

# Cleaning Column Names (changing the column names to snake case and getting rid of characters used):

def clean_col(col):
    col = col.strip()
    col = col.replace("Operating System", "os")
    col = col.replace(" ", "_")
    col = col.replace("(", "")
    col = col.replace(")", "")
    col = col.lower()
    return col

new_columns = []

for c in laptops.columns:
    clean_c = clean_col(c)
    new_columns.append(clean_c)
    
laptops.columns = new_columns
print(laptops.columns)


# Converting String Columns to Numeric datatypes (removing non-digit characters):

ram = laptops["ram"]
unique_ram = ram.unique()

laptops["ram"] = laptops["ram"].str.replace('GB','').astype(int)
ram = laptops["ram"]
unique_ram = ram.unique()
# Which other columns needs to be changed to numeric?  Viewing the datatypes:
laptops.dtypes

laptops['screen_size'] = laptops['screen_size'].str.strip('"').astype(float)


# Renaming Columns

laptops.rename({"ram":"ram_gb"}, axis = 1, inplace = True)
ram_gb = laptops["ram_gb"]

laptops.rename({"screen_size": "screen_size_inches"}, axis = 1, inplace = True)
screen_size = laptops["screen_size_inches"]

# Descriptive Statistics for the Columns:
ram_gb_desc = ram_gb.describe()
screen_size_desc = screen_size.describe()


# Extracting Values from Strings
# Extracting string 0 (the first string):

laptops["gpu_manufacturer"] = (laptops["gpu"].str.split().str[0])
laptops["cpu_manufacturer"] = (laptops["cpu"].str.split().str[0])

cpu_manufacturer = laptops["cpu_manufacturer"]
# Count for each CPU Manufacturer:
cpu_manufacturer_counts = cpu_manufacturer.value_counts()


# Correcting Bad Values using a mapping dictionary:

mapping_dict = {
    'Android': 'Android',
    'Chrome OS': 'ChromeOS',
    'Linux': 'Linux',
    'Mac OS': 'macOS',
    'No OS': 'NoOS',
    'Windows': 'Windows',
    'macOS': 'macOS'
}
os = laptops["os"]

laptops["os"] = os.map(mapping_dict)


# Dropping Missing Values:

laptops_no_null_rows = laptops.dropna()
laptops_no_null_cols = laptops.dropna(axis = 1)

# Filling Missing Values:

value_counts_before = laptops.loc[laptops["os_version"].isnull(), "os"].value_counts()
laptops.loc[laptops["os"] == "macOS", "os_version"] = "X"

no_os = laptops["os"] == "NoOS"
laptops.loc[no_os, "os_version"] = "Version Unknown"
value_counts_after = laptops.loc[laptops["os_version"].isnull(), "os"].value_counts()


# Cleaning a String Column:

weight_unique = laptops["weight"].unique()
laptops["weight"] = laptops["weight"].str.replace("kgs","").str.replace("kg","").astype(float)
laptops.rename({"weight":"weight_kg"}, axis = 1, inplace = True)


# Saving the Cleaned Data to a new CSV file:

laptops.to_csv("laptops_clean.csv", index = False)


