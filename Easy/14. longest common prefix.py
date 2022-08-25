class Solution:
    def longestCommonPrefix(self, strs) -> str:
        prefix = []
        a = []
        for i in range(len(strs[0])):
            for l in strs:
                try:
                    if strs[0] == l:
                        continue

                    if strs[0][i] == l[i]:
                        a.append(True)

                    else:
                        a.append(False)  
                              
                except IndexError:
                    pass
            
            if all(a):
                prefix.append(strs[0][i])

        ans = "".join(prefix)
        
        return ans

b = Solution()
strs = ['flower', 'flow', 'flight']
print(b.longestCommonPrefix(strs))