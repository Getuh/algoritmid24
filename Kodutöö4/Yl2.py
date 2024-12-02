class IndexMapping:
    def __init__(self, max_value):
        self.mapping = [False] * (max_value + 1)

    def insert(self, value):
        self.mapping[value] = True

    def exists(self, value):
        return self.mapping[value]

max_value = 100
mapper = IndexMapping(max_value)

mapper.insert(10)
mapper.insert(25)
mapper.insert(54)
mapper.insert(23)
mapper.insert(33)
mapper.insert(47)

print(mapper.exists(25)) 
print(mapper.exists(15))
print(mapper.exists(47))

#Ajakompleksus on O(1) ja ruumikompleksus O(n)