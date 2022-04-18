# rename_fasta
Automatically rename fasta and genbank file to the species name mentioned in the file

Fasta and genbank files containing genome sequnces, downloaded from NCBI website do not have the name of the species from which the genome is obtained from. This tool automatically renames the files to the name of the organism, from which the sequence was obtained. For fasta files, the program generates a name based on the first contig in the file, for genbank files, the name is generated based on "organism" attribute.
