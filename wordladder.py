#!/usr/bin/python3.6
"""A solver for word ladder puzzles."""

import argparse

from wordgraph import WordGraph
from persist import worddict_from_file, graphs_from_file, graphs_to_file


def main(words_filename, graphs_filename=None):
    """Provide user interface for the program."""
    worddict = worddict_from_file(words_filename)
    graphs = graphs_from_file(graphs_filename) if graphs_filename else {}
    start_num_of_graphs = len(graphs)

    while True:
        start = input('Enter your start word: ')
        end = input('Enter your end word: ')
        if not start and not end:
            break
        if len(start) != len(end):
            print('Words must be of the same length.', '\n')
            continue
        if start == end:
            print('You entered the same word twice.', '\n')
            continue

        print('Processing', start, '->', end)
        word_len = len(start)
        print('Getting graph...')
        if word_len in graphs:
            graph = graphs[word_len]
        else:
            graph = WordGraph(worddict[word_len])
            graphs[word_len] = graph
        print('Building ladder...')
        try:
            print(' -> '.join(graph.path(start, end)))
        except TypeError:  # if graph.path returns None
            print(f'{start} -> {end}: It is imposible to build a word ladder.')

        further_choice = input('Do you want to continue? [y/n] ')
        if further_choice.lower() not in ('y', 'yes'):
            print()
            break
        print()

    if graphs_filename and len(graphs) != start_num_of_graphs:
        graphs_to_file(graphs_filename, graphs)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Find the shortest path from word START to word END in which \
        two adjacent words differ by one letter."
    )
    parser.add_argument("words", help="a file with a list of words, one word per line")
    parser.add_argument("-g", "--graphs", help="a file for reading and writing \
                        already created word graphs")
    args = parser.parse_args()
    main(args.words, args.graphs)
