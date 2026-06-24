from pathlib import Path
import re
import json
import textwrap
from leetcode_query import query_leet

PROBLEM_DIR = Path('./problems')
MARKDOWN_DIR = Path('./frontend/public/problems')


# scan ./problems/ for any unrecorded or modified .py files, and convert to .md
def scan_py_files(source: Path, dest: Path) -> None:
    dest.mkdir(parents=True, exist_ok=True)

    for py_file in source.glob('*.py'):
        md_file = dest / py_file.with_suffix('.md').name
        if not md_file.exists() or py_file.stat().st_mtime > md_file.stat().st_mtime:
            convert_py_to_md(py_file, md_file)



# convert .py file to .md file
def convert_py_to_md(py_file: Path, md_file: Path) -> None:
    source = title = info = ''

    with open(py_file, 'r') as f:
        _, front, code = f.read().split("'''\n", 2)
        line1, description = front.split('\n', 1)

        # Parse promblem title, source
        if line1.lower().startswith('leetcode') or line1[0].isnumeric():
            title = re.match(r'[\w\s]*\d+\.(.+)', line1).groups()[0]
            title = title.strip()

            title_slug = title.replace(' ', '-')
            q_data = query_leet(title_slug)

            info = f'''\
            ---
            title: {title}
            tags: {q_data.tags}
            difficulty: {q_data.difficulty}
            ---
            '''

            source = f'[{line1}]({q_data.url})'

        elif ':' in line1:
            source, title = re.match(r'(\w+):(.+)', line1).groups()
            title = title.strip()
            info = f'''\
            ---
            title: {title}
            ---
            '''
        else:
            title = line1.strip()
            info = f'''\
            ---
            title: {title}
            ---
            '''
        info = textwrap.dedent(info)
        # if text line ends with \n, add space to force line break
        description = re.sub(r'(?<=\S)\n', '  \n', description)
        # escape # in description to avoid markdown header
        description = description.replace('#', '\\#')

        # keep original code block
        code_md = f'```python\n{code.strip()}\n```'
    
    with open(md_file, 'w') as f:
        f.write(f'{info}## {title}\n{source}\n\n{description}\n\n{code_md}\n')




if __name__ == '__main__':

    # # check new or modified .py files
    # for py_file in validate_py_files(problem_dir, md_dir):
    #     # convert updated .py contents to .md files
    #     convert_py_to_md(py_file, md_dir)

    convert_py_to_md(PROBLEM_DIR / '84_Largest_Rectangle_Histo.py', MARKDOWN_DIR / '84_Largest_Rectangle_Histo.md')