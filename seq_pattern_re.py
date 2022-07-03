import sys
from re import search

def read_fasta_hash (filename):
    from re import sub, search

    res = {}
    sequence = None
    info = None
    
    fh = open(filename)

    for line in fh:
        if search(">.*", line):
                if sequence is not None and info is not None and sequence != "":
                    res[info] = sequence
                info = line.partition(" ")[0][1:]          
                sequence = ""
        else:
            if sequence is None: return None
            else: sequence += sub("\s","",line)

    if sequence is not None and info is not None and sequence != "":
                    res[info] = sequence
    fh.close()

    return res


def find_prosite(seq, profile):

    regexp = profile.replace("-","")
    regexp = regexp.replace("x",".")
    regexp = regexp.replace("(","{")
    regexp = regexp.replace(")","}")
    mo = search(regexp, seq)
    if (mo != None):
        return mo.span()[0]
    else:
        return -1


def test():

    seq = "HKMMLASCKHLLCLKCIVKLG"
    print(find_prosite(seq,"C-x-H-x-[LIVMFY]-C-x(2)-C-[LIVMYA]"))


def tester(motif,infile):
    print("Testing 'read_fasta_hash' with file '" + infile + "':\n")
    dic = read_fasta_hash(infile)
    print("Key/Value Pairs:\n")
    for k,v in dic.items():
        print(k+" -> "+v + "\n")

    print("\n\nTesting 'seq_motif_counter' with file '" + infile + "':\n")
    res = seq_motif_counter(motif, infile)
    print("Concensus pattern: \n" + motif) 
    print(" -> Detected by " + infile + ": " + str(res[0]) + " (true positives)")
    print(" -> Undetected by " + infile + ": " + str(res[1]) + " (false negatives)") 


def seq_motif_counter(motif, file):

    dic = read_fasta_hash(file)
    match = 0
    not_match = 0

    for item in dic.values():
        aux = find_prosite(item, motif)
        if aux > 0:
            match += 1
        else: not_match += 1
    return (match, not_match)

		
if __name__ == "__main__":


    motif = "N-x-G-x-R-[LIVM]-D-[LIVMFYH]-x-[LV]-x-S"
    if len(sys.argv) < 2:
        print("Please run the script as 'python seq_pattern_re.py INPUT_FILE'")
    else:
        infile = sys.argv[1]
        tester(motif,infile) 
    

