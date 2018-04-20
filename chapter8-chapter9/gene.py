# Barbara King
# gene.py

def is_gene(dna):
    cond_1 = dna[0:3] == 'ATG'
    cond_2 = len(dna) % 3 == 0
    cond_3 = dna[len(dna)-3:] == 'TAG' or dna[len(dna)-3:] == 'TAA' or dna[len(dna)-3:] == 'TGA'
    seq_middle = dna[3:len(dna)-3]
    cond_4 = 'TAG' in seq_middle or 'TAA' in seq_middle or 'TGA' in seq_middle

    if not is_valid_DNA(dna):
        return "Not Valid DNA"
    if not cond_1:
        return "Not a potential gene, does not start with ATG"
    if not cond_2:
        return "Not a potential gene, length is not a multiple of 3"
    if not cond_3:
        return "Not a potential gene, must end in TAG, TAA or TGA"
    if cond_4:
        return "Not a potential gene, contains a stop codon"

    return "Is a potential gene"


def is_valid_DNA(seq):

    for char in seq:
        if char not in 'ACGT':
            return False
    return True

def main():
    dna = input("Enter a DNA sequence to verify: ").upper()
    print(is_gene(dna))

main()