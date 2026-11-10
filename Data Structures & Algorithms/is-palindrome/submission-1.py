class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        salnum = ''.join(i for i in s.lower() if i.isalnum())
        
        salnumrev="".join(reversed(salnum))

        return salnum==salnumrev