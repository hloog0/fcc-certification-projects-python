class HashTable:
    def __init__(self):
        self.collection = {}
    
    def hash(self, string: str) -> int:
        hash_value = 0
        for word in string:
            hash_value += ord(word)
        return hash_value

    def add(self, key, value):
        key_hash = self.hash(key)
        if key_hash in self.collection:
            self.collection[key_hash][key] = value
            return "Pair added to existing hash value"
        else:
            self.collection[key_hash] = {key: value}
            return "Pair added with new hash value"

    def remove(self, key):
        key_hash = self.hash(key)
        if key_hash in self.collection and key in self.collection[key_hash]: #does the hash exist and does the hash have the key
            if len(self.collection[key_hash]) > 1: #does hash have more than one
                self.collection[key_hash].pop(key, None)
                return "Pair removed from hash with duplicates"
            else: #hash only has 1 nested
                self.collection.pop(key_hash, None)
                return "Pair removed"
        else: #hash doesn't exist
            return "Key does not exist"

    def lookup(self, key):
        key_hash = self.hash(key)
        if key_hash in self.collection and key in self.collection[key_hash]:
                return self.collection[key_hash][key]
            else:
                return None
        else:
            return None
if __name__ = '__main__'
print(HashTable().hash('golf'))
newhash = HashTable()
newhash.add('dear', 'friend')
newhash.add('read', 'book')
print(newhash.collection)
print(newhash.lookup('read'))
print(newhash.remove('read'))
print(newhash.lookup('dear'))
print(newhash.lookup('read'))
