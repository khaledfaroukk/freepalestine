
import pandas as pd
from subprocess import run

data = pd.read_csv('wc.csv')

# Data Cleaning
# Task 1: Handling missing values 
data['Age'].fillna(data['Age'].median(), inplace=True)

# Task 2: Removing duplicates
data.drop_duplicates(inplace=True)

# Data Transformation
# Task 1: Creating a new column - 'Review_Length' based on the length of 'Review Text'
data['Review_Length'] = data['Review Text'].apply(lambda x: len(str(x)))

# Task 2: Encoding categorical variables - Convert 'Department Name' using one-hot encoding
department_dummies = pd.get_dummies(data['Department Name'], prefix='Department')
data = pd.concat([data, department_dummies], axis=1)
data.drop('Department Name', axis=1, inplace=True)

# Data Reduction
# Task 1: Aggregating data - Calculate mean ratings per 'Age' group
age_group_ratings = data.groupby('Age')['Rating'].mean().reset_index()

# Task 2: Dropping unnecessary columns - Drop columns 'Title' and 'Clothing ID'
data.drop(['Title', 'Clothing ID'], axis=1, inplace=True)

# Data Discretization
# Task 1: Binning numerical data - Convert 'Positive Feedback Count' into three bins
data['Feedback_Bins'] = pd.cut(data['Positive Feedback Count'], bins=3, labels=['Low', 'Medium', 'High'])

# Task 2: Converting 'Rating' to categorical based on thresholds
data['Rating_Category'] = pd.cut(data['Rating'], bins=[0, 2, 3, 4, 5], labels=['Low', 'Moderate', 'High', 'Very High'])

# Save the resulting DataFrame as a new CSV file

data.to_csv('res_dpre.csv', index=False)

run(["python", "eda.py", 'wc.csv'])