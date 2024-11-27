from typing import List

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file"""
    with open(path, 'r') as f:  # 'w' -> 'r'로 수정
        lines = [line.strip() for line in f.readlines()]  # lines 변수 추가
    return lines

def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[str]:
    """Converts two lists of file paths into a list of json strings"""
    # Preprocess unwanted characters
    def process_file(file):
        if '\\' in file:
            file = file.replace('\\', '\\\\')  # 이스케이프 처리
        if '/' in file or '"' in file:  # 수정: 조건 구문 분리
            file = file.replace('/', '\\/')
            file = file.replace('"', '\\"')
        return file

    # Template for json file
    template_start = '{"English":"'
    template_mid = '","German":"'
    template_end = '"}'

    processed_file_list = []
    for english_file, german_file in zip(english_file_list, german_file_list):
        english_file = process_file(english_file)  # 수정: 각각 파일을 처리
        german_file = process_file(german_file)

        json_string = template_start + english_file + template_mid + german_file + template_end
        processed_file_list.append(json_string)
    return processed_file_list


def write_file_list(file_list: List[str], path: str) -> None:
    """Writes a list of strings to a file, each string on a new line"""
    with open(path, 'w') as f:  # 'r' -> 'w'로 수정
        for file in file_list:
            f.write(file + '\n')  # 수정: 줄바꿈 추가
            
if __name__ == "__main__":
    path = './'
    german_path = './german.txt'
    english_path = './english.txt'

    english_file_list = path_to_file_list(english_path)
    german_file_list = path_to_file_list(german_path)  # 수정: 올바른 함수 호출

    processed_file_list = train_file_list_to_json(english_file_list, german_file_list)  # 수정: 올바른 변수 전달

    write_file_list(processed_file_list, path + 'concated.json')  # 수정: 파일 경로 전달