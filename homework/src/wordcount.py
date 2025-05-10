# python3 -m homework data/input data/output
import os

from homework.src._internals.parse_args import parse_args
from homework.src._internals.read_all_lines import read_all_lines


def preprocess_lines(lines):
    return [line.strip().lower() for line in lines]


def split_into_words(lines):
    words = []
    for line in lines:
        words.extend(word.strip(",.!?;:") for word in line.split())
    return words


def count_words(words):
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts


def write_word_counts(output_folder, word_counts):

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_file = os.path.join(output_folder, "wordcount.tsv")

    with open(output_file, "w", encoding="utf-8") as f:
        for word, count in word_counts.items():
            f.write(f"{word}\t{count}\n")


def main():
    input_folder, output_folder = parse_args()
    lines = read_all_lines(input_folder)
    preprocessed_lines = preprocess_lines(lines)
    words = split_into_words(preprocessed_lines)
    word_counts = count_words(words)
    write_word_counts(word_counts, output_folder)
