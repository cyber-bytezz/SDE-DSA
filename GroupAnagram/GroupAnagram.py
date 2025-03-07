from ast import List
from collections import defaultdict

class Solution:
    def Anagram(self, str: List[str]) -> List[List[str]]:

        # Create an Empty Dict that will store key:Value
        res = defaultdict(list)

        # in this we are iterating Str -> s
        for s in str:
            # In tihs we need to count all albaher so we are creating the list of 26(o)
            count  = [0] * 26

            # In this we are accesing the Coluum of {26(0)} to make it
            for c in s:


                # In this we are makeing Ascci values that like c =99 a= 97 -> 2 in this 2 
                # but we need to add +1 because of we are starig from 0
                count[[c] - ["a"]] +=1

                # In this we need to covert that to Tuple beause of the the Dict value 
                #and append them in to the store values (s)
                res[tuple(count)].append(s)

                # And this in we need to covert that to List ["",""] -> like this
        return list(res.value())