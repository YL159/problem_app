import sqlite3 as sql
from pathlib import Path


from leetcode_query import query_leet, Question


local_db = "leetcode"
table = "questions"

# get cursor of a local sqlite3 db
def get_db(local_db: str=local_db, table: str=table) -> sql.Connection:
    con = sql.connect(local_db)
    cur = con.cursor()

    cur.execute(f"""CREAT TABLE IF NOT EXISTS {table} (
                id: INTEGER PRIMARY KEY, 
                py_name: STRING, 
                md_name: STRING, 
                title: STRING, 
                url: STRING, 
                tags: STRING,
                difficulty: STRING)""")

    return con


def fetch_question(cur: sql.Cursor, py_name: str) -> tuple:
    num = get_num(py_name)
    query = f"SELECT * FROM {table} where id = ?"
    cur.execute(query, (num,))
    return cur.fetchone()


def update_names(con: sql.Connection, py_name: str) -> None:
    md_name = Path(py_name).with_suffix(".md").name

    # assume question id exists in db, and just update file names
    cur = con.cursor()
    query = f"UPDATE {table} SET py_name = ?, md_name = ? WHERE id = ?"
    cur.execute(query, (py_name, md_name, get_num(py_name)))
    con.commit()


def add_question(con: sql.Connection, py_name: str, md_name:str, title_slug: str) -> None:
    q = query_leet(title_slug)

    question = {
        "id": q.id,
        "py_name": py_name,
        "md_name": md_name,
        "title": q.title,
        "url": q.url,
        "tags": ','.join(q.tags),
        "difficulty": q.difficulty
    }

    # assume question id doesn't exist in db
    cur = con.cursor()
    query = f"""
    INSERT INTO {table} VALUES
        (:id, :py_name, :md_name, :title, :url, :tags, :difficulty)
    """
    cur.execute(query, (question,))
    con.commit()


def get_num(file_name: str) -> int:
    num = file_name.split('_', 1)[0]
    return int(num)
