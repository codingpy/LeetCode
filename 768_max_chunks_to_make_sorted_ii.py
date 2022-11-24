class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        st = []

        for num in arr:
            top = num

            while st and num < st[-1]:
                top = max(top, st.pop())

            st.append(top)

        return len(st)
