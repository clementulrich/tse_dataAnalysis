import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Charger le dataset
data = pd.read_csv("vgsales.csv")


## Exercice 2
print("Shape of dataset:", data.shape)
print("Missing values per column:\n", data.isnull().sum())
print("Number of duplicate rows:", data.duplicated().sum())

data_clean = data.dropna().drop_duplicates()

print("Shape after cleaning:", data_clean.shape)

print("\nRésumé statistique du dataset nettoyé :")
print(data_clean.describe(include='all'))
print("\nInformations sur le dataset nettoyé :")
print(data_clean.info())


## Exercice 3.1
print("\nStatistiques descriptives du jeu de données :")
print(data_clean.describe())

sales_data = data_clean[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']]
corr_matrix = sales_data.corr()
print("\nMatrice de corrélation entre les ventes régionales et globales :")
print(corr_matrix)


## Exercice 3.2
# Afficher les colonnes existantes
print(data_clean.columns)
