class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        dic = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in dic:
                if st and st[-1] == dic[c]:
                    st.pop()
                else:
                    return False
            else:
                st.append(c)

        return not st
