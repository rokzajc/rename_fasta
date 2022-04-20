# rename_fasta
Automatically rename fasta and genbank file to the species name mentioned in the file

Fasta and genbank files containing genome sequnces, downloaded from NCBI website do not have the name of the species from which the genome is obtained from. This tool automatically renames the files to the name of the organism, from which the sequence was obtained. For fasta files, the program generates a name based on the first contig in the file, for genbank files, the name is generated based on "organism" attribute.

## INSTALLATION
The program can be installed for easier acces in Linux, however they can be ran on other operating systems (including Linux) without installation. Without installation programs must be ran as any python script: `python rename_fasta.py -i <inputdirectory>

### Linux:
Download ZIP file and extract it anywhere. Open terminal in the directory which was created and run these commands:
```
chmod +x rename_fasta.py
cp rename_fasta.py ~/.local/bin/rename_fasta
```

After the installation the coligo.py and intetra.py scripts should be executable from any directory using command "rename_fasta".

## EXAMPLE
`rename_fasta -i <inputdirectory>`

## REQIREMENTS
  python3.6
  biopython
