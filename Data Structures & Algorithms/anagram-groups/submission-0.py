class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        output = {} 

        for string in strs: 
            sorted_string = ''.join(sorted(string)) 
            if sorted_string in output.keys(): 
                output[sorted_string].append(string)
            else: 
                output[sorted_string] = [string]
        
        return list(output.values())