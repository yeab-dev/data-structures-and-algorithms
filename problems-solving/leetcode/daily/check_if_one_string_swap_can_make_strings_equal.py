class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        index = 0
        d = []
        if s1 == s2:
            return True
        elif len(s1) != len(s2):
            return False
        else:
            l1 = list(s1)
            l2 = list(s2)
            for i in range(len(s1)):
                if l1[i] != l2[i]:
                    d.append(i)
        if len(d) > 2 or len(d) < 2:
            return False
        l1[d[0]], l1[d[1]] = l1[d[1]], l1[d[0]]
        return l1 == l2