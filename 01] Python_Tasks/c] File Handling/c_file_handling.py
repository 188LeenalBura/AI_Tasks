# Read a text file || file name : 'script.txt'

with open("script.txt", "r") as f:
    script = ( f.read() )
    

# Count the number of words in the 'script.txt' file    
                                    # split(): Breaks a sentence into individual words, using spaces as separators. 
words_list = script.split()         # It turns the sentence into a list of words.
count_words = len(words_list)       # len(): Counts how many items ( words ) are in the list

result = ( f"There are {count_words} words in a 'script.txt' file" )      


# Write the result to a new file 

with open("result.txt","w") as f:
    f.write( str(result) )
