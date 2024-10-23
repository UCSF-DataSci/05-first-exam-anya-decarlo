#import packages 
import argparse 

#DNA base complement dictionary 
base_complement = {"A" : "T","T": "A", "C":"G", "G":"C"}

#complement sequence function
#returns complement of a DNA Sequence
def complement(sequence): 
    complement_seq = "".join([base_complement[base] for base in sequence.upper()])
    return complement_seq 

#reverse sequence function 
#returns the reverse of a sequence 

def reverse(sequence):
    return sequence[::-1]

#reverse complement sequence function 
#returns the reverse complement of a DNA sequence 

def reverse_complement_sequence(sequence): 
    return reverse(complement(sequence))

def main(): 
    parser = argparse.ArgumentParser()
    parser.add_argument("sequence")
    args = parser.parse_args()

    #converts original sequence to uppercase 
    original_sequence = args.sequence.upper()

    #outputs results
    print("Original sequence:      " ,original_sequence)
    print("Complement:" , complement(original_sequence)) 
    print("Reverse:       " ,reverse(original_sequence))
    print("Reverse complement: ", reverse_complement_sequence(original_sequence))


if __name__ == "__main__":
        main()
