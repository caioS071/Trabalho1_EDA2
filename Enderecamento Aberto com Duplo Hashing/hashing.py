import os


class HashTable:
    def __init__(self, size, file_path):
        self.size = size
        self.hash_table = [None] * self.size
        self.file_path =  file_path
        
        if not os.path.exists(self.file_path):
            open(self.file_path, "w").close()
    
    def hash_function_1(self, key):
        return key % self.size
    
    def hash_function_2(self, key):
        return 7 - (key % 7)
    
    def insert(self, key, value):
        index = self.hash_function_1(key)
        if self.hash_table[index] is None:
            self.hash_table[index] = (key, value)
        else:
            i = 1
            while True:
                new_index = (self.hash_function_1(key) + i * self.hash_function_2(key)) % self.size
                if self.hash_table[new_index] is None:
                    self.hash_table[new_index] = (key, value)
                    break
                i += 1
                
        with open(self.file_path, "a") as f:
            f.write(str(key) + "," + str(value) + "\n")
                
    def search(self, key):
        index = self.hash_function_1(key)
        if self.hash_table[index] is None:
            return None
        elif self.hash_table[index][0] == key:
            return self.hash_table[index][1]
        else:
            i = 1
            while True:
                new_index = (self.hash_function_1(key) + i * self.hash_function_2(key)) % self.size
                if self.hash_table[new_index] is None:
                    return None
                elif self.hash_table[new_index][0] == key:
                    return self.hash_table[new_index][1]
                i += 1
    
    def load_from_file(self):
        with open(self.file_path, "r") as f:
            for line in f:
                key, value = line.strip().split(",")
                self.insert(int(key), int(value))
