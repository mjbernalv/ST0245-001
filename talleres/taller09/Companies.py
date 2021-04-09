#Puntos 2, 3 y 4

companies = {"Google": "United States",
            "La Locura": "Colombia",
            "Nokia": "Finland",
            "Sony": "Japan",
            }

#Punto 2
def printHash(hash):
    for key, value in hash.items():
        print(key + ": " + hash[key])

#Punto 3
def searchValue(key, hash = companies):
    if key in hash:
        print(key + " is located in " + hash[key])
    else:
        print(key + " does not exist in the hash table")

#Punto 4
def searchKeys(values, hash = companies):
    countries = hash.values()
    actkey = ""
    if values in countries:
        for key, value in hash.items():
            if values == value:
                actkey = key
                print("In " + values + " we can find " + actkey)
    else:
        print("There are no companies in " + values)

print("Punto 2:")
printHash(companies)
print("")
print("Punto 3:")
searchValue("Google")
searchValue("Apple")
print("")
print("Punto 4:")
searchKeys("Colombia")
searchKeys("Spain")