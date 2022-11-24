class Solution:
    def solveEquation(self, equation: str) -> str:
        x = 0
        b = 0

        s = 1

        i = 0
        j = 1

        n = len(equation)

        while j < n + 1:
            c = ''

            if j < n:
                c = equation[j]

            if c in ['+', '-', '=', '']:
                item = equation[i:j]

                if item[-1] == 'x':
                    item = item[:-1]

                    if item == '+' or item == '':
                        item = 1
                    elif item == '-':
                        item = -1

                    x += s * int(item)
                else:
                    b += s * int(item)

                i = j

                if c == '=':
                    i += 1
                    j += 1

                    s = -1

            j += 1

        if x:
            return f'x={-b // x}'

        return 'No solution' if b else 'Infinite solutions'
