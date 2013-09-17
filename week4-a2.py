def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return (len(dna1)>len(dna2))

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    count = 0
    for char in dna:
        if (char == nucleotide):
            count = count +1
    return count

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return (dna2 in dna1)

def is_valid_sequence(dna):
    """ (str) -> bool

    The parameter is a potential DNA sequence.
    Return True if and only if the DNA sequence
    is valid (that is, it contains no characters
    other than 'A', 'T', 'C' and 'G').

    >>> is_valid_sequence("ATCGCGTAT")
    True
    >>> is_valid_sequence("ATCGCHGTAT")
    False

    """
    count = True

    for char in dna:
        if char not in "ATCG":
            count = False
        
    return count
    
def insert_sequence(dna1, dna2, i):
    """ (str, str, int) -> str

    The first two parameters are DNA sequences
    and the third parameter is an index.
    Return the DNA sequence obtained by inserting the
    second DNA sequence into the first DNA sequence
    at the given index. (You can assume that the index is valid.)

    >>> insert_sequence("ATCA", "CGCG", 3)
    "ATCCGCGA"
    >>> insert_sequence("ATCA", "CGCG", 0)
    "CGCGATCA"

    """

    dna = ""
    l=len(dna2)
    dna = dna1[:i] + dna2 + dna1[i:]
    return dna

def get_complement(n):
    """ (str) -> str

    The first parameter is a nucleotide
    ('A', 'T', 'C' or 'G'). Return the nucleotide's complement.

    >>> get_complement('A')
    'T'
    >>> get_complement('T')
    'A'
    >>> get_complement('C')
    'G'
    >>> get_complement('G')
    'C'

    """

    if (n == 'A'):
        return 'T'
    elif (n == 'T'):
        return 'A'
    elif (n == 'C'):
        return 'G'
    else:
        return 'C'

def get_complementary_sequence(dna):
    """ (str) -> str

    The parameter is a DNA sequence.
    Return the DNA sequence that is complementary
    to the given DNA sequence.

    >>> get_complementary_sequence("ATCGAT")
    "TAGCTA"
    >>> get_complementary_sequence("CCCGTTTATCGA")
    "GGGCAAATAGCT"

    """

    seq = ""
    for char in dna:
        if (char == "A"):
            seq = seq + "T"
        elif (char == 'T'):
            seq = seq + "A"
        elif (char == "C"):
            seq = seq + "G"
        else:
            seq = seq + "C"

    return seq
