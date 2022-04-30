import requests

url = "https://opentdb.com/api.php?amount=10"

#this code fecthes the questions
question_list = []

for q in response_data["results"]:
    question_list.append(q["question"])
print(question_list)


#this code fetches the answers
answer_list = []

for q in response_data["results"]:
    answer_list.append(q["correct_answer"])
print(answer_list)


for question in question_list  
    print(question["question"])