import re
import sys

# Original file: PARSE GBK.py
# The input and output paths are provided when running the script.

if len(sys.argv) != 3:
    print("Usage: python parse_gbk.py <annotated_record_input> <output_file>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

file_1 = open(input_file, "r")
texto = file_1.read()
file_1.close()

genes = []
genes += re.findall(
    r'/(gene="[0-9]+")(?:(?!FT\s+gene).)*?FT\s+CDS\s+([0-9]+\.\.[0-9]+)',
    texto,
    re.DOTALL
)
genes += re.findall(
    r'/(gene="[0-9]+")(?:(?!FT\s+gene).)*?FT\s+CDS\s+complement\(([0-9]+\.\.[0-9]+)',
    texto,
    re.DOTALL
)

out = open(output_file, "w")
out.write("gene,cds\n")
for gene, cds in genes:
    gene_num = gene.replace('gene="', '').replace('"', '')
    out.write(gene_num + "," + cds + "\n")
out.close()
