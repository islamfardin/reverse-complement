nucleo = "ACGT"                 # Original data
complement = "TGCA"             # This is the complement of the original data

ask_user = input("Enter sequence to find reverse compliment: ")      # Asks user for sequence
rev_nucleo = ask_user[::-1]                                          # Reverses the sequence by indexing backwards
nucleo_replace = rev_nucleo.maketrans(nucleo,complement)             # Makes use of .maketrans method to replace original seq
                                                                     # with new seq.
rev_comp = rev_nucleo.translate(nucleo_replace)                      # .translate method interprets .maketrans method
print(rev_comp)                                                      # prints new seq
