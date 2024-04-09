#Sort Characters by Frequency
import heapq
def frequencySort(s):
    freq = {}
    print(freq)
    for char in s:
        #freq[char] = freq.get(char,0) + 1
        if char in freq:
            freq[char]+=1
            print("if", freq)
        else:
            freq[char]=1
            print(freq)
    #max_heap = [(-freq[char], char) for char in freq]
    max_heap=[]
    for char in freq:
        heapq.heappush(max_heap,(-freq[char], char))
        print(max_heap)
    sorted_string = ''
    while max_heap:
        count, char = heapq.heappop(max_heap)
        sorted_string += char * (-count)
    
    return sorted_string
    
    
s="tree"
#s="cccaaa"
#s="abbA"
print(frequencySort(s))

'''
def frequencySort(s: str) -> str:
    # Count frequency of characters
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    # Create a max heap based on negative frequencies
    max_heap = [(-freq[char], char) for char in freq]
    heapq.heapify(max_heap)
    
    # Construct the sorted string
    sorted_string = ''
    while max_heap:
        count, char = heapq.heappop(max_heap)
        sorted_string += char * (-count)
    
    return sorted_string

# Test cases
print(frequencySort("tree"))   # Output: "eert" or "eetr"
print(frequencySort("cccaaa")) # Output: "aaaccc" or "cccaaa"
print(frequencySort("Aabb"))   # Output: "bbAa" or "bbaA"
'''
