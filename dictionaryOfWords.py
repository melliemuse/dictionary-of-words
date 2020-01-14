
# Lastly, use the for in loop to iterate over the KeyValuePairs and display the entire dictionary to the console.

"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()  
word_definitions = {
    "asynchronous": "having each operation started only after the preceding operation is completed.",
    "juxtapose": "to place close together or side by side, especially for comparison or contrast.",
    "bifurcate": "to divide or fork into two branches.",
}

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""
word_definitions["kvell"] = "to be extraordinarily pleased; especially, to be bursting with pride, as over one's family."
word_definitions["Napoleonic"] = "pertaining to, resembling, or suggestive of Napoleon I, or, less often, Napoleon III, or their dynasty:"

"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""

print(word_definitions["bifurcate"])
print(word_definitions["juxtapose"])


for word in word_definitions.items(): 
    print(f"the definition of {word[0]} is {word[1]}")
""" 
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""