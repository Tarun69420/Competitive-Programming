class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Initialize a list to count characters in t
        hash_map = [0] * 256
        for char in t:
            hash_map[ord(char)] += 1

        l = 0
        min_len = float('inf')
        start_index = -1
        count = 0

        for r in range(len(s)):
            # If the current character is in t, increase the count of found characters
            if hash_map[ord(s[r])] > 0:
                count += 1
            
            # Decrease the count for the current character
            hash_map[ord(s[r])] -= 1
            
            # Try to shrink the window from the left as much as possible while keeping all characters of t
            while count == len(t):
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    start_index = l
                
                # Restore the count of the left character as we move the left pointer forward
                hash_map[ord(s[l])] += 1
                if hash_map[ord(s[l])] > 0:
                    count -= 1
                
                # Move the left pointer ahead
                l += 1

        # Return the minimum window substring if found, otherwise an empty string
        return "" if start_index == -1 else s[start_index:start_index + min_len]
