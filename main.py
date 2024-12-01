import json
from typing import List


def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file"""
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]


def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[str]:
    """Converts two lists of sentences into a list of json strings"""
    # Template for json file
    processed_file_list = []
    for english_sentence, german_sentence in zip(english_file_list, german_file_list):
        json_object = {
            "English": english_sentence,
            "German": german_sentence
        }
        processed_file_list.append(json.dumps(json_object, ensure_ascii=False))
    return processed_file_list


def write_file_list(file_list: List[str], path: str) -> None:
    """Writes a list of strings to a file, each string on a new line"""
    with open(path, 'w', encoding='utf-8') as f:
        f.write('[')
        f.write(',\n'.join(file_list))
        f.write(']\n')


if __name__ == "__main__":
    path = './'
    german_path = './german.txt'
    english_path = './english.txt'

    # Read the lines from the text files
    english_file_list = path_to_file_list(english_path)
    german_file_list = path_to_file_list(german_path)

    # Convert the lines to JSON strings
    processed_file_list = train_file_list_to_json(english_file_list, german_file_list)

    # Write the result to concated.json
    write_file_list(processed_file_list, path + 'concated.json')
