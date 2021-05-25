import heapq
from PIL import Image
from numpy import genfromtxt

class HuffmanCoding():
	""" This class is in charge of compression and decompression of images using 
	the Huffman Coding algorithm.	"""
	
	def __init__(self, path):
		""" This constructor initializes the process of compression and decompression of an image.		
		:type path: string
		:param path: contains the path of the image
				
		:rtype: None
		"""
		self.path = path
		self.heap = []
		self.codes = {}
		self.reverseMapping = {}

	class HeapNode():
		""" This class is in charge of creating the nodes to build the Huffman tree by using heap queue.	"""
		
		def __init__(self, pixel, frequency):
			""" This constructure initializes each node of the tree.		
			:type pixel: integer
			:param pixel: is the value of each pixel in the image
			
			:type frequency: integer
			:param frequency: says how much a certain pixel is repeated in the image
						
			:rtype: None
			"""
			self.pixel = pixel
			self.frequency = frequency
			self.left = None
			self.right = None

		def __lt__(self, other):
			""" This method defines the less than function.
			:type other: HeapNode
			:param other: the other node that will be compared with the current one
						
			:rtype: Boolean
			"""
			return self.frequency < other.frequency

		def __eq__(self, other):
			""" This method defines the equal to function.
			:type other: HeapNode
			:param other: the other node that will be compared with the current one
						
			:rtype: Boolean
			"""
			if(other == None):
				return False
			if(not isinstance(other, HeapNode)):
				return False
			return self.frequency == other.frequency

	def compress(self, filename):
		""" This method is in charge of compression using Huffman coding.	
		:type filename: string
		:param filename: contains the path of the file that is going to be compressed
		
		:raises: file not found exception
		
		:rtype: string with the compressed file name
		"""
		outputName = filename + "Compressed.csv"

		with open(self.path, 'r+') as file, open(outputName, 'wb') as output:
			text = file.read()
			frequency = self.__frequencyDict(text)
			self.__makeHeap(frequency)
			self.__makeTree()
			self.__createCodes()
			encoded = self.__getEncodedFile(text)
			paddedEncoded = self.__padEncodedFile(encoded)
			b = self.__byteArray(paddedEncoded)
			output.write(bytes(b))

		print("Compressed")
		return outputName

	def __frequencyDict(self, file):
		""" Creates a hash tables with all the frequencies for each pixel in the image
		:type file: string
		:param file: contains the file that is being read
				
		:rtype: Hash table (dictionary)
		"""
		frequency = {}
		for char in file:
			if not char in frequency:
				frequency[char] = 0
			frequency[char] += 1
		return frequency

	def __makeHeap(self, frequency):
		""" Creates a HeapNode for each pixel in the image with its corresponding frequency.		
		:type frequency: Hash table
		:param frequency: contains the frequencies of each pixel in the image
				
		:rtype: None
		"""
		for key in frequency:
			node = self.HeapNode(key, frequency[key])
			heapq.heappush(self.heap, node)

	def __makeTree(self):
		""" Creates Huffman tree with each of the nodes

		:rtype: None
		"""
		while(len(self.heap)>1):
			node1 = heapq.heappop(self.heap)
			node2 = heapq.heappop(self.heap)
			merged = self.HeapNode(None, node1.frequency + node2.frequency)
			merged.left = node1
			merged.right = node2
			heapq.heappush(self.heap, merged)

	def __createCodes(self):
		""" Codes each leaf of the tree (pixel in the image)
		
		:rtype: None
		"""
		root = heapq.heappop(self.heap)
		current = ""
		self.__createCodesAux(root, current)

	def __createCodesAux(self, root, current):
		""" Helps coding each leaf of the tree (pixel in the image)

		:type root: HeapNode
		:param root: is the root of the Huffman Tree

		:type current: Heapnode
		:param current: is the current node of the tree that is being used

		:rtype: None
		"""
		if(root == None):
			return
		if(root.pixel != None):
			self.codes[root.pixel] = current
			self.reverseMapping[current] = root.pixel
			return
		self.__createCodesAux(root.left, current + "0")
		self.__createCodesAux(root.right, current + "1")

	def __getEncodedFile(self, file):
		""" Encodes the image
		:type file: string
		:param file: contains the file that is going to be enconded
				
		:rtype: string
		"""
		encoded = ""
		for char in file:
			encoded += self.codes[char]
		return encoded

	def __padEncodedFile(self, encoded):
		""" Pads the pixels that have a code that is not a multiple of 8.	
		:type encoded: string
		:param encoded: contains the enconded image
				
		:rtype: string
		"""
		extra = 8 - len(encoded) % 8
		for i in range(extra):
			encoded += "0"
		info = "{0:08b}".format(extra)
		encoded = info + encoded
		return encoded

	def __byteArray(self, paddedFile):
		""" Creates a byte array with the padded file.
		
		:type paddedFile: string
		:param paddedFile: contains the padded file
		
		:raises: file not padded properly exception
		
		:rtype: byte array
		"""
		if(len(paddedFile) % 8 != 0):
			print("Encoded text not padded properly")
			exit(0)
		b = bytearray()
		for i in range(0, len(paddedFile), 8):
			byte = paddedFile[i:i+8]
			b.append(int(byte, 2))
		return b

	def decompress(self, filename):
		""" This method is in charge of decompression using Huffman coding.	
		
		:type filename: string
		:param filename: contains the path of the compressed image that is going to be decompressed.
		
		:raises: file not found exception
		
		:rtype: string with the decompressed file name
		"""
		outputName = filename + "_decompressed" + ".csv"

		with open(filename, 'rb') as file, open(outputName, 'w') as output:
			string = ""
			byte = file.read(1)
			while(len(byte) > 0):
				byte = ord(byte)
				bits = bin(byte)[2:].rjust(8, '0')
				string += bits
				byte = file.read(1)
			encoded = self.__removePadding(string)
			decompressed = self.__decodeFile(encoded)
			output.write(decompressed)

		print("Decompressed")
		return outputName

	def __removePadding(self, encoded):
		""" Removes the padding of the encoded file		
		:type encoded: string
		:param encoded: contains the padded encoded file
				
		:rtype: string
		"""
		padded = encoded[:8]
		extra = int(padded, 2)
		encoded = encoded[8:] 
		encodedFile = encoded[:-1*extra]
		return encodedFile

	def __decodeFile(self, encoded):
		""" Decodes the encoded file	
		:type encoded: string
		:param encoded: contains the encoded file
				
		:rtype: string
		"""
		current = ""
		decoded = ""
		for bit in encoded:
			current += bit
			if(current in self.reverseMapping):
				character = self.reverseMapping[current]
				decoded += character
				current = ""
		return decoded

	def showImage(self, path):
		""" Shows a plot of the image from a csv file
		:type path: string
		:param path: represents the image in a csv file
		
		:raises: file not found exception
		
		:rtype: None
		"""
		data = genfromtxt(path, delimiter=',')
		plot = Image.fromarray(data)
		plot.show()

#This code was contributed by: https://github.com/bhrigu123/huffman-coding/blob/master/huffman.py
