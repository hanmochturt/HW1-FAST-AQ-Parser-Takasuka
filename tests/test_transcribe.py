# write tests for transcribes
# test using "pytest" in command line
import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.resolve()))

from seqparser import (
        transcribe,
        reverse_transcribe)

SEQUENCE = "CAAACCGGCGATGCGG"
TRANSCRIBED_SEQ = "GUUUGGCCGCUACGCC"
REV_TRANSCRIBED_SEQ = "CCGCAUCGCCGGUUUG"


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the
    transcribe function here.
    """
    assert transcribe(SEQUENCE) == TRANSCRIBED_SEQ


def test_reverse_transcribe():
    """
    Write your unit test for the
    reverse transcribe function here.
    """
    assert reverse_transcribe(SEQUENCE) == REV_TRANSCRIBED_SEQ
