import pandas as pd
import numpy as np
import json

import ujson
from pathlib import Path

def read_jsonl(file_path):
    """Read a .jsonl file and yield its contents line by line.
    file_path (unicode / Path): The file path.
    YIELDS: The loaded JSON contents of each line.
    """
    with Path(file_path).open('r', encoding='utf8') as f:
        for line in f:
            try:  # hack to handle broken jsonl
                yield ujson.loads(line.strip())
            except ValueError:
                continue


def write_jsonl(file_path, lines):
    """Create a .jsonl file and dump contents.
    file_path (unicode / Path): The path to the output file.
    lines (list): The JSON-serializable contents of each line.
    """
    data = [ujson.dumps(line, escape_forward_slashes=False) for line in lines]
    Path(file_path).open('w', encoding='utf-8').write('\n'.join(data))

outf = open('processed.jsonl', 'w')
lines_all = []

for line in read_jsonl("context-question-to-label-processed.json"):
    question = line["question"]
    del line["question"]
    line["meta"] = {"question": question}
    lines_all.append(line)

write_jsonl("processed.jsonl", lines_all)
