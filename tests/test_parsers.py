# write tests for parsers
# test using "pytest" in command line
import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.resolve()))

from seqparser import (
        FastaParser,
        FastqParser)
import example
import data.make_seq


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser
    class here. You should generate an instance of
    your FastaParser class and assert that it properly
    reads in the example Fasta File.
    """
    fasta_file, fastq_file = example.find_fasta_fastq_files()
    fasta_parser = FastaParser(fasta_file)
    for _, seq in fasta_parser:
        for character in seq:
            assert character in data.make_seq.ALPHABET


def test_FastqParser():
    """
    Write your unit test for your FastqParser
    class here. You should generate an instance of
    your FastqParser class and assert that it properly
    reads in the example Fastq File.
    """
    fasta_file, fastq_file = example.find_fasta_fastq_files()
    fastq_parser = FastqParser(fastq_file)
    quality_characters = ''.join([chr(j) for j in range(data.make_seq.PHRED_MIN,
                                                        data.make_seq.PHRED_MAX)])
    for _, seq, q in fastq_parser:
        for character in seq:
            assert character in data.make_seq.ALPHABET
        for character in q:
            assert character in quality_characters
