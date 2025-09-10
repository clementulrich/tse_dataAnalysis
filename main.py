import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Charger le dataset
data = pd.read_csv("vgsales.csv")


## Exercice 2
print(" ")
print("-------------- Exercice 2 --------------")

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
print(" ")
print("-------------- Exercice 3.1 --------------")
print("\nStatistiques descriptives du jeu de données :")
print(data_clean.describe())

sales_data = data_clean[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']]
corr_matrix = sales_data.corr()
print("\nMatrice de corrélation entre les ventes régionales et globales :")
print(corr_matrix)


## Exercice 3.2
# Afficher les colonnes existantes
global_sales_by_year = data_clean.groupby('Year')['Global_Sales'].sum()
print(" ")
print("-------------- Exercice 3.2 --------------")
print(global_sales_by_year)

# Tracer l'évolution des ventes globales par année
global_sales_by_year.plot(kind='line', marker='x', figsize=(10,6))
plt.title('Évolution des ventes  par année')
plt.xlabel('Année'), plt.ylabel('Ventes mondiales (millions)')
plt.grid(True)
plt.show()

# Année avec le plus de ventes au total
most_selling_year = global_sales_by_year.idxmax()
most_selling_value = global_sales_by_year.max()
print(" ")
print(f"L'année avec le plus de ventes mondiales est : {most_selling_year} ({most_selling_value} millions)")


## Exercice 3.3
print(" ")
print("-------------- Exercice 3.3 --------------")

publisher_sales = data_clean.groupby('Publisher')['Global_Sales'].sum()
total_global_sales = data_clean['Global_Sales'].sum()
publisher_sales_percentage = publisher_sales / total_global_sales * 100
publisher_sales_percentage = publisher_sales_percentage.sort_values(ascending=False)
print(publisher_sales_percentage)

# Tracer le graphique en barres
plt.figure(figsize=(12, 8))
publisher_sales_percentage.plot(kind='bar', color='skyblue')
plt.title('Pourcentage des ventes mondiales par éditeur')
plt.xlabel('Éditeur')
plt.ylabel('Pourcentage (%)')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


# Sélectionner les 10 éditeurs avec les ventes les plus élevées
top_publishers = publisher_sales.sort_values(ascending=False).head(10)
print(" ")
print(top_publishers)

print(" ")
sales_values = top_publishers.values
indicator_matrix = (sales_values[:, None] > sales_values[None, :]).astype(int)
print(indicator_matrix)