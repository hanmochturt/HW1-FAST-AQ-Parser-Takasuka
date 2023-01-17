# DNA -> RNA Transcription

TRANSCRIPTION_PAIRS = {"A": "U", "C": "G", "T": "A", "G": "C"}


def transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA by generating
    the complement sequence with T -> U replacement
    """
    transcribed_seq_list = []

    for nucleotide in seq:
        transcribed_nucleotide = TRANSCRIPTION_PAIRS[nucleotide]
        transcribed_seq_list.append(transcribed_nucleotide)
    return "".join(transcribed_seq_list)


def reverse_transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA then reverses
    the strand
    """
    seq = seq[::-1]
    return transcribe(seq)
