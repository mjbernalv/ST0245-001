import os
import pandas as pd
import numpy as np
import math
from PIL import Image

pathGanadoEnfermoCSV = "Proyecto/Código/ArchivosCSV/Ganado Enfermo CSVs"
pathGanadoSanoCSV = "Proyecto/Código/ArchivosCSV/Ganado Sano CSVs"
dirGanadoEnfermo = os.listdir(pathGanadoEnfermoCSV)
dirGanadoSano = os.listdir(pathGanadoSanoCSV)
pathEnfermoComprido = "Proyecto/Código/ArchivosCSV/Ganado Enfermo Comprimido"
pathSanoComprimido = "Proyecto/Código/ArchivosCSV/Ganado Sano Comprimido"
pathEnfermoDescomprimido = "Proyecto/Código/ArchivosCSV/Ganado Sano Descomprimido"
pathSanoDescomprimido = "Proyecto/Código/ArchivosCSV/Ganado Enfermo Descomprimido"

print(type(dirGanadoEnfermo))

def loadCSV(path, pictures):
    """ Read images as a CSV file and returns an array containing all the images in arrays.
    :type path: string
    :param path: contains the path of the location of the images
    
    :type pictures: list
    :param pictures: contains the names of the pictures
    
    :raises: path not found exception
    
    :rtype: numpy array
    """
    array = []
    for i in range(len(pictures)):
        newPath = path + "/" + pictures[i]
        data = pd.read_csv(newPath, header=None)
        x = np.array(data).astype("int")
        array.append(x)
    return array    

def compress(image, ratio):
    """ Compresses image using Nearest neighbor algorithm and returns the compressed image as a matrix.
    :type image: numpy array (matrix)
    :param image: matrix containing the original image
    
    :type ratio: integer
    :param ratio: describes how much the image wants to be compressed
        
    :rtype: numpy array (matrix)
    """
    rows, columns = image.shape
    newRows = int(math.ceil(rows/ratio))
    newColumns = int(math.ceil(columns/ratio))
    newImage = np.zeros((newRows,newColumns),dtype=np.uint8)
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
        
def decompress(image, ratio):
    """ Decompresses image using Nearest Neighbor algorithm and returns the decompressed image as a matrix.
    :type image: numpy array (matrix)
    :param image: matrix containing the compressed image
    
    :type ratio: integer
    :param ratio: describes how much the image wants to be decompressed
        
    :rtype: numpy array (matrix)
    """
    rows, columns = image.shape
    newRows = int(math.ceil(rows*ratio))
    newColumns = int(math.ceil(columns*ratio))
    newImage = np.zeros((newRows,newColumns),dtype=np.uint8)
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
        
def saveCSV(path, image, name):
    """ Saves an image from a numpy array (matrix) to a csv file.
    :type path: string
    :param path: contains the path where the image is going to be saved
    
    :type image: numpy array (matrix)
    :param image: contains the image represented in a numpy array
    
    :type name: string
    :param name: contains the new file name of the image
        
    :rtype: None
    """
    np.savetxt(path + "/" + name, image, delimiter=",")    
    return

def showImage(image):
    """ Shows a plot of the image from a numpy array (matrix)
    :type image: numpy array
    :param image: represents the image as an array (matrix)
        
    :rtype: None
    """
    plot =  Image.fromarray(image)
    plot.show()

dataEnfermo = loadCSV(pathGanadoEnfermoCSV, dirGanadoEnfermo)
dataSano = loadCSV(pathGanadoSanoCSV, dirGanadoSano)

print("Files are being compressed and decompressed")

compressed = compress(dataEnfermo[0], 2)
decompressed = decompress(compressed, 2)

showImage(compressed)
showImage(decompressed)

print("Your files are ready")
