class HashTableMM():
    def __init__(self):
        self.table = [None]*100

    def hashFunction(self, key):
        count = 0
        for i in range(len(key)):
            count += ord(key[i])
        return count % 100
    
    def get(self, key):
        position = self.hashFunction(key)
        if self.table[position] is None:
            return None
        return self.table[position]

    def put(self, key, value):
        position = self.hashFunction(key)
        if self.table[position] is None:
            self.table[position] = (key, value)

class main():
    hash = HashTableMM()
    hash.put("Maria", 8349230)
    hash.put("Martin", 201323)
    hash.put("Mauricio", 312942)
    print(hash.get("Maria"))
    print(hash.get("Mauricio"))
    print(hash.get("Camila"))
    print(hash.table)