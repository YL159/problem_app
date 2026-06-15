from pathlib import Path

def get_new_py_files(directory: str):
    py_files = set(Path(directory).glob('*.py'))
    converted_files = set()
    with open('converted.txt', 'r') as f:
        for line in f:
            converted_files.add(Path(line.strip()))
    return list(py_files - converted_files)


if __name__ == '__main__':
    problem_dir = './problems'
    py_files = get_new_py_files(problem_dir)
    print(len(py_files), py_files[:3])