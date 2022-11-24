class Solution:
    def fib(self, n: int) -> int:
        return fib(n) % 1_000_000_007


def fib(n: int) -> int:
    # A = np.array([[1, 1], [1, 0]], dtype=object)

    # return int(
    #     np.matmul(matrix_power(A, n), [1, 0])[1]
    # )

    a, b = 0, 1

    for _ in range(n):
        a, b = b, a + b

    return a
