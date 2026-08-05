# Bioinformatics Toolbox

A small collection of Python scripts I developed while learning and applying basic bioinformatics concepts. The repository includes DNA sequence analysis, ORF detection, DNA-to-protein translation, GenBank feature parsing, and sequence character counting.

These are intentionally kept as simple standalone scripts instead of being converted into a Python package.

## Scripts

| Script | Purpose |
| --- | --- |
| `sequence_analysis.py` | Calculates sequence length and GC content, transcribes DNA, finds ORFs in six reading frames, and translates detected ORFs. |
| `dna_to_protein.py` | Reads multiple DNA FASTA records and translates them into protein sequences. |
| `parse_gbk.py` | Uses regular expressions to extract gene identifiers and CDS coordinates. |
| `parse_genomic_features.py` | Extracts gene, CDS, product, product type, and strand information. |
| `frequency_counter.py` | Counts how many times each character appears in a sequence. |

## Inputs and outputs

The scripts do not require a particular filename or accession. Input and output paths are supplied when each script is run.

| Script | Required input | Output |
| --- | --- | --- |
| `sequence_analysis.py` | Any plain-text file containing a DNA sequence, plus any annotated sequence record containing `gene`, `ORGANISM`, `JOURNAL`, and a final DNA sequence block. | A text ORF-analysis report and a text sequence-record summary. Both output paths are chosen by the user. |
| `dna_to_protein.py` | Any multi-record FASTA file containing DNA sequences. | A protein FASTA file written to the path chosen by the user. |
| `parse_gbk.py` | Any EMBL-style annotated flat file containing `FT gene` and `FT CDS` features. The filename and accession can be anything. | A CSV file containing gene identifiers and CDS coordinates. |
| `parse_genomic_features.py` | Any EMBL-style annotated flat file containing gene, CDS, and product annotations. The filename and accession can be anything. | A CSV file containing gene, CDS, product, product type, and strand. |
| `frequency_counter.py` | Any plain-text sequence file. | A text file containing character counts. |

## Requirements

- Python 3
- No third-party packages

The scripts use `re` and `sys`. Both are included with Python. `sys` is used only to receive input and output paths from the command line.

## How to run

Open a terminal in the repository folder. These examples use the included sample data, but the scripts accept files with any name or path:

```bash
python sequence_analysis.py example_data/dna_sequence.txt example_data/annotated_sequence_record.txt orf_analysis_results.txt sequence_record_summary.txt
python dna_to_protein.py example_data/dna_sequences.fasta translated_proteins.fasta
python parse_gbk.py example_data/annotated_genomic_record.txt gbk_cds_coordinates.csv
python parse_genomic_features.py example_data/annotated_genomic_record.txt genomic_features.csv
python frequency_counter.py example_data/dna_sequence.txt nucleotide_counts.txt
```

The names shown above are examples only. They are not hardcoded requirements.

No package structure, command-line framework, type hints, `pathlib`, `collections`, or external libraries were added. The only new import is `sys`, which reads positional paths from the command line.

## Notes

These scripts are educational utilities rather than replacements for established bioinformatics packages such as Biopython. Their purpose is to show the underlying Python logic directly.

## License

MIT License.
