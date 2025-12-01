import pandas as pd

data = {
    'Name': ['John', 'Mary', 'Bob', 'Sarah', 'Tom', 'Lisa'],
    'Department': ['IT', 'Marketing', 'Sales', 'IT', 'Finance', 
'Marketing'],
    'Age': [30, 40, 25, 35, 45, 28],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Salary': [50000, 60000, 45000, 55000, 70000, 55000],
    'Experience': [3, 7, 2, 5, 10, 4]
}

employee_df = pd.DataFrame(data)

# 1. Affichage complet
print("=== DataFrame complet ===")
print(employee_df)

# 2. 3 premières lignes
print("\n=== 3 premières lignes (iloc) ===")
print(employee_df.iloc[:3])

# 3. Lignes où Department = Marketing
print("\n=== Lignes où Department = Marketing (loc) ===")
print(employee_df.loc[employee_df['Department'] == 'Marketing'])

# 4. Age et Gender pour les 4 premières lignes
print("\n=== Age et Gender pour les 4 premières lignes (iloc) ===")
print(employee_df.iloc[:4, [2, 3]])

# 5. Salary et Experience pour Gender = Male
print("\n=== Salary et Experience pour Gender = Male (loc) ===")
print(employee_df.loc[employee_df['Gender'] == 'Male', ['Salary', 
'Experience']])

