from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Initialize the count dictionary for characters in t
        d = Counter(t)
        required = len(d)  # Number of unique characters in t that need to be matched
        l = 0
        minlen = float('inf')
        start = 0
        formed = 0  # Number of characters that have met their required frequency in the window
        
        window_counts = {}  # To count the frequency of characters in the current window
        
        for r in range(len(s)):
            char = s[r]
            # Expand the window by including the current character
            window_counts[char] = window_counts.get(char, 0) + 1
            
            # Check if the current character's count matches the required count in t
            if char in d and window_counts[char] == d[char]:
                formed += 1
            
            # Try to contract the window until it ceases to be 'desirable'
            while l <= r and formed == required:
                # Update the minimum window if a smaller valid window is found
                if r - l + 1 < minlen:
                    minlen = r - l + 1
                    start = l
                
                # The character at the left pointer to be removed from the window
                left_char = s[l]
                window_counts[left_char] -= 1
                if left_char in d and window_counts[left_char] < d[left_char]:
                    formed -= 1
                
                # Move the left pointer ahead to find a smaller window
                l += 1
        
        # Return the minimum window or an empty string if no window is found
        return "" if minlen == float('inf') else s[start:start + minlen]
