             code_splits[i] = code_split
 
         # Tokenize the input strings with a regular expression:
        token_lists = [tokenizer.findall(i) if isinstance(i, str) and i.isascii() else [i] for i in code_splits]
         tokens = [j for i in token_lists for j in i]
 
         # Remove newlines at the beginning
