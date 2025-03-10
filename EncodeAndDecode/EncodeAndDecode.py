class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = 1
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j= i+ length
            res.append(s[i:1 + length])
            i += j
        return res
