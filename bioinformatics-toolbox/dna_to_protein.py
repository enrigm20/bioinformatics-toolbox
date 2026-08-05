# Original file: DNATOPROT.py

import sys

genetic_code = {
    "TTT": "F", "TTC": "F",
    "TTA": "L", "TTG": "L",
    "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "ATT": "I", "ATC": "I", "ATA": "I",
    "ATG": "M",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",

    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",

    "TAT": "Y", "TAC": "Y",
    "TAA": "*", "TAG": "*",
    "CAT": "H", "CAC": "H",
    "CAA": "Q", "CAG": "Q",
    "AAT": "N", "AAC": "N",
    "AAA": "K", "AAG": "K",
    "GAT": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",

    "TGT": "C", "TGC": "C",
    "TGA": "*",
    "TGG": "W",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AGT": "S", "AGC": "S",
    "AGA": "R", "AGG": "R",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}


# Function to translate DNA
def translate_dna(dna):
    dna = dna.upper().replace("\n", "")
    protein = ""

    for i in range(0, len(dna) - 2, 3):
        codon = dna[i:i+3]
        aa = genetic_code.get(codon, "X")
        if aa == "*":
            break
        protein += aa

    return protein


# Read whichever FASTA and output paths were provided in the command
if len(sys.argv) != 3:
    print("Usage: python dna_to_protein.py <input_fasta> <output_fasta>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file) as infile, open(output_file, "w") as outfile:
    header = ""
    sequence = ""

    for line in infile:
        line = line.strip()

        if line.startswith(">"):
            # If we already read a sequence, translate and write it
            if sequence:
                protein = translate_dna(sequence)
                print(header)
                print(protein, "\n")
                outfile.write(header + "\n")
                outfile.write(protein + "\n")

            header = line
            sequence = ""

        else:
            sequence += line

    # Translate last sequence
    if sequence:
        protein = translate_dna(sequence)
        print(header)
        print(protein)
        outfile.write(header + "\n")
        outfile.write(protein + "\n")

print("\nTranslation complete.")
print(f"Protein FASTA written to: {output_file}")
