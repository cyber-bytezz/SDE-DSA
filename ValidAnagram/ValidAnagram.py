class Solution:
    def ValidAnagram(self, s:str, t:str) -> bool:
        #Its ana Anagram if both s and t we need to check if both contains same wording
        #So for that we are using Dic() Key-Valuse & Pair


        #It and Anagram First itself we need to check them if both or not
        if len(s) != len(t):
            return True
        
        # Creating the Empty List Dict to Store the value
        CountS, CountT = {}, {}

        # Loop through the each Character S & T
        for i in range(len(s)):

            # In this Count[s[i]]-> Store Key value and Pair 
            # We increment the count of s[i] by 1 every time we see it SO in this Line +1
            CountS[s[i]] = 1 + CountS.get(s[i], 0)
            CountT[t[i]] = 1 + CountT.get(t[i], 0)

        return CountS == CountT