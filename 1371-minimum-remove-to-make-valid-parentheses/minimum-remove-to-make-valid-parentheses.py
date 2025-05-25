class Solution:
    def minRemoveToMakeValid(self, s):
        left_count = 0
        right_count = 0
        stack = []

        # Pass 1: Count parentheses and filter invalid right parentheses
        for ch in s:
            if ch == '(':
                left_count += 1
            elif ch == ')':
                right_count += 1
            if right_count > left_count:
                right_count -= 1  # Ignore this right parenthesis
            else:
                stack.append(ch)  # Valid character

        result = ""

        # Pass 2: Remove unmatched left parentheses
        while stack:
            current_char = stack.pop()
            if left_count > right_count and current_char == '(':
                left_count -= 1  # Ignore this left parenthesis
            else:
                result += current_char  # Add valid character to result

        # Reverse the result string to get the final valid string
        return result[::-1]
