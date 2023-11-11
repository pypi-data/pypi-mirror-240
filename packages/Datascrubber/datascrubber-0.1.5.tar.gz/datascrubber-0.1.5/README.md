# Datascrubber Module Documentation
## Overview
This documentation explains the functions available in the ***`Datascrubber`*** package, which is designed to assist in data cleaning and analytics tasks 

## Creating the an instance
Through this process, we are calling our class which will help us access the various functions to be used.

```python
from Datascrubber import Datacleaning
data_cleaner = Datacleaning()
```
### OR 
```python
from Datascrubber.datacleaning import Datacleaning
data_cleaner = Datacleaning()
```

So for all the remaining part of our code, we shall be using the data_cleaner.
## Table of Contents
- read_data
- columns
- head
- summary
- missing_values
- drop_missing_values
- col_missing_value
- remove_empty_columns
- data_types
- cat_cols
- cont_cols
- distributions
- data_types
- col_dist
- cat_dist
- col_cat_dist
- remove_missingvalues
- drop
- outliers
- outliers_single
- remove_outliers
- remove_outliers_single
- corr_matrix
- cont_corr
- cont_to_cont
- cat_to_cat
- countplot
- contingency_table
- Chi_square
- combined_boplot
- singleAnova
- cont_to_cat
- lineplot
- getdata
- data_cleaning

<a name="#read_data"></a>
## read_data
### Function Name: read_data
This function is used to read data from a file. It supports reading data from a CSV file, Excel file, and a JSON file. The function automatically detects the file type and reads the data accordingly.
<br />
Then it gives an explanation of the data that has been read. This includes the number of rows and columns in the data, the number of numeric and categorical columns, and the number of missing values in each column.

#### Parameters
- `file_path`: The path to the file containing the data. This must be a string input.

#### Return Value
- Returns a dataframe containing the data from the file.

#### Usage Example
```python
data_clener.read_data("file_path") # replace file_path with the directory of the file.
```

<a name="#columns"></a>
## columns
### Function Name: columns
This function returns the columns of the loaded dataset.

#### Parameters
None

#### Return Value
- Returns a list of column names in the dataset.

#### Usage Example
```python
data_cleaner.columns()

```
##### OR

```python
columns_list = data_cleaner.columns()
print("Columns:", columns_list)
```

<a name="#head"></a>
## head
### Function Name: head
This function is used to display the first few rows of the data. It is useful to get a quick overview of the data.

#### Parameters
- `number`: The number of rows to display.

#### Return Value
- Returns a dataframe containing the first few rows of the data.

#### Usage Example
```python
data_cleaner.head(number=5) # replace number with the number of rows to display.

```
- It is also valid not to include `number`in parameter and instead just subsititute with an integer or float.
<a name="#summary"></a>
## summary 
### Function Name: summary
This function is used to generate summary statistics of the data. It provides valuable information about the distribution, central tendency, and spread of the data. It calculates statistics for each numeric column in the data. 

The statistics provided by the summary function include:

- Count: The number of non-null values in the column.
- Mean: The arithmetic mean (average) of the values.
- Standard Deviation: A measure of the spread or dispersion of the values.
- Minimum: The minimum value in the column.
- 25th Percentile (Q1): The value below which 25% of the data falls.
- 50th Percentile (Median or Q2): The middle value of the data.
- 75th Percentile (Q3): The value below which 75% of the data falls.
- Maximum: The maximum value in the column.

Then to a `categorical column`, The summary function generates statistics such as:

- Count: The number of non-null values in the column.
- Unique: The number of unique categories or levels in the column.
- Top: The most frequent category in the column.
- Freq: The frequency of the top category.
#### Parameters
None

#### Return Value
- Returns a dataframe containing the summary statistics of the data.

#### Usage Example
```python
data_cleaner.summary()
```
<a name="#missing_values"></a>

## missing_values
### Function Name: missing_values
This function is used to check for missing values in the data. 

#### Parameters
None

#### Return Value
- Returns a dataframe containing the number of missing values in each column.

#### Usage Example
```python

data_cleaner.missing_values()

```
<a name="#col_missing_value"></a>

## col_missing_value
### Function Name: col_missing_value
This function is used to check for missing values in a specific column.

#### Parameters
- `col_name`: The name of the column to check for missing values. The column name must be entered as as a string.

#### Return Value
- Returns the number of missing values in the specified column.

#### Usage Example
```python

data_clener.col_missing_value("col_name") #replace col_name with the column name.

```
<a name="#remove_empty_columns"></a>

## remove_empty_columns
### Function Name: remove_empty_columns
This function is used to remove columns that have no values. It is useful to remove columns that have no values as they do not provide any useful information.

#### Parameters
None

#### Return Value
None

#### Usage Example
```python

data_cleaner.remove_empty_columns()

```	
`Note:` This function is also automatically called by the `remove_missingvalues` function hence for predictive situations, one can put the column back after cleaning.

<a name="#data_types"></a>
## data_types
### Function Name: data_types
This function is used to check the data types of the columns and the creates subsets of the data based on the data types. It creates a subset of the data containing only the categorical columns and another subset containing only the numeric columns.

#### Parameters
None

#### Return Value
None
`Note:` This function maynot  necessarily be used as it is called in the background by other functions. 

<a name="#cat_cols"></a>

## cat_cols
### Function Name: cat_cols
This function is used to get the categorical columns in the data.

#### Parameters
None

#### Return Value
- Returns a dataframe of the categorical columns in the data.

#### Usage Example
```python

data_cleaner.cat_cols()

```	
<a name="#cont_cols"></a>

## cont_cols
### Function Name: cont_cols
This function is used to get the numeric columns in the data.

#### Parameters
None

#### Return Value
- Returns a dataframe of the numeric columns in the data.

#### Usage Example
```python

data_cleaner.cont_cols()

```	
<a name="#distributions"></a>

## distributions
### Function Name: distributions
This function is used to plot the distribution of the numeric columns in the data. It plots a histogram for each numeric column in the data.

It is useful to get an idea of the distribution of the data. It can be used to identify outliers and skewness in the data.

#### Parameters
None

#### Return Value
None

#### Usage Example
```python

data_cleaner.distributions()

```	
<a name="#col_dist"></a>

## col_dist
### Function Name: col_dist
This function is used to plot the distribution of a specific numeric column in the data.

#### Parameters
- `col`: The name of the column to plot the distribution for.

#### Return Value
None

#### Usage Example
```python

data_cleaner.col_dist("col") #replace col with the column name.

```	
<a name="#cat_dist"></a>

## cat_dist
### Function Name: cat_dist
This function is used to plot the distribution of a all categorical columns in the data.

#### Parameters
None

#### Return Value
None
#### Return Value
None

#### Usage Example
```python

data_cleaner.cat_dist()

```	
<a name="#col_cat_dist"></a>

## col_cat_dist
### Function Name: col_cat_dist
This function is used to plot the distribution of a specific categorical column in the data.

#### Parameters
- `col`: The name of the column to plot the distribution for.

#### Return Value
None

#### Return Value
None

#### Usage Example
```python

data_cleaner.col_cat_dist("col") #replace col with the column name.

```	
<a name="#remove_missingvalues"></a>

## remove_missingvalues
### Function Name: remove_missingvalues
This function is used to remove deal with rows that have  missing values (NA). 
The funcion first removes all the duplicates that are within the data and also automatically removes all the empty columns.

The missing values are then replaced with the mode of the column (`the most occuring value`) for categorical columns.

For numeric columns, the missing values are replaced with either the mean or median of the column depending on the skewness of the data.


#### Parameters
None

#### Return Value
None

#### Usage Example
```python

data_cleaner.remove_missingvalues()

```	
<a name="#drop_missingvalues"></a>

## drop_missing_values
### Function Name: drop_missing_values
This function is used to remove rows that have  missing values (NA). 
The funcion first removes all the duplicates that are within the data and also automatically removes all the empty columns.

The missing values are totally removed from the data.


#### Parameters
None

#### Return Value
None

#### Usage Example
```python

data_cleaner.drop_missing_values()

```	
## drop
### Function Name: drop
This function is used to drop columns from the data.

#### Parameters
- `column`: This is a two way parameter. It can either be a string or a list of strings. If it is a string, it is the name of the column to drop. If it is a list of strings, it is a list of columns to drop.

#### Return Value
None
#### Usage Example
```python

data_cleaner.drop("column") #replace column with the column name.

```

```	
##### OR 
```python

data_cleaner.drop(["column_1","column_2"]) #replace column_1 and column_2 with the column names.

```	
<a name="#outliers"></a>

## outliers
### Function Name: outliers
This function is used to plot the outliers in the data. It plots a boxplot for each numeric column in the data.

It is useful to get an idea of the outliers in the data. It can be used to identify outliers in the data.

#### Parameters
None

#### Return Value
None
#### Usage Example
```python

data_cleaner.outliers()

```
<a name="#outliers_single"></a>

## outliers_single
### Function Name: outliers_single
This function is used to plot the outliers in a specific numeric column in the data.

#### Parameters
- `column`: The name of the numeric column to plot the outliers for.

#### Return Value
None
#### Usage Example
```python

data_cleaner.outliers_single("column") #replace column with the column name.

```
<a name="#remove_outliers"></a> 

## remove_outliers
### Function Name: remove_outliers
This function is used to remove outliers from the data. It removes outliers from all the numeric columns in the data.

The concept of outliers is based on the interquartile range (IQR). The IQR is the difference between the 75th percentile (Q3) and the 25th percentile (Q1). The IQR is used to identify outliers by defining limits on the sample values that are a factor k of the IQR below the 25th percentile or above the 75th percentile. The common value for the factor k is the value 1.5. This is the default value used by the function.

#### Parameters
None

#### Return Value
None

#### Usage Example
```python

data_cleaner.remove_outliers()

```
`Note :` Depending on the data one is dealing with, the outliers may not be removed completely. Hence one can use alternative methods to remove outliers for example using the `imputation with nearest logical values`, `Transformation`, `Segmentation` and others.

<a name="#remove_outliers_single"></a> remove_outliers_single_single

## remove_outliers_single
### Function Name: remove_outliers_single
This function is used to remove outliers from the data. It removes outliers from a specific numeric column in the data.

#### Parameters
None

#### Return Value
None

#### Usage Example
```python

data_cleaner.remove_outliers_single("column") #replace column with the column name.

```
OR 
```python

data_cleaner.remove_outliers_single(["column_1","column_2"]) #replace column_1 and column_2 with the column names.	
```

<a name="#corr_matrix"></a>

## corr_matrix
### Function Name: corr_matrix
This function is used to plot the correlation matrix of the data. It plots a heatmap of the correlation matrix of the data.

It is useful to get an idea of the correlation between the numeric columns in the data. It can be used to identify highly correlated columns in the data.

#### Parameters
None

#### Return Value
None

#### Usage Example
```python

data_clener.corr_matrix() 

```

<a name="#cont_corr"></a>


## cont_corr
### Function Name: cont_corr
This function is used to plot a pairplot of the numeric columns in the data.

#### Parameters
None

#### Return Value
None

#### Usage Example
```python

data_clener.cont_corr()

```
<a name="#cont_to_cont"></a>

## cont_to_cont
### Function Name: cont_to_cont
The function is used to show significant relationship or difference between two numeric columns in the data.
This is achieved through plotting a scatter plot of two numeric columns in the data.
The function also goes on to indicate the correlation value between the two columns.

#### Parameters
- `col1`: This is a two way parameter. It can either be a string or a list of strings. If it is a string, it is the name of the first column to plot. If it is a list of strings, it is a list of columns to plot.

- `col2`: This is a two way parameter. It can either be a string or a list of strings. If it is a string, it is the name of the second column to plot. If it is a list of strings, it is a list of columns to plot.

#### Return Value
None

#### Usage Example
```python

data_cleaner.cont_to_cont("col1","col2") #replace col1 and col2 with the column names.

```
##### OR
```python

data_cleaner.cont_to_cont("col1",["col2","col3"]) #replace col1, col2 and col3 with the column names.

```
##### OR
```python

data_cleaner.cont_to_cont(["col1","col2"],"col3") #replace col1, col2 and col3 with the column names.

```
##### OR
```python

data_cleaner.cont_to_cont(["col1","col2"],["col3","col4"]) #replace col1, col2, col3 and col4 with the column names.

```

## cat_to_cat
### Function Name: cat_to_cat
The function is used to show significant relationship or difference between two categorical columns in the data.
The function hence displays a contingency table of the two categorical columns in the data. and also plots a comparative bar graph of the two columns.

#### Parameters
- `col1`: This is a two way parameter. It can either be a string or a list of strings. If it is a string, it is the name of the first column to plot. If it is a list of strings, it is a list of columns to plot.

- `col2`: This is a two way parameter. It can either be a string or a list of strings. If it is a string, it is the name of the second column to plot. If it is a list of strings, it is a list of columns to plot.

#### Return Value
None

#### Usage Example
```python

data_cleaner.cat_to_cat("col1","col2") #replace col1 and col2 with the column names.

```

```
##### OR
```python

data_cleaner.cat_to_cat("col1",["col2","col3"]) #replace col1, col2 and col3 with the column names.

```

```
##### OR
```python

data_cleaner.cat_to_cat(["col1","col2"],"col3") #replace col1, col2 and col3 with the column names.

```

```
##### OR
```python

data_cleaner.cat_to_cat(["col1","col2"],["col3","col4"]) #replace col1, col2, col3 and col4 with the column names.

```
## countplot
### Function Name: countplot
The function is used to plot a countplot of a two categorical columns in the data.
This is a way of showing the distribution of the two categorical columns in the data.

#### Parameters
- `col1`: This is a string. It is the name of the first column to plot.
- `col2`: This is a string. It is the name of the second column to plot.

#### Return Value
None

#### Usage Example
```python

data_cleaner.countplot("col1","col2") #replace col1 and col2 with the column names.

```

## contingency_table
### Function Name: contingency_table
The function is used to show significant relationship or difference between two categorical columns in the data.
The function hence displays a contingency table of the two categorical columns in the data.

#### Parameters
- `col1`: This is a string. It is the name of the first column to plot.
- `col2`: This is a string. It is the name of the second column to plot.

#### Return Value
None

#### Usage Example
```python

data_cleaner.contingency_table("col1","col2") #replace col1 and col2 with the column names.

```

## Chi_square
### Function Name: Chi_square
The function tests for a statistically significant relationship between nominal and ordinal variables. In other words, it tells us whether two variables are independent of one another.

#### Parameters
- `col1`: This is a string. It is the name of the first column categorical column.
- `col2`: This is a string. It is the name of the second column categorical column.

#### Return Value
- Chi_square value
- The p-value
- The degrees of freedom
- A string indicating whether the two columns are independent or not.

#### Usage Example
```python

data_cleaner.Chi_square("col1","col2") #replace col1 and col2 with the column names.

```
## combined_boplot
### Function Name: combined_boplot
The function is used to plot a set of side by side box plots, one for each of the categories. 

#### Parameters
- `col1`: This is a string. It is the name of the first column, categorical column.
- `col2`: This is a string. It is the name of the second column, continuous column.

#### Return Value
None

#### Usage Example
```python

data_cleaner.combined_boxplot("col1", "col2") #replace col1 and col2 with the column names.

```
## singleAnova
### Function Name: singleAnova
The function is used to test for a statistically significant difference between the means of two or more groups.

#### Parameters
- `col1`: This is a string. It is the name of the first column continuous column.
- `col2`: This is a string. It is the name of the second column categorical column.

#### Return Value
- A string indicating whether the two columns are independent or not.

#### Usage Example
```python

data_cleaner.singleAnova("col1", "col2") #replace col1 and col2 with the column names.

```
## cont_to_cat
### Function Name: cont_to_cat
The function is used to show significant relationship or difference between a continuous and a categorical column in the data.  
The function hence displays a side by side boxplot of the continuous column and a categorical column in the data.

#### Parameters
- `col1`: This is two way parameter. It can either be a string or a list of strings. If it is a string, it is the name of the first column continuous column. If it is a list of strings, it is a list of columns to plot.On the other hand, it can be a a string or a list of strings of categorical columns. 

- `col2`: This is two way parameter. It can either be a string or a list of strings. If it is a string, it is the name of the second column categorical column. If it is a list of strings, it is a list of columns to plot.On the other hand, it can be a a string or a list of strings of continuous columns. 

#### Return Value
- A string indicating whether the two columns are independent or not.

#### Usage Example
```python

data_cleaner.cont_to_cat("col1","col2") #replace col1 and col2 with the column names.

```
##### OR
```python

data_cleaner.cont_to_cat("col1",["col2","col3"]) #replace col1, col2 and col3 with the column names.

```
##### OR
```python

data_cleaner.cont_to_cat(["col1","col2"],"col3") #replace col1, col2 and col3 with the column names.

```
##### OR
```python

data_cleaner.cont_to_cat(["col1","col2"],["col3","col4"]) #replace col1, col2, col3 and col4 with the column names.

```

## lineplot
### Function Name: lineplot
The function is used to plot a lineplot of a continous column against a categorical column in the data.
This is a way of showing the distribution of the two continuous columns in the data.

#### Parameters
- `col1`: This is a string. It is the name of the first column to plot.
- `col2`: This is a string. It is the name of the second column to plot.

#### Return Value
None

#### Usage Example
```python

data_cleaner.lineplot("col1","col2") #replace col1 and col2 with the column names.

```
OR 
```python

data_cleaner.lineplot("col1",["col2","col3"]) #replace col1, col2 and col3 with the column names.

```
OR 
```python

data_cleaner.lineplot(["col1","col2"],"col3") #replace col1, col2 and col3 with the column names.

```

OR 
```python

data_cleaner.lineplot(["col1","col2"],["col3","col4"]) #replace col1, col2, col3 and col4 with the column names.

```

## getdata
### Function Name: getdata
The function returns the data that has been cleaned and preprocessed.

#### Parameters
None

#### Return Value
- Returns a dataframe containing the cleaned data.
#### Usage Example

```python

data = data_cleaner.getdata()
data.head()

```
`Note :` This method can be used to access the data at any step after achieving any required process. 

## savedata
### Function Name: data_cleaning
The function is used to download the preprocessed file with the same extension as the entered file. 

#### Parameters
None

#### Return Value   
- None

#### Usage Example

```python

data = data_cleaner.savedata()
data.head()

```

## data_cleaning
### Function Name: data_cleaning
The function is used to clean the data. It performs the following operations:
- Removes empty columns.
- Removes duplicate rows.
- Deals with missing values appropriately.
- Removes outliers.

#### Parameters
None

#### Return Value   
- A dataframe containing the cleaned data.

#### Usage Example

```python

data = data_cleaner.data_cleaning()
data.head()

```
