# Prodigy run

Data schema for Q&A labeling should bea JSONL following convention:

```
{“text”: “<context of the product>”, “meta”: {“question”: “question to be answer in the text/context”}}:
``` 
\*Question will be displayed on the lower right corner

### Process
1. Getting data with context & questions into our prodigy local machine with: <br>
`gsutil cp gs://unlabeled-data-ml-q-a/context-question-to-label.jsonl . `

2. Confirm the dataset that you will use: # <br>
`python3 -m prodigy stats -l`
  - You can drop datasets with: `python3 -m prodigy drop test_qanda_extractive` 

3. Lanuch prodigy server with: <br>
`PRODIGY_HOST=0.0.0.0 PRODIGY_PORT=80 python3 -m prodigy qa qa-test en_core_web_sm ./data/context-question-to-label.jsonl.jsonl -F prodigy-recipes/other/extractive_qa.py`
