file = open('usda-dc-directory.csv','r')
text = file.read()
file.close()

rows = text.split("\n")
hashTable = dict()

for line in rows:
    columns = line.split(",")
    lastName = columns[0]
    name = columns[1]
    phone = columns[3]
    hashTable[name+" "+lastName] = phone

for nameAndLastName in hashTable:
    print(nameAndLastName + ": " + hashTable[nameAndLastName])