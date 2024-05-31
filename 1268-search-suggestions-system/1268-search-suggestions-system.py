class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Time Complexity: 
        # Trie Data Structure 
        # Binary Search 

        res = []
        products.sort()

        l, r = 0, len(products) - 1 
        for i in range(len(searchWord)):
            c = searchWord[i]

            # we will have to eliminate the words 
            # which will not have a matching prefix 
            while l <= r and (len(products[l]) <= i or products[l][i] != c):
                l += 1 
            while l <= r and (len(products[r]) <= i or products[r][i] != c):
                r -= 1

            res.append([])
            remain = r - l + 1 
            for j in range(min(3, remain)):
                res[-1].append(products[l + j])
        return res 
