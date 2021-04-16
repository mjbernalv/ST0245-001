import os, sys
import pandas as pd
import numpy as np
import math

pathGanadoEnfermoCSV = "./ArchivosCSV/Ganado Enfermo CSVs"
pathGanadoSanoCSV = "./ArchivosCSV/Ganado Sano CSVs"
dirGanadoEnfermo = os.listdir(pathGanadoEnfermoCSV)
dirGanadoSano = os.listdir(pathGanadoSanoCSV)
pathEnfermoComprido = "./ArchivosCSV/Ganado Enfermo Comprimido"
pathSanoComprimido = "./ArchivosCSV/Ganado Sano Comprimido"
pathEnfermoDescomprimido = "./ArchivosCSV/Ganado Enfermo Descomprimido"
pathSanoDescomprimido = "./ArchivosCSV/Ganado Sano Descomprimido"

def loadCSV(path, pictures):
    array = []
    for i in range(len(pictures)):
        newPath = path + "/" + pictures[i]
        data = pd.read_csv(newPath, header=None)
        x = np.array(data).astype("int")
        array.append(x)
    return array    

def compress(image, ratio):
    try:
        rows, columns = image.shape
        newRows = int(math.ceil(rows/ratio))
        newColumns = int(math.ceil(columns/ratio))
        newImage = np.arange(newRows*newColumns).reshape(newRows,newColumns)
        if ratio==1:
            newImage = image
        else:
            countRows = 0
            for i in range(0, rows, ratio):
                countColumns = 0
                for j in range (0, columns, ratio):
                    newImage[countRows, countColumns]=image[i,j]
                    countColumns+=1
                countRows+=1
        return newImage  
    except:
        print("Error")

def decompress(image, ratio):
    try:
        rows, columns = image.shape
        newRows = int(math.ceil(rows*ratio))
        newColumns = int(math.ceil(columns*ratio))
        newImage = np.arange(newRows*newColumns).reshape(newRows,newColumns)
        if ratio==1:
            newImage = image
        else:
            countRows = 0
            for i in range (newRows):
                countColumns = 0
                for j in range(newColumns):
                    newImage[i,j]=image[int(math.floor(countRows/ratio)), int(math.floor(countColumns/ratio))]
                    countColumns+=1
                countRows+=1 
        return newImage
    except:
        print("Error")

def saveCSV(path, image, name):
    np.savetxt(path + "/" + name, image, delimiter=",")    
    return

dataGanadoEnfermo = loadCSV(pathGanadoEnfermoCSV, dirGanadoEnfermo)
dataGanadoSano = loadCSV(pathGanadoSanoCSV, dirGanadoSano)

print("Files are being compressed and decompressed")
for i in range (len(dataGanadoEnfermo)):
    compressed = compress(dataGanadoEnfermo[i], 2)
    saveCSV(pathEnfermoComprido, compressed, dirGanadoEnfermo[i])
    decompressed = decompress(compressed, 2)
    saveCSV(pathEnfermoDescomprimido, decompressed, dirGanadoEnfermo[i])

for j in range (len(dataGanadoSano)):
    compressed = compress(dataGanadoSano[j], 2)
    saveCSV(pathSanoComprimido, compressed, dirGanadoSano[j])
    decompressed = decompress(compressed, 2)
    saveCSV(pathSanoDescomprimido, decompressed, dirGanadoSano[j])

print("Your files are ready")
