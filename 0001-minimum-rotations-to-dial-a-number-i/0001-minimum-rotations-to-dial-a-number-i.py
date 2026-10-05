class Solution:
    def minRotations(self, s: str) -> int:
        total_rotations = 0
        current_digit = 0 
        
        for char in s:
            target_digit = int(char)
            diff = abs(target_digit - current_digit)
            total_rotations += min(diff, 10 - diff)

            current_digit = target_digit
            
        return total_rotations


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna