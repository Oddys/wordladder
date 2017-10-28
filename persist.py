"""Functions for reading data from and writing data to files."""

from collections import defaultdict
from wordgraph import WordGraph
import pickle


def worddict_from_file(filename):
    """(str) -> dict
    Process a file containing a list of words (one per line) and return
    a dictionary mapping a length of a word (int) to the set of words
    each of which has this length.
    """
    worddict = defaultdict(set)
    with open(filename, 'r') as file_input:
        for line in file_input:
            word = line.strip()
            worddict[len(word)].add(word)
    if not worddict:
        raise ValueError('Dictionary is empty.')
    return worddict


def graphs_from_file(filename):
    """(str) -> dict
    If possible, read a dictionary of graphs from a file.
    Return an empty dictionary otherwise.
    """
    try:
        with open(filename, 'rb') as file_input:
            return pickle.load(file_input)
    except (FileNotFoundError, EOFError):
        return {}


def graphs_to_file(filename, graphs):
    """(str, dict) -> None
    Write a dictionary of graphs to file.
    """
    with open(graphs_filename, 'wb') as file_output:
        pickle.dump(graphs, file_output, pickle.HIGHEST_PROTOCOL)
