class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False 

        length = len(s)
        s_map = {}
        t_map = {} 

        for i in range(length): 
            val1 = s_map.get(s[i], 0)
            val2 = t_map.get(t[i], 0)

            s_map[s[i]] = val1+1
            t_map[t[i]] = val2+1

        for key in s_map.keys(): 
            if t_map.get(key) == None :  
                return False 

            if s_map[key] != t_map[key]: 
                return False 
        
        return True 
        