import heapq
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None                                                               

    
    def __lt__(self, other):
        return self.freq < other.freq

def huffman_encoding(char_freq):
    
    heap = [Node(ch, fr) for ch, fr in char_freq.items()]
    heapq.heapify(heap)

    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    # Step 3: Traverse final tree to get Huffman codes
    codes = {}
    generate_codes(heap[0], "", codes)
    return codes


# ---------- Recursive Helper Function ----------
def generate_codes(node, code, codes):
    if node is None:
        return
    if node.char is not None:
        codes[node.char] = code
        return
    generate_codes(node.left, code + "0", codes)
    generate_codes(node.right, code + "1", codes)


# ---------- Main Program ----------
if __name__ == "__main__":
    print("----- Huffman Encoding using Greedy Strategy -----")

    n = int(input("Enter number of characters: "))
    char_freq = {}

    for i in range(n):
        ch = input(f"Enter character {i+1}: ")
        fr = int(input(f"Enter frequency of '{ch}': "))
        char_freq[ch] = fr

    codes = huffman_encoding(char_freq)

    print("\nHuffman Codes for each character:")
    print("--------------------------------")
    for ch, code in codes.items():
        print(f"{ch} -> {code}")

