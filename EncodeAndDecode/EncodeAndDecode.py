from typing import List

class Solution:
    def encode(self, words: List[str]) -> str:

        # This is Encodede code that we need to 
        #["apple", "banana", "cherry"] # 5#apple6#banana6#cherry

         # This will store the final encoded message
        encoded_string = ""

        # This will Iterate the word in the words
        for word in words:

            # Store length + '#' + word 
            encoded_string += str(len(word)) + "#" + word  
        return encoded_string

    def decode(self, encoded_string: str) -> List[str]:

        # Tn this we have Declare Encoded string as Main Function

        # List to store the extracted words
        decoded_words = []
        # Pointer to track position while decoding
        current_position = 0  

        # In Python we can also write decoded_words, current position = [], 0

        # Process the entire string using While Loop
        while current_position < len(encoded_string): 
            
            # Start looking for '#'
            separator_position = current_position

            # Find the '#' that separates the length from the word
            while encoded_string[separator_position] != "#":

                # Move forward until we find '#'
                separator_position += 1 

            # Extract length
            word_length = int(encoded_string[current_position:separator_position]) 

            # Word starts after '#' 
            word_start = separator_position + 1  

            # Calculate where the word ends
            word_end = word_start + word_length 
            
            # Extract and store the word
            decoded_words.append(encoded_string[word_start:word_end])  

            # Move to the next encoded word
            current_position = word_end  
        
        return decoded_words  # Return the final list of words
