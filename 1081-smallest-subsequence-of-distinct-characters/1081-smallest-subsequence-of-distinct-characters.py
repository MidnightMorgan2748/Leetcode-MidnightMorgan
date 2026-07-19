class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_occurrence = {c: i for i, c in enumerate(s)}
        stack = []
        visited = set()
        for i, char in enumerate(s):
            if char in visited:
                continue
            while stack and char < stack[-1] and i < last_occurrence[stack[-1]]:
                removed_char = stack.pop()
                visited.remove(removed_char)
            stack.append(char)
            visited.add(char)
        return "".join(stack)