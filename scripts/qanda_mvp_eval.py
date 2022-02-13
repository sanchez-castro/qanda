from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import torch
 
tokenizer = AutoTokenizer.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")
model = AutoModelForQuestionAnswering.from_pretrained("kamilali/distilbert-base-uncased-finetuned-squad")

print("Provide a description of the product:", '\n')
# The Kind Bar has 15 grams of sugar and 10 grams of protein.
text = input()

print("\nProvide questions to ask the model, and press enter twice when finished:", '\n')
# questions = [
#         "What is the bar?",
#         "How many grams of sugar does it have?",
#         "How many grams of protein does it have?"
# ]

cq = input()
questions = []
while cq != "":
    questions.append(cq)
    cq = input()

print("Context provided:", text)
print("Questions asked:", questions)

print("-----")
 
for question in questions:
    inputs = tokenizer.encode_plus(question, text, add_special_tokens=True, return_tensors="pt")
    input_ids = inputs["input_ids"].tolist()[0]
 
    text_tokens = tokenizer.convert_ids_to_tokens(input_ids)
    out = model(**inputs)
    answer_start_scores, answer_end_scores = out[0], out[1]
 
    answer_start = torch.argmax(answer_start_scores)
    answer_end = torch.argmax(answer_end_scores) + 1
 
    answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(input_ids[answer_start:answer_end]))
 
    print(f"Question: {question}")
    print(f"Answer: {answer}\n")
