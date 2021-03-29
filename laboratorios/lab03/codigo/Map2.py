import pandas as pd

vertices = pd.read_csv('Vertices.csv')
print(vertices)

arcos = pd.read_csv('Arcos.csv')
print(arcos)

dicArcos = {}
for i in range(len(arcos['ID'])):
    dicArcos[(arcos.iloc[i]['ID'],arcos.iloc[i]['ID1'])] = arcos.iloc[i]['Distancia']

print("El diccionario de los arcos es:")
print(dicArcos)

dicVert = {}
for i in range(len(vertices['ID'])):
    dicVert[(vertices.iloc[i]['ID'])] = (vertices.iloc[i]['Coordenada X'], vertices.iloc[i]['Coordenada Y'])

print("El diccionario de los vertices es:")
print(dicVert)