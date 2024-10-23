#import modules
import os 
import sys 
import argparse 

#read FAFSTA file 
def read_fasta(fasta_file):
    with open( fasta_file, "r" ) as file:
        lines = file.readlines()
    sequence = "".join(line.strip() for line in lines if not line.startswith(">"))
    return sequence 

#find occurences of the cut sites 
def find_occurences(dna, cut_site): 
    remove_pipe = cut_site.replace('|', "")
    locations = []
    index = dna.find(remove_pipe)
    while index != -1:
        locations.append(index)
        index = dna.find(remove_pipe, index +1)
    return locations 

#find all pairs of cutsite base pairs (80-120 kbp) apart
def  find_pairs(locations): 
    pairs = []
    for i in range(len(locations)):
        for j in range (i +1, len(locations)): 
            length = locations[j] - locations[i]
            if 80000 <= length <= 120000:
                pairs.append((locations[i], locations[j]))
    return pairs

def save_summary_results(pairs, summary_file):
    with open(summary_file, "w") as file:
        file.write("Total cut sites found:" + str(len(pairs)) + "\n")
        file.write("First 5 pairs:\n")
        for pair in pairs[:5]:
            file.write(f"{pair[0]},{pair[1]}\n")

def main (): 
    fasta_file = sys.argv[1]
    cut_site = sys.argv[2]
    summary_file = "/Users/anyadecarlo/05-first-exam-anya-decarlo/bioinformatics_project/results/cutsite_summary.txt"
    dna_sequence = read_fasta(fasta_file)
    positions = find_occurences(dna_sequence, cut_site)
    pairs = find_pairs(positions)
    save_summary_results = (pairs, summary_file)
    print(f"Total cut site pairs found: {len(pairs)}")

if __name__ == "__main__": 
    main ()