class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        valid = []

        def generate(s, open, close):
            if open == 0 and close == 0:
                valid.append(s)
                return

            if open > 0:
                generate(s + '(', open - 1, close)

            if close > 0:
                if open < close:
                    generate(s + ')', open, close - 1)

        generate("", n, n)
        return valid
