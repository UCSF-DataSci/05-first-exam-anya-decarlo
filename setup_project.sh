#! /bin/bash

#Create main project directory 
mkdir -p bioinformatics_project 
#Create subdirectories 
mkdir -p bioinformatics_project/data
mkdir -p bioinformatics_project/scripts
mkdir -p bioinformatics_project/results

#Create Empty Python files in scripts directory touch bioinformatics_project/scripts/generate_fasta.py
touch bioinformatics_project/scripts/dna_operations.py
touch bioinformatics_project/scripts/find_cutsites.py

#Create empty file name in results directory 
touch bioinformatics_project/results/cutside_summary.txt

#Create empty file in data directory 
touch bioinformatics_project/data/random_sequence.fasta

#Create README.md file in main directory 
#!/bin/bash

echo "# Bioinformatics Project Structure

- **data/**: A sub directory for raw and processed data files.
  - \\\`random_sequence.fasta\\\`: An empty placeholder file where a random DNA sequence in FASTA format is stored.
  
- **scripts/**: A sub directory that contains Python scripts for the project tasks.
  - \\\`generate_fasta.py\\\`: Generates random DNA sequences in FASTA format.
  - \\\`dna_operations.py\\\`: Performs complementation, reversal, and reverse complementation operations on DNA sequences.
  - \\\`find_cutsites.py\\\`: Identifies restriction enzyme cut sites in DNA sequences.
  
- **results/**: A subdirectory that stores the output files from the analyses.
  - \\\`cutsite_summary.txt\\\`: A placeholder file where the summary of restriction cut sites is stored." > /Users/anyadecarlo/05-first-exam-anya-decarlo/bioinformatics_prokect/README.md

# Check if everything was created successfully
if [ -d "bioinformatics_project" ]; then
  echo "Project directory structure created successfully:"
  
  # Display the directory structure
  tree bioinformatics_project
else
  echo "Failed to create project directory structure."
fi
