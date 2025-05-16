import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

resultados_parametros= pd.read_excel('resultados_parametros.xlsx')
print(resultados_parametros)

sns.scatterplot(data=resultados_parametros, x='dAttr', y='Resultado')
plt.title('Relación entre dAttr y Fitness')
plt.show()

sns.scatterplot(data=resultados_parametros, x='wAttr', y='Resultado')
plt.title('Relación entre wAttr y Fitness')
plt.show()

sns.scatterplot(data=resultados_parametros, x='wRep', y='Resultado')
plt.title('Relación entre wRep y Fitness')
plt.show()

resultados_parametros['config'] = resultados_parametros.apply(lambda row: f"d={row['dAttr']}, w={row['wAttr']}", axis=1)

plt.figure(figsize=(10, 5))
sns.barplot(data=resultados_parametros, x='config', y='Resultado')
plt.xticks(rotation=45)
plt.title('Fitness según combinación de parámetros')
plt.ylabel('Resultado (Fitness)')
plt.xlabel('Configuración (dAttr, wAttr)')
plt.tight_layout()
plt.show()


pivot = resultados_parametros.pivot_table(values='Resultado', index='dAttr', columns='wAttr')
sns.heatmap(pivot, annot=True, cmap='viridis')
plt.title('Mapa de calor de Fitness según dAttr y wAttr')
plt.show()


resultados_comparacion= pd.read_excel('resultados_comparacion.xlsx')
print(resultados_comparacion)

metricas = ['Fitness', 'BlosumScore', 'Interaction', 'NFE', 'Time']
df_plot = resultados_comparacion.set_index('Algoritmo')[metricas]

df_plot.T.plot(kind='bar', figsize=(10, 6))
plt.title('Comparación de desempeño entre algoritmos')
plt.ylabel('Valor')
plt.xlabel('Métrica')
plt.xticks(rotation=45)
plt.legend(title='Algoritmo')
plt.grid(axis='y')
plt.tight_layout()
plt.show()

plt.figure()
plt.bar(resultados_comparacion['Algoritmo'], resultados_comparacion['Fitness'], color=['gray', 'green'])
plt.title('Comparación de Fitness')
plt.ylabel('Fitness')
plt.ylim(15.95, 16.05) 
plt.show()
