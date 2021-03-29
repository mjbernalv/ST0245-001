import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

ciudad = nx.Graph()

vertices = pd.read_csv('Vertices.csv')
print(vertices)

arcos = pd.read_csv('Arcos.csv')
print(arcos)

for i in range(len(vertices["ID"])):
    ciudad.add_node(vertices["ID"].values[i])

for j in range(len(arcos)):
    ciudad.add_edge(arcos["ID"].values[j], arcos["ID1"].values[j])
    ciudad[arcos['ID'].values[j]][arcos['ID1'].values[j]]["weight"] = arcos['Distancia'].values[j]
    
nx.draw_shell(ciudad, with_labels=True, font_weight='bold', font_size = 15, node_size = 500, font_color = "white")
plt.show()