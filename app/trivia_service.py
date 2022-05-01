# here is the code to actually run the game 
# this means display the questions and answers on the interface

from flask import Flask 
app = Flask(__name__)

import requests
import json
from pprint import pprint
import janitor

def list_question():
    request_url = f"https://opentdb.com/api.php?amount=10"
    response = requests.get(request_url)
    response_data = json.loads(response.text)

    trivia_url = parsed_response["response_data"]["results"]
    trivia_response = requests.get(trivia_url)

    #this code appends the questions in this list
    question_list = []
    for q in response_data["results"]:
        question_list.append(q["question"])

    #this code cleans up the data
    for question in question_list: 
        if "&quot;" in question:
            new_string = question.replace("&quot;", "'")
        if "&#039;s" in question: 
            new_string2 = question.replace("&#039;s", "'")

    #this code appends the answer in this list
    answer_list = []
    for q in response_data["results"]:
        answer_list.append(q["correct_answer"])

    return{"question:": question, "correct_answer:": correct_answer}



#url = "https://opentdb.com/api.php?amount=10"
#
#response = requests.get(url)
#response_data = json.loads(response.text)
#
##this selects all the questions and appends it to this list
#question_list = []
#
#for q in response_data["results"]:
#    question_list.append(q["question"])
##print(question_list)
#
#for question in question_list: 
#    if "&quot;" in question:
#        new_string = question.replace("&quot;", "'")
#    if "&#039;s" in question: 
#        new_string2 = question.replace("&#039;s", "'")
#
#
##this is supposed to print out all of the questions but it prints out the answers as well
#for question in question_list:  
#    print("Question:")
#    print(question)
#
#print("-------------")
#
##this selects all the answers and appends it to this list
#answer_list = []
#
#for q in response_data["results"]:
#    answer_list.append(q["correct_answer"])
##print(answer_list)
#
##this is supposed to print out all of the questions but it 
#for answer in answer_list: 
#    print("Answer:") 
#    print(answer)