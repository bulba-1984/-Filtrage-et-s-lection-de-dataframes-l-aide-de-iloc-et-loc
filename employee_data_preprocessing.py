import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Charger le fichier CSV (remplace par ton chemin réel si nécessaire)
df = pd.read_csv("client_bills.csv")

# 10 premières lignes
client_0_bills = df.head(10)
print("10 premières lignes :\n", client_0_bills)

# Type de client_0_bills
print("\nType :", type(client_0_bills))

# Infos générales
df.info()

# Dimensions
print("\nDimensions :", df.shape)

# Colonnes catégorielles
categorical_cols = df.select_dtypes(include='object').columns
print("Colonnes catégorielles :", list(categorical_cols))
print("Nombre :", len(categorical_cols))

# Mémoire utilisée
print("Mémoire utilisée :", df.memory_usage(deep=True).sum(), "octets")

# Valeurs manquantes
print("\nValeurs manquantes :\n", df.isnull().sum())

# Analyse descriptive
print("\nAnalyse descriptive :\n", df.describe())

# Sélection du client 'train_Client_0'
client_0_df1 = df.loc[df['id'] == 'train_Client_0']
client_0_df2 = df.query("id == 'train_Client_0'")

print("\nClient 0 (loc) :\n", client_0_df1)
print("\nClient 0 (query) :\n", client_0_df2)

# Encodage de 'counter_type'
le = LabelEncoder()
df['counter_type_encoded'] = le.fit_transform(df['counter_type'])

# Supprimer 'counter_statue'
df.drop(columns=['counter_statue'], inplace=True)

print("\nDataFrame final :\n", df)

