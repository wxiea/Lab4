"""
CS 2302

Lab 4 A
"""
import time
from Node import HashTableNode 
from HashTable import HashTable

def LoadFactor(table):
    NumberofNode = 0
    for i in range(len(table)):
        temp = table[i]
        while temp != None:
            NumberofNode +=1
            temp = temp.next
    print("Load factor: " + str((NumberofNode)/ len(table)))
    return
        
def AverageNumberOfComparisons(table):
    lengths = []
    TotalNode = 0
    count = 0
    for i in range(len(table)):
        count = 0
        temp = table[i]
        while temp != None:
            count += 1
            temp = temp.next
            lengths.append(count)
    for i in lengths:
        TotalNode += i
    return TotalNode/len(lengths)
                 
    
def ReadFile(filename):
    table = [None]*5500000 
    with open(filename, encoding ="utf8")as file:
        for line in file:
            values = line.split()
            name = values.pop(0)
            table = HashTable.insert(table, name, values)
        return table
    
def main():
    start = time.time()  
    table = ReadFile("glove.6B.50d.txt")
    print((time.time() - start))
    temp = AverageNumberOfComparisons(table)
    print(str(temp) + " is the average")
    LoadFactor(table)
main()