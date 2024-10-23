#import packages 
import random 
import os 
import textwrap 

#DNA sequence length with one million base pairs
seq_length = 1000000

#DNA nucleotide bases 
bases = ["A", "C" , "G", "T"]

#Generates random DNA sequence with replacement 
random_seq = "".join(random.choices(population = bases, k = seq_length))

#Format sequence with 80 basse pairs per line 
format_seq = '\n'.join(
    random_seq[i:i +80] for i in range(0, len(random_seq), 80)
)

#Save sequence in FASTA format in data directory 
with open("/Users/anyadecarlo/05-first-exam-anya-decarlo/bioinformatics_project/data/random_sequence.fasta", "w") as fasta_file:
    fasta_file.write(format_seq)



