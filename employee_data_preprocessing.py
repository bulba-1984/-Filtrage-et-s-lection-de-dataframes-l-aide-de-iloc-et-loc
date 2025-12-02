#!/usr/bin/env python3
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import sys
import os

print("=== PREPROCESSING EMPLOYEE DATA ===")

# Vérifie si un argument CSV a été passé
if len(sys.argv) < 2:
    print("Aucun fichier CSV fourni. Usage: python3 employee_data_preprocessing.py <nom_du_fichier.csv>")
    sys.exit(1)

csv_file = sys.argv[1]

# Vérifie si le fichier existe
if not os.path.exists(csv_file):
    print(f"Fichier introuvable : {csv_file}")
    sys.exit(1)

# Charge le CSV
df = pd.read_csv(csv_file)

# Affiche les 10 premières lignes
print("10 premières lignes :")
print(df.head(10))

# Type et info
print("\nType :", type(df))
df.info()

# Dimensions
print("\nDimensions :", df.shape)

# Colonnes catégorielles
cat_cols = df.select_dtypes(include=['object']).columns.tolist()
print("Colonnes catégorielles :", cat_cols)
print("Nombre :", len(cat_cols))

# Mémoire utilisée
print("Mémoire utilisée :", df.memory_usage(deep=True).sum(), "octets")

# Valeurs manquantes
print("\nValeurs manquantes :")
print(df.isnull().sum())

# Analyse descriptive
print("\nAnalyse descriptive :")
print(df.describe())

# Sélection client 0
if 'id' in df.columns:
    client_0_df1 = df.loc[df['id'] == 'train_Client_0']
    client_0_df2 = df.query("id == 'train_Client_0'")
    print("\nClient 0 (loc) :")
    print(client_0_df1)
    print("\nClient 0 (query) :")
    print(client_0_df2)
else:
    print("\nAucune colonne 'id' détectée -> sélection client ignorée.")

# Encodage 'counter_type' si présent
if 'counter_type' in df.columns:
    le = LabelEncoder()
    df['counter_type_encoded'] = le.fit_transform(df['counter_type'])
    print("\nEncodage 'counter_type' effectué.")
else:
    print("\nAucune colonne 'counter_type' détectée -> encodage ignoré.")

# Suppression 'counter_statue' si présent
if 'counter_statue' in df.columns:
    df.drop(columns=['counter_statue'], inplace=True)
    print("\nColonne 'counter_statue' supprimée.")
else:
    print("\nAucune colonne 'counter_statue' détectée -> suppression ignorée.")
