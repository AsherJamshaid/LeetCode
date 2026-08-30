class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        def padding(num: int) -> str:
            st = str(num)
            while len(st) < 4:
                st = "0" + st
            return st

        p = padding(num1)
        q = padding(num2)
        r = padding(num3)

        ans = ""
        for i in range(4):
            ans += str(min(int(p[i]), int(q[i]), int(r[i])))
        return int(ans)
