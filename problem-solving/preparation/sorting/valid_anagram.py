class Solution:
    def isAnagram(self, s: str, t:str) -> bool:
        signature_of_s = [0] * 26
        signature_of_t = [0] * 26
        for i in range(len(s)):
            if  signature_of_s[ord(s[i]) - 97] != 0:
                signature_of_s[ord(s[i]) - 97] += 1
            else: signature_of_s[ord(s[i]) - 97] = 1

        for i in range(len(t)):
            if signature_of_t[ord(t[i]) - 97] != 0:
                signature_of_t[ord(t[i]) - 97] += 1
            else: signature_of_t[ord(t[i]) - 97] = 1
        return signature_of_s == signature_of_t

print(Solution().isAnagram("rat", "car"))
        