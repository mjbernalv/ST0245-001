from LZ77 import LZ77Compressor
import os

original = "Proyecto/Código/Sin pérdida/053111_1344_traceelemen9.csv"
compressed = "Proyecto/Código/Sin pérdida/compressed.csv"
decompressed = "Proyecto/Código/Sin pérdida/decompressed.csv"

compressor = LZ77Compressor(windowSize=40) 
comprimir = compressor.compress(original, compressed)
descomprimir = compressor.decompress(compressed, decompressed)

compressor.showImage(original)
compressor.showImage(decompressed)
