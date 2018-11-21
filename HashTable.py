import math

class HashTable:  

    def HashFunction1(value,length):
        total =  float(1)
        for i in range(len(value)):
            Char_value = ord(value[i])
            total = Char_value * (total+1)
        return total % length
    
    def HashFunction2(value,length):  
        total =  0 
        for i in range(len(value)):
            Char_value = ord(value[i])
            total = Char_value + total
        return total % length
    
    def HashFunction3(value,length):
        s = 0
        for k in value:
            s = s + ord(k)
        return s % length
    
    def insert(HashTable, key, value):
        HashKey = HashFunction1(key)
        HashTable[HashKey].append(value)
