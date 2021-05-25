from Huffman import HuffmanCoding
from time import time
from memory_profiler import profile

path = "Proyecto/Código/Sin pérdida/Ensayo/00000004_66324407_ver1.csv"

image = HuffmanCoding(path)

inicio1 = time()
compressed = image.compress(path)
fin1 = time()
total1 = fin1-inicio1
print("Compressed:", total1)

'''inicio2 = time()
decompressed = image.decompress(compressed)
fin2 = time()
total2 = fin2-inicio2
print("Decompressed:", total2) '''

#image.showImage(decompressed)