import pandas as pd
from subprocess import run

data = pd.read_csv('wc.csv')

# Insight 1: 
average_age = data['Age'].mean()
with open('eda-in-1.txt', 'w') as file:
    file.write(f"The average age of customers is: {average_age:.2f}\n")

# Insight 2: 
most_reviewed_department = data['Department Name'].value_counts().idxmax()
with open('eda-in-2.txt', 'w') as file:
    file.write(f"The most reviewed department is: {most_reviewed_department}\n")

# Insight 3:
recommended_percentage = data['Recommended IND'].mean() * 100
with open('eda-in-3.txt', 'w') as file:
    file.write(f"The percentage of recommended products is: {recommended_percentage:.2f}%\n")


run(["python", "vis.py", 'wc.csv'])