import re
import sys

# The file being parsed is an annotated flat file, not a genomic FASTA file.

if len(sys.argv) != 3:
    print(
        "Usage: python parse_genomic_features.py "
        "<annotated_record_input> <output_csv>"
    )
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

file_1 = open(input_file, "r")
text = file_1.read()
file_1.close()

genes = []

# Forward strand
genes += [
    (gene, cds, product, "forward")
    for gene, cds, product in re.findall(
        r'/(gene="[0-9]+")(?:(?!FT\s+gene).)*?FT\s+CDS\s+([0-9]+\.\.[0-9]+)(?:(?!FT\s+gene).)*?/product="([^"]+)"',
        text,
        re.DOTALL
    )
]

# Complement strand
genes += [
    (gene, cds, product, "complement")
    for gene, cds, product in re.findall(
        r'/(gene="[0-9]+")(?:(?!FT\s+gene).)*?FT\s+CDS\s+complement\(([0-9]+\.\.[0-9]+)\)(?:(?!FT\s+gene).)*?/product="([^"]+)"',
        text,
        re.DOTALL
    )
]

out = open(output_file, "w")
out.write("gene,cds,product,type,strand\n")

for gene, cds, product, strand in genes:
    if product.lower() == "hypothetical protein":
        product_type = "hypothetical protein"
    else:
        product_type = "other protein"

    gene_num = gene.replace('gene="', '').replace('"', '')
    out.write(f"{gene_num},{cds},{product},{product_type},{strand}\n")

out.close()
