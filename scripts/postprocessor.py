import numpy as np
import json

with open("/home/jupyter/qanda/data/qa-database-labeled.jsonl", "rb") as inf:
    lines = inf.readlines()
    rows = []
    missed_count = 0
    for line in lines:
        json_f = json.loads(line)
        text = json_f["text"]
        question = json_f["meta"]["question"]
        if "spans" in json_f:
            span_start = json_f["spans"][0]["start"]
            span_end = json_f["spans"][0]["end"]
            answer = text[span_start:span_end]
            row = [text, question, {'text': [answer], 'answer_start': [span_start]}]
            rows.append(row)
        else:
            missed_count += 1
    print(f"Transformed JSONL into JSON dumping out a total of {missed_count} instances' errors")

    outobj = pd.DataFrame(rows, columns=["context", "question", "answers"])
    outobj.to_json('/home/jupyter/qanda/data/qa-database-labeled.json')