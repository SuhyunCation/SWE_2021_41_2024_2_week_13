from typing import List

def path_to_file_list(path: str) -> List[str]:
    with open(path, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    return lines

def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[str]:
    def process_file(file: str) -> str:
        file = file.replace('\\', '\\\\')
        file = file.replace('/', '\\/')
        file = file.replace('"', '\\"')
        return file

    processed_file_list = []
    for english_file, german_file in zip(english_file_list, german_file_list):
        english_file = process_file(english_file)
        german_file = process_file(german_file)
        json_string = f'{{"English":"{english_file}","German":"{german_file}"}}'
        processed_file_list.append(json_string)
    return processed_file_list

def write_file_list(file_list: List[str], path: str) -> None:
    with open(path, 'w') as f:
        for file in file_list:
            f.write(file + '\n')

if __name__ == "__main__":
    path = './'
    german_path = './german.txt'
    english_path = './english.txt'

    # Read file contents
    english_file_list = path_to_file_list(english_path)
    german_file_list = path_to_file_list(german_path)

    # Convert to JSON
    processed_file_list = train_file_list_to_json(english_file_list, german_file_list)

    # Write to output file
    write_file_list(processed_file_list, path + 'concated.json')
