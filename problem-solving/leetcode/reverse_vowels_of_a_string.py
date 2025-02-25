class Solution:
    def reverseVowels(self, s: str)-> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        word = list(s)

        i,j = 0, len(word) - 1
        while i < j:
            if word[i] in vowels:
                if word[j] in vowels:
                    word[i],word[j] = word[j], word[i]
                    i += 1
                    j -= 1
                else:
                    j -= 1
            else:
                i += 1
        return "".join(word)
