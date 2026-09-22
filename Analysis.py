import pandas as pd
import matplotlib.pyplot as plt

excel_file=pd.read_excel("Final thesis results (version 2).xlsb (1).xlsx", sheet_name="Proline 50%")
print(excel_file.head(37))
print(excel_file.info())
print(excel_file.isnull())
print(excel_file.fillna(0))
print(excel_file.columns)
Graph_analysis=excel_file.groupby("TREATMENTS")['Proline '].agg(["mean","std"])
print(Graph_analysis)
print(Graph_analysis.fillna(0.01))
#For graph plotting 
fig, ax = plt.subplots(figsize=(10, 6))
Graph_analysis['mean'].plot(
    kind='bar',
    yerr=Graph_analysis['std'],
    capsize=5,
    ax=ax,
    color='skyblue',
    edgecolor='black',
)
plt.title('Plant Treatments Analysis', fontsize=14, fontweight='bold')
plt.xlabel('Treatments', fontsize=12)
plt.ylabel('Proline Concentration / Value', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('Proline_Analysis_Plot.png', dpi=300)
plt.show()