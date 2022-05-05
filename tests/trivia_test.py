import os
import pytest

from app.trivia_service import list_question

CI_ENV = os.getenv("CI") == "true"

@pytest.mark.skipif(CI_ENV==True, reason="to avoid issuing HTTP requests on the CI server")
def test_list_question():
    # with questions and answers, returns the following type of data and count how much data there is :
    results = list_question()
    assert isinstance(results, dict)
    assert isinstance(results["question"], list)
    assert len(results["question"]) == 10
    assert len(results["correct_answer"]) == 10
    assert isinstance(results["correct_answer"], list)
    

