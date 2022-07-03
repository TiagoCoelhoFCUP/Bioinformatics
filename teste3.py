####################################################################################################################
###                                    Algorithms for Bioinformatics/ Bioinformatics
###                                         *** Sequence functions              ***    
###
### Pratical Test number: 3
### Group
### Student: Nuno Guilherme Balatrejo Pereira Nunes     Number:201606441
### Student: Tiago da Silva Coelho                      Number:201604170
### Student: Vasco Fernando Coelho Soares               Number:201604364
###
####################################################################################################################
### Add below all the functions from sequence_function.py to be completed and submit in Pratical Test 3


## Exercise 1

def all_orfs (dna_seq):
    """Computes all possible proteins for all open reading frames."""
    assert validate_dna(dna_seq), "Invalid DNA sequence"
    
    # complete
    # ...
    aux = reading_frames(dna_seq)
    print(aux)
    proteins = []

    for i in range(len(aux)):
        aux2 = all_proteins_rf(aux[i])
        proteins.append(aux2)


    return proteins

def all_orfs_ord (dna_seq, minsize = 0):
    """Computes all possible proteins for all open reading frames. Returns ordered list of proteins with minimum size."""
    assert validate_dna(dna_seq), "Invalid DNA sequence"
    rfs = reading_frames (dna_seq)
    res = []
    # complete
    # ...
    aux = all_orfs(dna_seq)
    for i in range(len(aux)):
        insert_prot_ord(aux[i],res)
       
    return res


# Exercise 2
'''add code developed to exercises 2.1 and 2.2'''
def longest_protein(seq):
    
	mods = len(seq) % 3
	if mods == 0:
		upper_seq = seq.upper()
		seq_len = int(len(upper_seq)/3)
		single_seq = ''
		tmp = ''
		for i in range(seq_len):
			range_seq = upper_seq[3*i:3*i+3]
			#print("Protein sequence: " + tmp);
			if range_seq == "ATG":
				#print("Start codon: " + range_seq)
				if len(tmp) == 0:
					tmp = range_seq
				else:
					tmp += range_seq
			elif range_seq == "TAA" or range_seq == "TAG" or range_seq == "TGA":
				#print("Stop codon: " + range_seq)
				tmp += range_seq
				if len(tmp) > len(single_seq):
					#print("Previus biggest sequence was: " + single_seq + " with length: " , len(single_seq))
					single_seq = tmp
					tmp = ''
					#print("New biggest sequence is: " + single_seq + " with length: " , len(single_seq))
			else:
				#print("Codon: " + range_seq)
				if len(tmp) != 0:
					tmp += range_seq
		return single_seq



def count_proteins(otlp):

  tmp = 0
  seq_start = False
  arr = []

  for i in range(50):
    arr.append("");

  counter = 1
  for i in otlp:

    if i == 'M' and not seq_start:
      #print("Start codon and sequence hasn't started: " + i)
      seq_start = True
      arr[counter-1] += i

    elif i == '_' and seq_start:
      tmp += counter
      seq_start = False
      counter = 1
      for p in range(50):
        arr[p] = "";

    elif i == 'M' and seq_start:
      counter += 1
      for j in range(0,counter):
        arr[j] += i
        #print(arr[j])
    else:
      if seq_start:
        for k in range(0,counter):
          arr[k] += i
          #print("Sequence so far: " + arr[k])

  return tmp



# add here the results of 2.2 as a comment.
    #7 proteins found
    #+1 :
    #MVLSPADKTNVKAAWGKVGAHAGEYGAEALER
    #MFLSFPTTKTYFPHFDLSHGSAQVKGHGKKVADALTNAVAHVDDMPNALSALSDLHAHKLRVDPVNFKVSGGPGAIWVEGRDGAFLAGQRITRVAGGVAQAAAAGLGPRPH
    #MPNALSALSDLHAHKLRVDPVNFKVSGGPGAIWVEGRDGAFLAGQRITRVAGGVAQAAAAGLGPRPH
    #+2 :
    #MVRRPWRGEAPSPAPTRAPRPPGPTGHPQPSWPRTQTPPLTLLLPAGCSCPSPPPRPTSRTST
    #MAPSSQGRGSRGLREV
    #+3 :
    #MLLAPWASPQPLLPFLHPYPRGL
    #-1 :
    #MKGVKLDSVPRRVQFPVPFFHRLRDWLRHRVHLLYGLRDRRDSLDVRVFEAHLGQLKFHSPPGPR
    #-2 :
    #none
    #-3 :
    #none



# Exercise 3
def read_fasta_2dictionary(infile):
    f = open(infile,"r")
	dic = {}
	lines = f.readlines()
	key = ""
	value = ""
	
	for line in lines:
		if line[0] == ">":
			if key!="":
				dic[key] = value
			key = line.partition(" ")[0][1:]
			value = ""
		else:
			value = value + line.rstrip()
			
	dic[key] = value	
	f.close()
	
	return dic

if __name__ == "__main__":
    
    # test here all implemented functions
    # used your own defined sequences or read from example files
   # seq = "ATGAAATTATGAATGAGCCTCAGCTGAAGCATCGCGCATCAGACTACGCTCAGACTCAGACTCAGCATTATAGTGAATGTTAATAAATAAAATAA"

   #  print("Reverse:", seq[::-1])

    #print("Exit:", all_orfs_ord(seq))