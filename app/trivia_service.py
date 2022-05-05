# here is the code to actually run the game 
# this means display the questions and answers on the interface

from flask import Flask 
app = Flask(__name__)

import requests
import json
from pprint import pprint
import janitor

def list_question():
    request_url = f"https://opentdb.com/api.php?amount=10&difficulty=easy&type=boolean"
    response = requests.get(request_url)
    response_data = json.loads(response.text)

    #this code appends the questions in this list
    question_list = []
    for q in response_data["results"]:
        question = q["question"]
        #clean up the data within the trivia API
        question = question.replace("&quot;", "'")
        question = question.replace("&#039;s", "'")
        question = question.replace("&#039;", "'")
        question = question.replace("&eacute;", "e")
        question_list.append(question)

    #this code appends the answer in this list
    answer_list = []
    for q in response_data["results"]:
        answer_list.append(q["correct_answer"])

    return{"question": question_list, "correct_answer": answer_list}

