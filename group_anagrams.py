class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = {}
        for word in strs:
            temp = "".join(sorted(list(word)))
            if temp in mydict.keys(): mydict[temp].append(word)
            else: mydict[temp] = [word]
        
        return list(mydict.values())
        
