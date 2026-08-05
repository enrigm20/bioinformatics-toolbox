import sys

def compress1(lis):
    if not lis:
        return []

    uniq = {}
    count = 0
    for i in lis:
        if i not in uniq:
            count = 1
            uniq[i] = count
        elif i in uniq:
            uniq[i] = uniq[i] + 1
    return uniq


if len(sys.argv) != 3:
    print("Usage: python frequency_counter.py <sequence_input> <output_file>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

# Read any sequence file provided by the user and remove whitespace.
sequence = ''.join(open(input_file).read().split())

ke = compress1(sequence)

out = open(output_file, "w")
out.write("counts: " + str(ke) + "\n")
out.close()
