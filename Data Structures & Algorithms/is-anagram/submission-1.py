class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False 
        
        s_map = {}
        t_map = {} 

        length = len(s)

        for i in range(length):
            if s[i] in s_map: 
                s_map[s[i]] += 1
            else: 
                s_map[s[i]] = 1

            if t[i] in t_map: 
                t_map[t[i]] += 1
            else: 
                t_map[t[i]] = 1

        for val in s_map.keys(): 
            if t_map.get(val) is None: 
                return False 

            if t_map[val] != s_map[val]: 
                return False 

        return True      