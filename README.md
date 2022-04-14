# Bioinformatics
Projects developed under the Bioinformatics college chair during the 2020/2021 school year

## Sequence Alignments
In bioinformatics, a sequence alignment is a way of arranging the sequences of DNA, RNA, or protein to identify regions of similarity that may be a consequence of functional, structural, or evolutionary relationships between the sequences. Aligned sequences of nucleotide or amino acid residues are typically represented as rows within a matrix. Gaps are inserted between the residues so that identical or similar characters are aligned in successive columns.

The alignments can be either local or global alginments, given that the very basic difference between a local and a global alignments is that in a local alignment, you try to match your query with a substring (a portion) of your subject (reference). Whereas in a global alignment you perform an end to end alignment with the subject (and therefore, you may end up with a lot of gaps in a global alignment if the sizes of query and subject are dissimilar). You may have gaps in local alignment also.

Local Alignment:

```
5' ACTACTAGATTACTTACGGATCAGGTACTTTAGAGGCTTGCAACCA 3' 
             |||| |||||| |||||||||||||||
          5' TACTCACGGATGAGGTACTTTAGAGGC 3'
```
Global Alignment

```
5' ACTACTAGATTACTTACGGATCAGGTACTTTAGAGGCTTGCAACCA 3'
   |||||||||||    |||||||  |||||||||||||| |||||||
5' ACTACTAGATT----ACGGATC--GTACTTTAGAGGCTAGCAACCA 3'
```

In this project we were tasked with implementing 2 well known dynamic programming algorithms to obtain the alignments: The Needleman-Wunsch (Global) algorithm and the Smith-Waterman (local) algorithm, sa well as all auxiliary functions needed:
<ul>
  <li> create_submat (match, mismatch, alphabet) - Creates substitution matrix given the match and missmatch values and the alphabet </li>
  <li> read_submat_file (filename) - Reads a substitution matrix from a file </li>
  <li> score_pos(c1, c2, sm, g) - Scores the individual pair (c1,c2) given the sm substitution matrix and the gap value of g </li>
  <li> score_align (seq1, seq2, sm, g) - Scores the whole alignment (seq1, seq2) given the sm substitution matrix and the gap value of g </li>
  <li> score_affinegap (seq1, seq2, sm, g, r) - Scores the whole alignment (seq1, seq2) given the sm substitution matrix aand the afine gap values of g and r </li>
  <li> recover_align (T, seq1, seq2) - Recovers the alignment obtained by an algorithm given the resulting T traceback matrix and the original sequences </li>
  <li> max_mat(mat) - Finds the cell with the maximum value within a matrix mat </li>
  <li> identity(seq1, seq2, alphabet) - Calculte the identity score between seq1 and seq2 given the alphabet </li>
  <li> print_mat (mat) - Print a matrix mat </li>
</ul>
<br>
To score an alignment you need to score each individual pair of letters. The letters may match, mismatch, or be matched to a gap (a deletion or insertion (indel)):
<ul>
  <li> Match: The two letters at the current index are the same </li>
  <li> Mismatch: The two letters at the current index are different </li>
  <li> Indel (INsertion or DELetion): The best alignment involves one letter aligning to a gap in the other string </li>
  
Each of these scenarios is assigned a score according to the gap value and the substitution matrix and the sum of the scores of all the pairings is the score of the whole alignment candidate.


