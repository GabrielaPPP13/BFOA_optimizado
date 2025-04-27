import pandas as pd


df = pd.read_excel('resultados.xlsx')

print(df)


import matplotlib.pyplot as plt
import seaborn as sns

# Supongamos que df es tu DataFrame
plt.figure(figsize=(10,6))
sns.scatterplot(x='Fitness', y='Tiempo de Ejecución (segundos)', data=df)
plt.title('Fitness vs Tiempo de Ejecución')
plt.xlabel('Fitness')
plt.ylabel('Tiempo de Ejecución (segundos)')
plt.grid(True)
plt.show()


plt.figure(figsize=(10,6))
sns.lineplot(x='Corrida', y='Fitness', data=df, marker='o')
plt.title('Fitness a lo largo de las Corridas')
plt.xlabel('Corrida')
plt.ylabel('Fitness')
plt.grid(True)
plt.show()


plt.figure(figsize=(10,6))
sns.barplot(x='Corrida', y='numeroDeBacterias', data=df)
plt.title('Número de Bacterias por Corrida')
plt.xlabel('Corrida')
plt.ylabel('Número de Bacterias')
plt.grid(True)
plt.show()


plt.figure(figsize=(10,6))
sns.scatterplot(x='Calificación Blosum', y='Interacción', data=df)
plt.title('Calificación Blosum vs Interacción')
plt.xlabel('Calificación Blosum')
plt.ylabel('Interacción')
plt.grid(True)
plt.show()


plt.figure(figsize=(10,6))
sns.barplot(x='numeroDeBacterias', y='numRandomBacteria', data=df)
plt.title('Número de Bacterias vs Número Aleatorio de Bacterias')
plt.xlabel('Número de Bacterias')
plt.ylabel('Número Aleatorio de Bacterias')
plt.grid(True)
plt.show()


plt.figure(figsize=(10,6))
sns.histplot(df['Tiempo de Ejecución (segundos)'], kde=True, color='blue')
plt.title('Distribución del Tiempo de Ejecución')
plt.xlabel('Tiempo de Ejecución (segundos)')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()


plt.figure(figsize=(12,8))
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Mapa de Calor de Correlaciones')
plt.show()


plt.figure(figsize=(10,6))
sns.boxplot(x='Corrida', y='Fitness', data=df)
plt.title('Distribución del Fitness por Corrida')
plt.xlabel('Corrida')
plt.ylabel('Fitness')
plt.grid(True)
plt.show()
