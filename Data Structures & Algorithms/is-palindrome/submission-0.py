class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        salnum=""
        for i in s:
            if i.isalnum()==True:
                salnum+=i
        
        salnumrev="".join(reversed(salnum))

        if salnum==salnumrev:
            return True
        else:
            return False