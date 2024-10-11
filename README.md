# DS-217 Exam 1

## Instructions
- This exam consists of four interconnected questions that will guide you through a bioinformatics project workflow.
- Submit your solutions as separate files with the names specified in each question.
- Make sure your code is well-commented and follows good programming practices.
- You may use any built-in Python libraries or standard command-line tools, but no external packages.

## Question 1: Project Setup (15 points)

@@ -93,9 +92,9 @@ Create a Python script that performs various operations on DNA sequences. Your sript should:

1. Accept a DNA sequence as a command-line argument.
2. Implement the following functions:
   - `complement(sequence)`: Returns the complement of a DNA sequence (A -> T, C -> G, G -> C, T -> A).
   - `reverse(sequence)`: Returns the reverse of a sequence (e.g. "CCTCAGC" -> "CAGCCTC").
   - `reverse_complement(sequence)`: Returns the reverse complement of a DNA sequence (e.g. "CCTCAGC" -> "GAGCTTG"); i.e. the reverse of the complement (apply `complement` then `reverse`, or vice versa).
   - `complement(sequence)`: Returns the complement of a DNA sequence (A -> T, C -> G, G -> C, T -> A; e.g., "CCTCAGC" -> "GGAGTCG").
   - `reverse(sequence)`: Returns the reverse of a sequence (e.g. "CCTCAGC" -> "CGACTCC").
   - `reverse_complement(sequence)`: Returns the reverse complement of a DNA sequence (e.g. "CCTCAGC" -> "GCTGAGG"); i.e. the reverse of the complement (apply `complement` then `reverse`, or vice versa).
3. For the input sequence, print:
   - The original sequence
   - Its complement
@@ -144,7 +143,9 @@ Create a Python script that finds pairs of restriction enzyme cut sites that are
3. Find all occurrences of the cut site (specified below) in the DNA sequence.
4. Find all pairs of cut site locations that are 80,000-120,000 base pairs (80-120 kbp) apart.
5. Print the total number of cut site pairs found and the positions of the first 5 pairs.
6. Save a summary of the results in the results directory as "distant_cutsite_summary.txt".
6. Save a summary of the results (example below) in the results directory as "distant_cutsite_summary.txt".
**NOTE:** This problem originally required searching for reverses, complements, and reverse complements. For simplicity, only use the cut site sequence as written (no reverse, no complement, definitely no reverse complement).

Tips:
- When running the script, put the cut site sequence in quotes to prevent issues with the pipe character, e.g., "G|GATCC".
@@ -161,9 +162,9 @@ Run the script on the random sequence you generated in Question 2 and with cut s
python find_distant_cutsites.py data/random_sequence.fasta "G|GATCC"
`````

Expected output:
Expected output (results/distant_cutsite_summary.txt):
`````
Analyzing cut site: GGATCC
Analyzing cut site: G|GATCC
Total cut sites found: 976
Cut site pairs 80-120 kbp apart: 1423
First 5 pairs:
@@ -172,6 +173,4 @@ First 5 pairs:
3. 28764 - 109102
4. 28764 - 126471
5. 42198 - 122609
Results saved to bioinformatics_project/results/distant_cutsite_summary.txt
`````
