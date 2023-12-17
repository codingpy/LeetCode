class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n

        st = []

        prev = 0

        for log in logs:
            func_id, is_start, timestamp = parse(log)

            if is_start:
                if st:
                    ans[st[-1]] += timestamp - prev

                st.append(func_id)

                prev = timestamp
            else:
                ans[func_id] += timestamp - prev + 1

                st.pop()

                prev = timestamp + 1

        return ans


def parse(log: str) -> Tuple[int, bool, int]:
    func_id, state, timestamp = log.split(":")

    return int(func_id), state == "start", int(timestamp)
