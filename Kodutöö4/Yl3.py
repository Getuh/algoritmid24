class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):

        return hash(key) % self.size

    def find_node(self, key):

        index = self.hash_function(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current
            current = current.next
        return None

    def insert(self, key, value):

        node = self.find_node(key)
        if node:
            node.value = value
        else:
            index = self.hash_function(key)
            new_node = Node(key, value)
            new_node.next = self.table[index]
            self.table[index] = new_node

    def search(self, key):

        node = self.find_node(key)
        return node.value if node else None

    def delete(self, key):

        index = self.hash_function(key)
        current = self.table[index]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return True
            prev = current
            current = current.next
        return False 

    def resize(self):

        old_table = self.table
        self.size *= 2
        self.table = [None] * self.size
        for head in old_table:
            current = head
            while current:
                self.insert(current.key, current.value)
                current = current.next

    def display(self):

        for i, node in enumerate(self.table):
            chain = []
            current = node
            while current:
                chain.append(f"({current.key}, {current.value})")
                current = current.next
            print(f"Index {i}: {' -> '.join(chain) if chain else 'None'}")


ht = HashTable(5)
ht.insert(1, "One")
ht.insert(11, "Eleven")
ht.insert(21, "Twenty-one")
ht.insert(2, "Two")

print("Tabeli sisu pärast lisamist:")
ht.display()

print("\nOtsimine:")
print(ht.search(11))
print(ht.search(3)) 

print("\nKustutamine:")
ht.delete(11)  
ht.display()

print("\nTabel:")
ht.resize()
ht.display()