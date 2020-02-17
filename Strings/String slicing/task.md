Slicing is used to get multiple characters (a substring) from a string. Its syntax is similar to that of indexing, but instead of just one index you use two indices (numbers) separated by a colon, e.g. `['str[ind1:ind2]']` .##### Example

 `['\nstr[start:end] # items start through end-1\nstr[start:]    # items start through the rest of the array\nstr[:end]      # items from the beginning through end-1\nstr[:]         # a copy of the whole array\n']` Use slicing to get `['"Python"']` from the `['monty_python']` variable.  
You can leave one or both indices empty.