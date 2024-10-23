#import packages 
import random 
import os 
import textwrap 

#DNA sequence length with one million base pairs
seq_length = 1,000,000

#DNA nucleotide bases 
bases = ["A", "C" , "G", "T"]

#Generates random DNA sequence with replacement 
random_seq = "".join(random.choices)(populatin = bases, k = seq_length)

#Format sequence with 80 basse pairs per line 
format_seq = '\n'.join(random_seq[i:i +80] for i in range(0, len(random_seq), 80)
)



