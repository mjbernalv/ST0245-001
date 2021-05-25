from bitarray import bitarray
from PIL import Image
from numpy import genfromtxt

class LZ77Compressor:
	maxWindow = 500

	def __init__(self, windowSize=20):
		self.windowSize = min(windowSize, self.maxWindow) 
		self.lookaheadBufferSize = 15

	def compress(self, inputFile, outputFile):
		image = None
		counter = 0
		outputBuffer = bitarray(endian='big')

		image = self.openFile(inputFile, True)

		while counter < len(image):
			match = self.findLongestMatch(image, counter)

			if match: 
				(bestDistance, bestLength) = match
				outputBuffer.append(True)
				outputBuffer.frombytes(bytes([bestDistance >> 4]))
				outputBuffer.frombytes(bytes([((bestDistance & 0xf) << 4) | bestLength]))
				counter += bestLength
			else:
				outputBuffer.append(False)
				outputBuffer.frombytes(bytes([image[counter]]))
				counter += 1

		outputBuffer.fill()
		self.saveFile(outputFile, outputBuffer, True)
		return outputBuffer

	def decompress(self, inputFile, outputFile):
		outputBuffer = []

		image = self.openFile(inputFile, False)

		while len(image) >= 9:
			current = image.pop(0)

			if not current:
				byte = image[0:8].tobytes()
				outputBuffer.append(byte)
				del image[0:8]
			else:
				byte1 = ord(image[0:8].tobytes())
				byte2 = ord(image[8:16].tobytes())
				del image[0:16]
				distance = (byte1 << 4) | (byte2 >> 4)
				length = (byte2 & 0xf)

				for i in range(length):
					outputBuffer.append(outputBuffer[-distance])
		
		outputImage =  b''.join(outputBuffer)
		self.saveFile(outputFile, outputImage, False)		
		return outputImage

	def findLongestMatch(self, data, current):
		end = min(current + self.lookaheadBufferSize, len(data) + 1)
		bestDistance = -1
		bestLength = -1

		for m in range(current + 2, end):
			start = max(0, current - self.windowSize)
			substring = data[current:m]

			for n in range(start, current):
				repeat = len(substring) // (current - n)
				last = len(substring) % (current - n)
				matched = data[n:current] * repeat + data[n:n+last]

				if matched == substring and len(substring) > bestLength:
					bestDistance = current - n
					bestLength = len(substring)

		if bestDistance > 0 and bestLength > 0:
			return (bestDistance, bestLength)
		return None

	def openFile(self, inputFile, x):
		try:
			if x:
				with open(inputFile, 'rb') as file:
					image = file.read()
				return image
			else:
				image = bitarray(endian='big')
				with open(inputFile, 'rb') as file:
					image.fromfile(file)
				return image
		except IOError:
				print('File could not be opened')
				raise

	def saveFile(self, outputFile, output, x):
		try:
			if x:
				with open(outputFile, 'wb') as file:
					file.write(output.tobytes())
					print("Your file was compressed")
					return
			else:
				with open(outputFile, 'wb') as file:
					file.write(output)
					print('Your file was decompressed')
					return 
		except IOError:
				print('File could not be saved')
				raise 

	def showImage(self, path):
		data = genfromtxt(path, delimiter=',')
		plot = Image.fromarray(data)
		plot.show()


#This code was contributed by: https://github.com/manassra/LZ77-Compressor/blob/master/src/LZ77.py