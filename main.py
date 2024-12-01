from typing import List

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file"""
    with open(path, 'r') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[str]:
    """Converts two lists of file paths into a list of json strings"""
    # Preprocess unwanted characters
    def process_file(file: str) -> str:
        file = file.replace('\\', '\\\\')  # Escape backslashes
        file = file.replace('/', '\\/')    # Escape forward slashes
        file = file.replace('"', '\\"')   # Escape double quotes
        return file

    # Template for json format
    processed_file_list = []
    for english_file, german_file in zip(english_file_list, german_file_list):
        english_file = process_file(english_file)
        german_file = process_file(german_file)

        json_entry = f'{{"English":"{english_file}","German":"{german_file}"}}'
        processed_file_list.append(json_entry)
    return processed_file_list

def write_file_list(file_list: List[str], path: str) -> None:
    """Writes a list of strings to a file, each string on a new line"""
    with open(path, 'w') as f:
        for file in file_list:
            f.write(file + '\n')

if __name__ == "__main__":
    path = './'
    german_path = './german.txt'
    english_path = './english.txt'

    # Read input files
    english_file_list = path_to_file_list(english_path)
    german_file_list = path_to_file_list(german_path)

    # Convert to JSON format
    processed_file_list = train_file_list_to_json(english_file_list, german_file_list)

    # Write output to concated.json
    write_file_list(processed_file_list, path + 'concated.json')

