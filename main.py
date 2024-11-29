from typing import List

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file"""
    lines = open(path, 'r') # 1 : 오탈자 수정, 읽기모드로 변경
    return lines

def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[str]:
    """Converts two lists of file paths into a list of json strings"""
    # Preprocess unwanted characters
    def process_file(file):
        file = file.strip() # 8 : 줄넘김 제거
        if '\\' in file:
            file = file.replace('\\', '\\')
        if '/' or '"' in file:
            file = file.replace('/', '\\/')
            file = file.replace('"', '\\"')
        return file

    # Template for json file
    template_start = '{\"English\":\"' # 7 : German -> English
    template_mid = '\",\"German\":\"'
    template_end = '\"}'

    # Can this be working?
    processed_file_list = []
    for english_file, german_file in zip(english_file_list, german_file_list):
        english_file = process_file(english_file)
        german_file = process_file(german_file) # 2 : eng -> ger
        processed_file_list.append(template_start + english_file + template_mid + german_file + template_end) # 3 시작, 중간, 끝 템플릿 수정
    return processed_file_list


def write_file_list(file_list: List[str], path: str) -> None:
    """Writes a list of strings to a file, each string on a new line"""
    with open(path, 'w') as f: # 4 : 쓰기모드로 변경
        for file in file_list:
            f.write(file + '\n')  # 5 : 파일을 불러올 수 있도록 변경
            
if __name__ == "__main__":
    path = './'
    german_path = './german.txt'
    english_path = './english.txt'

    english_file_list = path_to_file_list(english_path)
    german_file_list = path_to_file_list(german_path)
    processed_file_list = train_file_list_to_json(english_file_list, german_file_list)
    # 6 : german_file_list 변수에 맞게 함수를 변경, processed_file_list 변수에 train_file_list_to_json 적용 

    write_file_list(processed_file_list, path+'concated.json')
