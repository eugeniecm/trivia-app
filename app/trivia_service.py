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

    return{"question": question_list, "correct_answer": answer_list}
