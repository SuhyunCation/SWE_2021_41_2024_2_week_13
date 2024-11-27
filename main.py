from typing import List

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file"""
    lines = open(path, 'r').read().split('\n') #잘못된 변수명 li를 line으로 변경, file open option을 w->r로 수정,'\n'을 기준으로 나눠서 읽도록 수정
    return lines

def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[str]:
    """Converts two lists of file paths into a list of json strings"""
    # Preprocess unwanted characters
    def process_file(file):
        if '\\' in file:
            file = file.replace('\\', '\\\\')
        if '/' or '"' in file:
            file = file.replace('/', '\\/')
            file = file.replace('"', '\\"')
        return file

    # Template for json file
    template_start = '{\"English\":\"' # German -> English
    template_mid = '\",\"German\":\"'
    template_end = '\"}'

    # Can this be working?
    processed_file_list = []
    for english_file, german_file in zip(english_file_list, german_file_list):
        english_file = process_file(english_file)
        german_file = process_file(german_file) #파일명을 english_file -> german_file로 수정

        processed_file_list.append(template_start + english_file + template_mid + german_file + template_end)
        #mid eng start ger start -> start eng mid ger end 로 순서 수정
    return processed_file_list


def write_file_list(file_list: List[str], path: str) -> None:
    """Writes a list of strings to a file, each string on a new line"""
    with open(path, 'w') as f: #file open option을 r->w로 수정
        for file in file_list:
            f.write(file + '\n') #file을 출력하게끔 수정
            
if __name__ == "__main__":
    path = './'
    german_path = './german.txt'
    english_path = './english.txt'

    english_file_list = path_to_file_list(english_path)
    german_file_list = path_to_file_list(german_path) #train_file_list_to_json -> path_to_file_list

    processed_file_list = train_file_list_to_json(english_file_list, german_file_list) #path_to_file_list -> train_file_list_to_json

    write_file_list(processed_file_list, path+'concated.json')
