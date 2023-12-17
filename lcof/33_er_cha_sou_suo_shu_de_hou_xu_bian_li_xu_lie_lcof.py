class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        root = float("inf")

        st = []

        for i in range(len(postorder) - 1, -1, -1):
            if postorder[i] > root:
                return False

            while st and postorder[i] < st[-1]:
                root = st.pop()

            st.append(postorder[i])

        return True
