from typing import List

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file"""
    with open(path, 'r') as li: # revise the mode to read and open as li
        lines = [line.strip() for line in li] # store lines included in the file
    return lines

def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[str]:
    """Converts two lists of file paths into a list of json strings"""
    # Preprocess unwanted characters
    def process_file(file):
        if '\\' in file:
            file = file.replace('\\', '\\')
        if '/' or '"' in file:
            file = file.replace('/', '\\/')
            file = file.replace('"', '\\"')
        return file

    # Template for json file
    template_start = '{\"German\":\"'
    template_mid = '\",\"German\":\"'
    template_end = '\"}'

    # Can this be working?
    processed_file_list = []
    for english_file, german_file in zip(english_file_list, german_file_list):
        english_file = process_file(english_file)
        german_file = process_file(german_file) # change variable name to 'german_file' to process the german_file
        json_line = f'{{\"English\":\"{english_file}\",\"German\":\"{german_file}\"}}' # change format for easy debugging
        processed_file_list.append(json_line)
    return processed_file_list


def write_file_list(file_list: List[str], path: str) -> None:
    """Writes a list of strings to a file, each string on a new line"""
    with open(path, 'w') as f: # not a r mode but a w mode to write file
        for file in file_list:
            f.write(file+'\n') # to save data, add 'file'
            
if __name__ == "__main__":
    path = './'
    german_path = './german.txt'
    english_path = './english.txt'

    english_file_list = path_to_file_list(english_path)
    german_file_list = path_to_file_list(german_path)

    # change function to train_file_list_to_json and add more argument for processing file
    processed_file_list = train_file_list_to_json(english_file_list, german_file_list) 

    write_file_list(processed_file_list, path+'concated.json')
