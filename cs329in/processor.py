import pandas as pd
import numpy as np
import json

data = pd.read_excel('protein-bar-qanda.xlsx')

out = []

for entry in data.iterrows():
    if isinstance(entry[1]["question"], str):
        curr = {}
        curr["text"] = entry[1]['product_full_description'].replace("\"", "")
        curr["meta"] = {}
        curr["meta"]["question"] = entry[1]['question']
        out.append(curr)

print(len(out))
with open("processed.jsonl", "w") as outf:
    for entry in out:
        entry_out = str(entry)
        entry_out = entry_out.replace("\'text\'", "\"text\"")
        entry_out = entry_out.replace("\'meta\'", "\"meta\"")
        entry_out = entry_out.replace("\'question\'", "\"question\"")
        entry_out = entry_out.replace("\'{", "\"{")
        entry_out = entry_out.replace("\'}", "\"}")
        entry_out = entry_out.replace("\',", "\",")
        entry_out = entry_out.replace(": \'", ": \"")
        outf.write( entry_out + "\n")
