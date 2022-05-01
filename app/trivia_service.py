# here is the code to actually run the game 
# this means display the questions and answers on the interface


import requests
import json
from pprint import pprint
import janitor

url = "https://opentdb.com/api.php?amount=10"

response = requests.get(url)
#print(type(response))
#print(response.text)
#print(type(response.text))
response_data = json.loads(response.text)
#print(type(response_data))

print(response_data)

#this selects all the questions and appends it to this list
question_list = []

for q in response_data["results"]:
    question_list.append(q["question"])
print(question_list)

for question in question_list: 
    if "&quot;" in question:
        question.replace("&quot;", "'")
    if "&#039;s" in question: 
        question.replace("&#039;s", "'")

#this is supposed to print out all of the questions but it prints out the answers as well
for question in question_list:  
    print(question)

#this selects all the answers and appends it to this list
answer_list = []

for q in response_data["results"]:
    answer_list.append(q["correct_answer"])
print(answer_list)

#this is supposed to print out all of the questions but it 
for answer in answer_list:  
    print(answer)