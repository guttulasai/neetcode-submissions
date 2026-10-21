class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result +=str(len(s))+"#"+s
        return result
    def decode(self, s: str) -> List[str]:
        words = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            leng = int(s[i:j])
            word = s[j+1:j+leng+1]
            words.append(word)
            i = j+leng+1
        return words