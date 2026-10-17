class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        pre, ele = "", min(strs)
        for i in range(len(ele)):
            for j in strs:
                if j[i] == ele[i]:
                    con = True
                else:
                    con = False
                    return pre
            if con == True:
                pre = pre + ele[i]
        return pre