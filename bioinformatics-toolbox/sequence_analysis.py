import re
import sys


# Length function
def length(seq):
    return len(seq)


# GC content function
def gc_cont(seq):
    return (seq.count('G') + seq.count('C')) / len(seq)


# Transcription function
def transcribe(seq):
    return seq.replace('T', 'U')


# Sequence reverse function from the original script
def reverse(seq):
    return seq[::-1]


# Reverse-complement function added for biologically correct negative frames
def reverse_complement(seq):
    complement = seq.translate(str.maketrans('ATCG', 'TAGC'))
    return reverse(complement)


# ORF finder function
# Regex-based ORF detection using start and stop codons
def orfs(seq):
    found = []

    # Only examine codon positions in the frame passed to this function.
    # Without this loop, the same ORF can incorrectly appear in all 3 frames.
    for i in range(0, len(seq)-2, 3):
        if seq[i:i+3] == 'ATG':
            match = re.match(r'ATG(?:...)*?(?:TAA|TAG|TGA)', seq[i:])
            if match:
                found.append(match.group())

    return found


# Translation function
# Codon table used to translate detected ORFs
def translate(seq):
    table = {
        'TTT':'F','TTC':'F','TTA':'L','TTG':'L',
        'TCT':'S','TCC':'S','TCA':'S','TCG':'S',
        'TAT':'Y','TAC':'Y','TAA':'*','TAG':'*',
        'TGT':'C','TGC':'C','TGA':'*','TGG':'W',

        'CTT':'L','CTC':'L','CTA':'L','CTG':'L',
        'CCT':'P','CCC':'P','CCA':'P','CCG':'P',
        'CAT':'H','CAC':'H','CAA':'Q','CAG':'Q',
        'CGT':'R','CGC':'R','CGA':'R','CGG':'R',

        'ATT':'I','ATC':'I','ATA':'I','ATG':'M',
        'ACT':'T','ACC':'T','ACA':'T','ACG':'T',
        'AAT':'N','AAC':'N','AAA':'K','AAG':'K',
        'AGT':'S','AGC':'S','AGA':'R','AGG':'R',

        'GTT':'V','GTC':'V','GTA':'V','GTG':'V',
        'GCT':'A','GCC':'A','GCA':'A','GCG':'A',
        'GAT':'D','GAC':'D','GAA':'E','GAG':'E',
        'GGT':'G','GGC':'G','GGA':'G','GGG':'G'
    }
    protein = ''
    for i in range(0, len(seq)-2, 3):
        codon = seq[i:i+3]
        protein += table.get(codon, 'X')
    return protein


# Function for exercise 1
# Uses the original helper functions to compute metrics, ORFs, and translations
def number_one(seq, output_file):
    fw1 = orfs(seq)
    fw2 = orfs(seq[1:])
    fw3 = orfs(seq[2:])

    # Biological correction: negative frames use the reverse complement
    rev = reverse_complement(seq)
    rv1 = orfs(rev)
    rv2 = orfs(rev[1:])
    rv3 = orfs(rev[2:])

    out = open(output_file, "w")
    out.write("Length of Sequence: " + str(length(seq)) + "\n")
    out.write("GC Content: " + str(gc_cont(seq)) + "\n\n")
    out.write("ORFs in Forward Direction:\n")
    out.write("ORF +1: " + " ".join(fw1) + "\n")
    out.write("ORF +2: " + " ".join(fw2) + "\n")
    out.write("ORF +3: " + " ".join(fw3) + "\n\n")
    out.write("ORFs in Reverse Direction:\n")
    out.write("ORF -1: " + " ".join(rv1) + "\n")
    out.write("ORF -2: " + " ".join(rv2) + "\n")
    out.write("ORF -3: " + " ".join(rv3) + "\n\n")
    out.write("Translated:\n")
    for x in fw1 + fw2 + fw3 + rv1 + rv2 + rv3:
        out.write(translate(x) + "\n")
    out.close()


# Function for exercise 2
def parsing(fasta, output_file):
    gene = re.search(r'gene=([A-Za-z0-9_-]+)', fasta)
    org = re.search(r'ORGANISM\s+(.+)', fasta)
    journals = re.findall(r'JOURNAL\s+(.+)', fasta)

    # The sequence is taken from the final FASTA-style block in the file.
    seq = re.search(r'([ATCG]{10,}(?:\s+[ATCG]+)*)\s*$', fasta, re.DOTALL)
    seq = re.sub(r'\s+', '', seq.group(1))

    out = open(output_file, "w")
    out.write("Gene Abbreviation: " + gene.group(1) + "\n")
    out.write("Organism: " + org.group(1) + "\n\n")
    out.write("Length of Sequence: " + str(length(seq)) + "\n")
    out.write("GC Content: " + str(gc_cont(seq)) + "\n\n")
    out.write("Journals:\n")
    for j in journals:
        out.write(j + "\n")
    out.write("\nSequence:\n" + seq)
    out.close()


if len(sys.argv) != 5:
    print(
        "Usage: python sequence_analysis.py "
        "<dna_input> <annotated_record_input> <orf_output> <summary_output>"
    )
    sys.exit(1)

dna_input = sys.argv[1]
record_input = sys.argv[2]
orf_output = sys.argv[3]
summary_output = sys.argv[4]

# Read whichever input paths were provided in the command
file_1 = open(dna_input).read().upper()
match = re.search(r'[ATCG]{10}.+', file_1, re.DOTALL)
sequence_1 = re.sub(r'\s+', '', match.group())

file_2 = open(record_input).read()

number_one(sequence_1, orf_output)
parsing(file_2, summary_output)
