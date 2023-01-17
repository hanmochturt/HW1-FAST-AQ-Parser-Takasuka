from seqparser import (
        FastaParser,
        FastqParser,
        transcribe,
        reverse_transcribe)

import os
import pathlib
import file_format
from typing import Dict, Tuple

DATA_FOLDER = "data"
FASTA_FILETYPE = ".fa"
FASTQ_FILETYPE = ".fq"


def main():
    """
    The main function
    """
    fasta_file, fastq_file = find_fasta_fastq_files()

    # Create instance of FastaParser
    # Create instance of FastqParser

    fasta_parser = FastaParser(fasta_file)
    fastq_parser = FastqParser(fastq_file)
        
    # For each record of FastaParser, Transcribe the sequence
    # and print it to console

    for seq_name, seq in fasta_parser:
        print(seq_name, transcribe(seq))
       
    # For each record of FastqParser, Transcribe the sequence
    # and print it to console

    for seq_name, seq, _ in fastq_parser:
        print(seq_name, transcribe(seq))

    # For each record of FastaParser, Reverse Transcribe the sequence
    # and print it to console

    for seq_name, seq in fasta_parser:
        print(seq_name, reverse_transcribe(seq))

    # For each record of FastqParser, Reverse Transcribe the sequence
    # and print it to console

    for seq_name, seq, _ in fastq_parser:
        print(seq_name, reverse_transcribe(seq))

"""
When executing a python script from the command line there will
always be a hidden variable `__name__` set to the value `__main__`.

Since this is guaranteed you can execute your `main` function with
the following if statement
"""


def find_fasta_fastq_files() -> Tuple:
    """find first .fa and .fq files in the parent directory"""
    parent_this_filepath = pathlib.Path(__file__).parent.resolve()
    fa_fq_filenames = find_fasta_fastq_files_from_folder(parent_this_filepath / "data")
    fasta_file = parent_this_filepath / "data" / fa_fq_filenames[FASTA_FILETYPE]
    fastq_file = parent_this_filepath / "data" / fa_fq_filenames[FASTQ_FILETYPE]
    return fasta_file, fastq_file


def find_fasta_fastq_files_from_folder(folder: str) -> Dict:
    """find first .fa and .fq files"""
    files = os.listdir(folder)
    fasta_fastq_files = dict.fromkeys([FASTA_FILETYPE, FASTQ_FILETYPE])
    for filename in files:
        file_type = file_format.find_filetype(filename)
        if file_type == FASTA_FILETYPE or file_type == FASTQ_FILETYPE:
            fasta_fastq_files[file_type] = filename
    return fasta_fastq_files


if __name__ == "__main__":
    main()
