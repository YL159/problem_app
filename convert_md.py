from pathlib import Path
import re

# scan ./problems/ for any unrecorded or modified .py files, and convert to .md
def get_new_py_files(source: Path, dest: Path):
    dest.mkdir(parents=True, exist_ok=True)

    for py_file in source.glob('*.py'):
        md_file = dest / py_file.with_suffix('.md').name
        if not md_file.exists() or py_file.stat().st_mtime > md_file.stat().st_mtime:
            yield py_file


# convert .py file to .md file
def convert_py_to_md(py_file: Path, dest_dir: Path):
    md_file = dest_dir / py_file.with_suffix('.md').name
    source = ''

    with open(py_file, 'r') as f:
        _, front, code = f.read().split("'''\n", 2)
        line1, description = front.split('\n', 1)

        # Parse promblem title, source
        if line1.lower().startswith('leetcode') or line1[0].isnumeric():
            num, title = re.match(r'[\w\s]*(\d+)\. (.+)', line1).groups()
            link = f'https://leetcode.com/problems/{title.replace(' ', '-')}/'
            source = f'[{line1}]({link})\n\n'
        elif ':' in line1:
            source, title = re.match(r'(\w+): (.+)', line1).groups()
            source = f'{source}\n\n'
        else:
            title = line1
        
        # if text line ends with \n, add space to force line break
        description = re.sub(r'(?<=\S)\n', '  \n', description)
        # escape # in description to avoid markdown header
        description = description.replace('#', '\\#')

        # keep original code block
        code_md = f'```python\n{code.strip()}\n```'
    
    with open(md_file, 'w') as f:
        f.write(f'## {title}\n{source}{description}\n\n{code_md}\n')


if __name__ == '__main__':
    problem_dir = Path('./problems')
    md_dir = Path('./frontend/public/problems')

    # # check new or modified .py files
    # for py_file in get_new_py_files(problem_dir, md_dir):
    #     # convert updated .py contents to .md files
    #     convert_py_to_md(py_file, md_dir)

    convert_py_to_md(problem_dir / '84_Largest_Rectangle_Histo.py', md_dir)