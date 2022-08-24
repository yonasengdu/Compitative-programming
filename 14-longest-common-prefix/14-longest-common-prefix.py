class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
            counter = 0
            flag =False
            for i,w in enumerate(strs[0]):
                for j in strs[1:]:
                    if i >= len(j):
                        flag = True
                        break
                    elif j[i] != w:
                            flag = True
                            break

                if flag:
                    break
                counter +=1
                if counter == 0:
                    return ""
            return strs[0][:counter]
