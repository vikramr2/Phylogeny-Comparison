import dendropy

alignment = dendropy.DnaCharacterMatrix.get(path='rose.aln.true.fasta', schema='fasta')
alignment.write(path='rose.aln.true.phylip', schema='phylip')