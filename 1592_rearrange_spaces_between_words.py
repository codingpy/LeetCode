class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()

        space_num = text.count(" ")

        if len(words) == 1:
            return words[0] + " " * space_num

        return (" " * (space_num // (len(words) - 1))).join(words) + " " * (
            space_num % (len(words) - 1)
        )
