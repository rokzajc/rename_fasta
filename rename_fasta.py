#!/usr/bin/env python3

#Author: Rok Zajc

import os
from Bio import SeqIO
import fnmatch
import re
import argparse

def main():
    parser = argparse.ArgumentParser(description='Rename the fasta and genbank files in a folder to the species whose sequence is represented in the fasta file. Note: file is named after the first contig in a fasta file.')
    parser.add_argument('-i', help='folder where input fasta and genbank files are located (Default=<Current working directory>)', type=str, dest='input', default='' )
    args = parser.parse_args()
    input_mapa=args.input

    for file in os.listdir(os.path.join(os.getcwd(),input_mapa)):
        rename=0
        if fnmatch.fnmatch(file, '*.fna') or fnmatch.fnmatch(file, '*.fasta'):
            with open(os.path.join(os.getcwd(),input_mapa,file)) as f:
                for contig in SeqIO.parse(f, "fasta"):
                    sequence_name=re.split('[.]\d |str[.]|strain|[.] |complete|genome|sequence| |\d* bp|,|/|chromosome|whole|shotgun|=.*',contig.description)
                    for i in range(sequence_name.count('')):
                        sequence_name.remove('')
                    if len(sequence_name)>3:
                        new_name='_'.join(sequence_name[1:])+'.fna'
                        rename=1
                        break
        if fnmatch.fnmatch(file, '*.gbff'):
            with open(os.path.join(os.getcwd(),input_mapa,file)) as f:
                for contig in SeqIO.parse(f, "genbank"):
                    new_name='_'.join(re.split(' |/|[.] ', contig.annotations['organism']))+'.gbff'
                    rename=1
                    break
        if rename==1:
            try:
                os.rename(os.path.join(os.getcwd(),input_mapa,file),os.path.join(os.getcwd(),input_mapa,new_name))
            except FileExistsError:
                pass

if __name__ == "__main__":
    main()
